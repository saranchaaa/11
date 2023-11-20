import cv2
from PIL import Image

cat = 'cat.jpeg'
fc = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
img = cv2.imread(cat)

catt = Image.open(cat)
glasses = Image.open('glasses.png')
catt = catt.convert("RGBA")
glasses = glasses.convert("RGBA")

cf = fc.detectMultiScale(img)

for (x, y, w, h) in cf:
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    glasses = glasses.resize((w, int(h / 3)))
    catt.paste(glasses, (x, int(y+h/4)), glasses)
    catt.save("cattt.png")
    cattt = cv2.imread("cattt.png")
    cv2.imshow("cattt", cattt)
    cv2.waitKey()

