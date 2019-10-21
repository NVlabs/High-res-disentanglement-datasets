# High resolution disentanglement datasets

This repository contains the *Falcor3D* and *Isaac3D* datasets, which present a 
state-of-the-art challenge for controllable generation in terms of 
image resolution, photorealism, and richness of style factors, 
as compared to existing disentanglement datasets.


## Falor3D
The Falcor3D dataset consists of `233,280` images based on the 3D scene of a living room, 
where each image has a resolution of `1024x1024`. The 
meta code corresponds to all possible combinations of `7` factors of variation:

* lighting_intensity (5)
* lighting_x-dir (6)
* lighting_y-dir (6)
* lighting_z-dir (6)
* camera_x-pos (6)
* camera_y-pos (6)
* camera_z-pos (6)

Note that the number `m` behind each factor represents that the factor has `m` possible values, 
uniformly sampled in the normalized range of variations [0, 1].

Each image has as filename `padded_index.png` where
```
index = lighting_intensity * 46656 + lighting_x-dir * 7776 + lighting_y-dir * 1296 + 
lighting_z-dir * 216 + camera_x-pos * 36 + camera_y-pos * 6 + camera_z-pos
```
padded_index = index padded with zeros such that it has 6 digits.


To see the Falcor3D images by varying each factor of variation individually, 
you can run 
```bash
python dataset_demo.py --dataset Falor3D
```
and the results are saved in the `examples/falcor3d_samples` folder.

You can also check out the Falcor3D images here: 
[falcor3d_samples_demo](assets/falcor3d_samples_demo.jpg),
which includes all the ground-truth latent traversals.


## Isaac3D 
The Isaac3D dataset consists of `737,280` images, based on the 3D scene of a kitchen, 
where each image has a resolution of `512x512`. The 
meta code corresponds to all possible combinations of `9` factors of variation:


* object_shape (3)
* object_scale (4)
* camera_height (4)
* robot_x-movement (8)
* robot_y-movement (5)
* lighting_intensity (4)
* lighting_y-dir (6)
* object_color (4)
* wall_color (4)

Similarly, the number `m` behind each factor represents that the factor has `m` possible values, 
uniformly sampled in the normalized range of variations [0, 1].


Each image has as filename `padded_index.png` where
```
index = object_shape * 245760 + object_scale * 30720 + camera_height * 6144 + 
robot_x-movement * 1536 + robot_y-movement * 384 + lighting_intensity * 96 + 
lighting_y-dir * 16 + object_color * 4 + wall color
```
padded_index = index padded with zeros such that it has 6 digits.


To see the Isaac3D images by varying each factor of variation individually, 
you can run 
```bash
python dataset_demo.py --dataset Isaac3D
```
and the results are saved in the `examples/isaac3d_samples` folder.

You can also check out the Isaac3D images here: 
[isaac3d_samples_demo](assets/isaac3d_samples_demo.jpg),
which includes all the ground-truth latent traversals.


## Links to datasets
The two datasets can be downloaded from Google Drive:

* Falcor3D (98 GB): [link](https://drive.google.com/uc?export=download&id=15njKf7WsBYoFVoLDGyXe4na3MYnTYXOF)
* Isaac3D (190 GB): [link](https://drive.google.com/uc?export=download&id=1vFkgK4CpHpCOBOU7l07yocrqAqr2uDox)

Besides, we also provide a downsampled version (resolution 128x128) of the two datasets:

* Falcor3D_128x128 (3.7 GB): [link](https://drive.google.com/uc?export=download&id=1XAQfFK1x6cpN1eiovbP0hVfLTm5SsSoJ)
* Isaac3D_128x128 (13 GB): [link](https://drive.google.com/uc?export=download&id=1OmQ1G2wnm6eTsSFGTKFZZAh5D3nQTW1B)


## License
This work is licensed under a Creative Commons Attribution 4.0 International License by NVIDIA Corporation
(https://creativecommons.org/licenses/by/4.0/).
