import imageio
import os

path = 'path/to/image/folder'
image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png', '.gif') ):
        filenames.append(os.path.join(path, filename))

filenames.sort() 

images = [imageio.imread(f) for f in filenames]

imageio.mimsave(os.path.join('output_name.gif'), images, duration = 0.05) # set duration
