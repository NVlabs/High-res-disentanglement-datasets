# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution 4.0 International License .
# To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/
# or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.


import glob, os
import argparse
import numpy as np
import PIL.Image


def save_images(images, size, image_path):
    img = merge(images, size)
    assert img.ndim == 3

    img = np.rint(img).clip(0, 255).astype(np.uint8)
    PIL.Image.fromarray(img, 'RGB').save(image_path)


def merge(images, size):
    h, w = images.shape[1], images.shape[2]
    c = images.shape[3]
    img = np.zeros((h * size[0], w * size[1], c))
    for idx, image in enumerate(images):
        i = idx % size[1]
        j = idx // size[1]
        img[h * j:h * (j + 1), w * i:w * (i + 1), :] = image

    return img


def main(args):
    """ First need to download the Falcor3D and Isaac3D datasets and put in the current directory. """
    if args.dataset == 'Falcor3D':
        image_dir = 'Falcor3D/images'
        target_dir = os.path.join(args.dest_folder, 'falcor3d_samples')
        factor_sizes = [5, 6, 6, 6, 6, 6, 6]
        factor_names = ['lighting_intensity', 'lighting_x-dir', 'lighting_y-dir', 'lighting_z-dir',
                        'camera_x-pos', 'camera_y-pos', 'camera_z-pos']
    else:
        image_dir = 'Isaac3D/images'
        target_dir = os.path.join(args.dest_folder, 'isaac3d_samples')
        factor_sizes = [3, 8, 5, 4, 4, 4, 6, 4, 4]
        factor_names = ['object_shape', 'robot_x-move', 'robot_y-move', 'camera_height', 'object_scale',
                        'lighting_intensity', 'lighting_y-dir', 'object_color', 'wall_color']

    image_files = sorted(glob.glob(os.path.join(image_dir, '*.png')))
    os.makedirs(target_dir, exist_ok=True)
    factor_bases = np.array(np.prod(factor_sizes) / np.cumprod(factor_sizes), np.int32)
    for (factor_index, factor_size) in enumerate(factor_sizes):
        index_arr = factor_bases[factor_index] * np.arange(factor_size) + np.random.randint(factor_bases[factor_index])
        image_names = [image_files[t] for t in index_arr]
        images = []
        for image_file in image_names:
            assert isinstance(image_file, str), image_file
            img = PIL.Image.open(image_file)
            images.append(np.array(img, dtype=np.float32))
        images = np.array(images)
        save_images(images, (1, factor_size), os.path.join(
            target_dir, 'c{}_{}_traversal.png'.format(factor_index, factor_names[factor_index])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Demo the dataset by showing random latent traversal results.')
    parser.add_argument('--dataset', type=str, default='Isaac3D', help='dataset name: [Isaac3D, Falcor3D].')
    parser.add_argument('--dest_folder', type=str, default='examples', help='path to store latent traversal results.')
    args = parser.parse_args()
    main(args)

