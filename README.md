# Flooding_brains
Creating mesmerizing brain animations by playing with geodesic distances.

<img src="/visuals/movie-okapi_white.gif"/>

## Dependencies
This project is developed using [Debian 10](https://www.debian.org/intro/philosophy) operating systems.

| Package                                                  | Tested version  |
|----------------------------------------------------------|-----------------|
| [Python](https://www.python.org/)                        | 3.7.6           |
| [NumPy](http://www.numpy.org/)                           | 1.17.2          |
| [Nibabel](https://nipy.org/nibabel/)                     | 2.2.1           |
| [PyVista](https://docs.pyvista.org/)                     | 0.30.1          |
| [LayNii](https://github.com/layerfMRI/LAYNII)            | 2.1.0 (in devel)|
| [ffmpeg](https://www.ffmpeg.org/)                        | 4.3.1           |

## Installation
TODO

## Usage
TODO
1. Get borders from a segmented image using `LN2_BORDERIZE`.
2. Get points on borders using `LN2_COLUMNS`.
3. Get geodesic distances from the points on the borders using `LN2_GEODISTANCE`.
4. Use `scripts/step-1_select_camera_angle.py` to find a nice viewing angle.
5. Use `scripts/step-2_render.py` for generating animation frames (png).
6. Use `ffmpeg` script to convert the frames into movies (mp4).


## License
This project is licensed under [MIT](LICENSE).
