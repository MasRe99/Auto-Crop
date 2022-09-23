import glob
from PIL import Image

box1 = (300, 300, 1050, 1050)
box2 = (1050, 300, 1800, 1050)
box3 = (300, 1050, 1050, 1800)
box4 = (1050, 1050, 1800, 1800)

def compress_image(source_path, dest_path):
    with Image.open(source_path) as img:
        image_cropped1 = img.crop(box1)
        image_cropped2 = img.crop(box2)
        image_cropped3 = img.crop(box3)
        image_cropped4 = img.crop(box4)

        image_cropped1.save(dest_path[:-4] + "1" + ".JPG", "JPEG")
        image_cropped2.save(dest_path[:-4] + "2" + ".JPG", "JPEG")
        image_cropped3.save(dest_path[:-4] + "3" + ".JPG", "JPEG")
        image_cropped4.save(dest_path[:-4] + "4" + ".JPG", "JPEG")


paths = glob.glob("*.JPG")

for path in paths:
    compress_image(path, path[:-4]+ ".JPG")

"""import glob
from PIL import Image

box1 = (300, 300, 1050, 1050)
box2 = (1050, 300, 1800, 1050)
box3 = (300, 1050, 1050, 1800)
box4 = (1050, 1050, 1800, 1800)

def crop_image(source_path, dest_path):
    with Image.open(source_path) as img:
        img_crop1 = img.crop(box1)
        img_crop.save(dest_path)

paths = glob.glob(".JPG")
for path in paths:
    crop_image(path, path[:-4] + ".JPG")
"""
"""for image in glob.glob("Dataset/*.jpg"):
    print("Processing {}...".format(image))
    im1_crop = image.crop(box1)
    im2_crop = image.crop(box2)
    im3_crop = image.crop(box3)
    im4_crop = image.crop(box4)

    im_save = im1_crop.save("cropped1_" + image)
    im_save = im2_crop.save("cropped2_" + image)
    im_save = im3_crop.save("cropped3_" + image)
    im_save = im4_crop.save("cropped4_" + image)
"""