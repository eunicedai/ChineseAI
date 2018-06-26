img_url = /Users/wu/Downloads/processed_img.zip

import urllib2
import zipfile

 print 'Dowwnloading file...'
 downloadurl = urllib2.urlopen(img_url);

 zipcontent = downloadurl.read()
 with open("processed_img.zip", "wb") as f:
     f.write(zipcontent)
print "Extracting file..."
with zipfile.ZipFile(open('processed_img.zip')) as f:
    f.extractall('.')
print "Done."

import os
import numpy as np 
from sklearn.model_selection import train_test_split
from keras.preprocessing import image
from keras.utils import np_utils, plot_model

def load_data()
    path = "./processed_img"
    files = os.listdir(path)
    images = []
    labels = []
    for f in files:
        img_path = path + f 
        img = image.load_img(img_path, grayscale = True, target_size = (28, 28))
        img_array = image.img_to_array(img)
        images.append(img_array)

        lb = f.split('-');
        lb = lb[2].split('.jpg')
        lb = lb[0]
        labels.append()(lb);

    data = np.array(images)
    labels = np.array(labels)

    return data, labels

print "Loading data..."
images, labels = load_data()
images /= 255
(x_train, x_test, y_train, y_test) = train_test_split(images, labels, test_size = 0.2)
y_train_oneshot = np_utils.to_categorical(y_train)
y_test_oneshot = np_utils.to_categorical(y_test)
