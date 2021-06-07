# Flooding_brains
Creating mesmerizing brain animations by playing with geodesic distances.

<img src="/visuals/movie-okapi_white_crop.gif"/>

## Dependencies
| Package                                                  | Tested version  |
|----------------------------------------------------------|-----------------|
| [Python](https://www.python.org/)                        | 3.7.6           |
| [NumPy](http://www.numpy.org/)                           | 1.17.2          |
| [Nibabel](https://nipy.org/nibabel/)                     | 2.2.1           |
| [PyVista](https://docs.pyvista.org/)                     | 0.30.1          |
| [LayNii](https://github.com/layerfMRI/LAYNII)            | 2.1.0 (in devel)|
| [ffmpeg](https://www.ffmpeg.org/)                        | 4.3.1           |

This project is developed using [Debian 10](https://www.debian.org/intro/philosophy) operating system.

## Installation
Flooding brains project is just a script compilation for now. Therefore make sure to install each dependency to be able run the scripts.

## Beginner's guide
1. Change directory to where your scripts are stored. For example you can use the `scripts` directory that comes with this repository: `cd /path/to/flooding/brains/scripts`

### Prepare inputs for animation
2. Get borders from a segmentation file by running `python prep-flooding_step-01_borders.py`.
3. Get points on the borders by running: `python prep-flooding_step-02_points.py`.
4. Get geodesic distances from the points on the borders by running: `python prep-flooding_step-03_distances.py`

### Create animation frames
5. Run `python anim-flooding_step-1_prep.py` to find a nice viewing angle.
6. Run `python anim-flooding_step-2_render.py` for generating animation frames (png).

### Compile frames into a movie
7. Run `bash movie-flooding_compile.sh` to convert the frames into movies (mp4).

### What comes next?
Feel free to read, edit and augment all the example scripts to generate different animations.

# Support
Please use the [GitHub issues](https://github.com/ofgulban/flooding_brains/issues) for questions.

## License
This project is licensed under [MIT](LICENSE).
