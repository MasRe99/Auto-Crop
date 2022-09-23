import glob
from PIL import Image

#To set the coordinates as the boundaries
box1 = (300, 300, 1050, 1050)
box2 = (1050, 300, 1800, 1050)
box3 = (300, 1050, 1050, 1800)
box4 = (1050, 1050, 1800, 1800)

#function to crop the image
def compress_image(source_path, dest_path):
    with Image.open(source_path) as img:
        image_cropped1 = img.crop(box1)
        image_cropped2 = img.crop(box2)
        image_cropped3 = img.crop(box3)
        image_cropped4 = img.crop(box4)
#auto save with
        image_cropped1.save(dest_path[:-4] + "-C1" + ".JPG", "JPEG")
        image_cropped2.save(dest_path[:-4] + "-C2" + ".JPG", "JPEG")
        image_cropped3.save(dest_path[:-4] + "-C3" + ".JPG", "JPEG")
        image_cropped4.save(dest_path[:-4] + "-C4" + ".JPG", "JPEG")

#To batch processing
paths = glob.glob("*.JPG")

for path in paths:
    compress_image(path, path[:-4]+ ".JPG")
