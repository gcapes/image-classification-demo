from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os
from tabulate import tabulate
import csv
from natsort import natsorted
import sys

model_file = sys.argv[1]
# Load the model
model = load_model(model_file)

with open('labels.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    labels = list(reader)
category_labels = [sub[1] for sub in labels]

test_dir = 'test-data'
test_files = os.listdir(test_dir)
test_files = natsorted([os.path.join(test_dir, file) for file in test_files])
n_files = len(test_files)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(n_files, 224, 224, 3), dtype=np.float32)

for i, file in enumerate(test_files):
    image = Image.open(file)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[i] = normalized_image_array

# run the inference
prediction = model.predict(data)

entries = []
for file, [cat1, cat2] in zip(test_files, (prediction*100).round()):
    entries.append([os.path.basename(file), f'![]({file})', cat1, cat2])
header = ['file', 'image'] + category_labels
print(tabulate(entries, headers=header, tablefmt='github'))
