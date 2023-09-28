# AIUB_CS_Python_Brain_Tumor_Detection
This Python script is a Brain Tumor Detection web application that uses a convolutional neural network (CNN) trained on medical images to classify brain tumor images into two categories: "No Brain Tumor" and "Yes Brain Tumor." The application is built using Flask and allows users to upload MRI or CT scan images of the brain for real-time tumor detection.

Key components of the script include:

Data Preprocessing: The script loads and preprocesses brain tumor images from a specified directory, resizing them to a consistent input size and normalizing pixel values.

CNN Model: It defines a CNN model using Keras that consists of convolutional layers, max-pooling layers, and dense layers. The model is trained using categorical cross-entropy loss and Adam optimizer.

Model Saving and Loading: The trained model is saved to a file and loaded when needed for predictions.

Web Application: The Flask web application provides a simple user interface for uploading images. When a user uploads an image, it passes the image to the loaded model for inference and returns the classification result.

To use this script, follow these steps:

Install the required Python packages (OpenCV, TensorFlow, Keras, PIL, Flask).
Prepare your dataset of brain tumor images and organize them into "no" (no tumor) and "yes" (tumor) subdirectories within a specified directory.
Train the model using your dataset (not shown in this code).
Run the Flask application, and it will provide a local web interface for uploading images and getting predictions.
This script is a useful tool for anyone interested in implementing a brain tumor detection system and can serve as a starting point for further development and customization.
