from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the model
model = load_model('keras_model.h5')

cap = cv2.VideoCapture(0)
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.


frameWidth = 1280
frameHeight = 720


while 1:
    # disable scientific notation for clarcv2.imshow('frame',img_text)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        breakity


    np.set_printoptions(suppress=True)

    # Create the array of the right shape to feed into the keras model.
    # We are inputting 1x 224x224 pixel RGB image.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # capture image
    check, frame = cap.read()
    # mirror image - mirrored by default in Teachable Machine
    # depending upon your computer/webcam, you may have to flip the video
    # frame = cv2.flip(frame, 1)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # crop to square for use with TM model
    margin = int(((frameWidth-frameHeight)/2))
    square_frame = frame[0:frameHeight, margin:margin + frameHeight]
    # resize to 224x224 for use with TM model
    resized_img = cv2.resize(square_frame, (224, 224))
    # convert image color to go to model
    model_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

    # turn the image into a numpy array
    image_array = np.asarray(model_img)
    # normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # load the image into the array
    data[0] = normalized_image_array

    # run the prediction
    predictions = model.predict(data)


    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0,255,25)
    lineType = cv2.LINE_4
    if predictions[0][0] >= 0.7:
        text ='without mask'
    
    elif predictions[0][1] >= 0.7:
        text = 'with mask'

    for (x,y,w,h) in faces:
        org = (x, y)
        img_rect = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        img_text = cv2.putText(img_rect, text, org, fontFace, fontScale, color, lineType)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow('frame',img_text)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyWindows()