# **Brain Tumor Detection Using CNN**
This repository contains the code and resources for a project focused on detecting brain tumors using Convolutional Neural Networks (CNNs). The project aims to leverage deep learning techniques to enhance the early diagnosis of brain tumors, ultimately contributing to improved healthcare outcomes.

## Overview
Brain tumors are a significant health concern, and early detection is crucial for effective treatment. This project explores the use of CNNs, a type of deep learning model, to analyze MRI images and identify the presence of brain tumors. By training and evaluating CNN models on large datasets of brain MRI images, the project seeks to develop an accurate and reliable system for automated tumor detection.

## Key Features
### * CNN architecture design for brain tumor detection
### * Dataset preparation and preprocessing techniques
### * Implementation of CNN models using TensorFlow and Keras
### * Integration with a mini hospital management system for real-world application
### * Evaluation of model performance and accuracy

## Getting Started
### * Clone the repository to your local machine.
### * Install the necessary dependencies which is given below using pip.
### * Used IDE is "JetBrains PyCharm 2018.1.3" with given python interpreter environment.
      - Python version : 3.7.9
      - Django version : 3.2.25
      - Keras version : 2.8.0
      - Mysqlclient version : 1.4.6
      - Numpy version : 1.21.6
      - Pandas version : 1.3.5
      - Pillow version : 9.5.0
      - Tensorflow version : 2.8.0
### * Follow the instructions in the project documentation to train and evaluate CNN models.
#### I can't provide the trained model because of it's size (around 509Mb), so i provided a folder "Used_CNN_Model_Architecture" which have the "Anaconda" file to learn and create the model you can get the MRI dataset from Kaggel. 
### * Anaconda Environment I am used
      - Tensorflow version : 2.3.0
      - Keras version : 2.3.1
      - Py-opencv version : 3.4.2
      - Python version : 3.7 
### * Explore the provided model code which is used in the project for reference(Remaining code will be in the folder mentioned above). 

      EPOCHS = 10 
      STEPS = 138
      LR = 1e-3
      BATCH_SIZE = 32
      WIDTH = 224
      HEIGHT = 224
      DEPTH = 3
      
      # Number of classes
      num_classes = 5
      model = Sequential()
      
      # Convolutional layers
      model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
      model.add(MaxPooling2D((2, 2)))
      model.add(Conv2D(64, (3, 3), activation='relu'))
      model.add(MaxPooling2D((2, 2)))
      model.add(Conv2D(128, (3, 3), activation='relu'))
      model.add(MaxPooling2D((2, 2)))
      
      # Flattening layer
      model.add(Flatten())
      
      # Fully connected layers
      model.add(Dense(512, activation='relu'))
      model.add(Dropout(0.5))
      model.add(Dense(256, activation='relu'))
      model.add(Dropout(0.5))
      
      # Output layer
      model.add(Dense(num_classes, activation='softmax'))  

## Usage
### * Train CNN models using Kaggle's datasets.
### * Evaluate model performance on test datasets.
### * Integrate the trained models into your own applications for brain tumor detection.

## Contribution
Here, we present the unique advancements and original contributions of the project on brain tumor detection using Convolutional Neural Networks (CNNs).

#### * Novel Methodologies
Introducing innovative approaches for CNN architecture design, dataset preparation, and technical implementation.

#### * CNN Architecture Design
Developing new CNN architectures tailored specifically for brain tumor detection, optimizing model performance, and ensuring accurate classification of MRI images.

#### * Dataset Preparation
Curating and preparing extensive datasets of brain MRI images, including preprocessing techniques to enhance data quality and facilitate model training.

#### * Technical Implementation
Implementing state-of-the-art deep learning techniques using TensorFlow and Keras to train and deploy CNN models for real-world applications in brain tumor detection.

These contributions represent a significant advancement in the field of medical imaging and hold promise for improving early diagnosis and treatment of brain tumors.


## License
This project is licensed under persional license of myself.

## If you need the model and the dataset and all the paper work related to this project you can visit the telegram channel provided given below.
### <a href="https://t.me/+riFFTt0hHxg4NjZl">channel_link</a>
