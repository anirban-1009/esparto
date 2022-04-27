# Esparto

This is a follow up Github repo for the facial recognition session it contains all the files mentioned in the session so feel free to look around.

To clone this repository enter the command below.

>git clone https://github.com/anirban-1009/esparto.git

This repository contains both facial recognition using Haar cascade and also a follow up code for object detection using the model from teachable.

It is recommended to create and activate a virtual environment by following this [tutorial](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/ "The tutorial")  without the virtual environment the following steps will work just fine.

## Requirements.txt

To get install all the depencendices enter the following command.

>pip3 install -r "requirements.txt"

## Facial Recognition

The code for facial recognition can be found
[here](https://github.com/anirban-1009/esparto/blob/main/face_det.py "The code")
 to run the code enter first we have the directory enter the command.
>cd esparto

Then to run the script enter the code bellow.
>python face_det.py

or

>python3 face_det.py

## Object Detection using Teachable

There is a model created with teachable enclosed [here](https://github.com/anirban-1009/esparto/blob/main/keras_model.h5 "The model")

The script applying the detection model on facial detection script can be executed by the following command

>python det.py

or 

>python3 det.py

The script implementing the model created with teachable standalone can be executed by the following command

>python static_label.py

or 

>python3 static_label.py

## Masks

[These](https://github.com/anirban-1009/esparto/tree/main/Masks "The masks") are the datasets being used while making [this](https://drive.google.com/file/d/1gFLkIJnktulYjTFhvKamowU4V5GCespG/view?usp=sharing "the project") project just for reference making your own dataset is encouraged.

## Structure of the directory

>├── det.py
├── face_det.py
├── h5.py
├── haarcascade_eye.xml
├── haarcascade_frontalface_default.xml
├── keras_model.h5
├── labels.txt
├── Masks
│   ├── With Mask
│   │   ├── download (1).jpg
│   │   ├── download (2).jpg
│   │   ├── download (3).jpg
│   │   ├── download (4).jpg
│   │   ├── download.jpg
│   │   ├── file-20200408-44160-1qpyrm3.jpg
│   │   ├── images (1).jpg
│   │   ├── images (2).jpg
│   │   ├── images.jpg
│   │   ├── Mask Roundup Image_0.png
│   │   └── woman-wearing-mask.original.jpg
│   └── Without Mask
│       ├── download (1).jpg
│       ├── download (2).jpg
│       ├── download (3).jpg
│       ├── download (4).jpg
│       ├── download (5).jpg
│       ├── download.jpg
│       ├── images (1).jpg
│       ├── images (2).jpg
│       ├── images (3).jpg
│       └── images.jpg
├── README.md
├── requirements.txt
├── static_label.py
├── test1.jpg
└── test2.jpg
