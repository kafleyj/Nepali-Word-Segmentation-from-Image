"""
For Testing purposes
    Take image from user, crop the background and transform perspective
    from the perspective detect the word and return the array of word's
    bounding boxes
"""

import page
import words
from PIL import Image
import cv2
import os

# User input page image 
#image = cv2.cvtColor(cv2.imread("test.jpg"), cv2.COLOR_BGR2RGB)

folder = 'Text images'
images = []
for filename in os.listdir(folder):
    print(filename)
    img = cv2.imread(os.path.join(folder,filename))
    if img is not None:
        images.append(img)
    image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)



# Crop image and get bounding boxes
    crop = page.detection(image)
    boxes = words.detection(crop)
    lines = words.sort_words(boxes)

# Saving the bounded words from the page image in sorted way
    i = 0
    internal_folder = os.path.splitext(filename)[0]
    os.mkdir("segmented"+'/'+ str(internal_folder))
    for line in lines:
        text = crop.copy()
        for (x1, y1, x2, y2) in line:
            # roi = text[y1:y2, x1:x2]
            save = Image.fromarray(text[y1:y2, x1:x2])
            # print(i)

            save.save("segmented"+"/"+ str(internal_folder) + "/" + str(i) + ".png")
            i += 1