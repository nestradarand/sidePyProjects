from PIL import Image
import os

path = os.getcwd()

dirs = os.listdir(old_path)

# opens file with names of smiling pictures (comment out)
#file = open('non_smile_image_names.txt', 'r')
#smiles = []
#for line in file:
#    line = line[:-5]
#    smiles.append(line)
#file.close()

for item in dirs:
    item_check = item[:-4]  # removes different image format
    if 'resized' not in item and item != '.DS_Store':
        im = Image.open(old_path + "/" + item)
        f, e = os.path.splitext(item)
        imResize = im.resize((180,180), Image.ANTIALIAS)
        imResize.save(new_path + f + '_resized.jpg', 'JPEG', quality=90)

