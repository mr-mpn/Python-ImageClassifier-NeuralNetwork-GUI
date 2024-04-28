Here is a step-by-step guide on this application:

1- Taipy is used as the graphical user interface for our application.
The Taipy GUI library provides Python classes that make it easy to create powerful web applications in minutes.

What is a graphical user interface?
A graphical user interface (or GUI) displays and organizes graphic elements on the user's device. These elements represent application data and allow users to interact with the application code.

There are mechanisms in place to install communication between the server, running at the heart of the application, and the graphical interface presented to end-users.

For more information on taipy : 
https://docs.taipy.io/en/release-3.0/manuals/gui/

---------------------------------------------

2- Neural Network Machine Learning approach is used in order to make a prediction on an image provided by the user.
The training is executed based on the CIFAR10 Dataset provided by tensorflow
this model is suitable for performing classification tasks, recognizing 10 different entities
airplanes, automobiles, birds, cats, deer, dogs, frogs, horses, ships and trucks.

CIFAR10 provides 50000 train samples and 10000 test samples in RGB
All samples are 32px * 32px
RGB: RED, GREEN, BLUE

---------------------------------------------

To train our model : 
First step = Normalization of the samples (pixel values) 
To do so we have x_train = x_train / 255 (which 255 is the (max-min) value of the value for each pixel)

Each sample contains pixels, and each pixel has a value between 0 and 255 which is the color intensity 
By Normalization, the values go in the range of zero and organize

Then we use one-hot encoding to change the decimal values to their binary 
x_train: pixel values
Y_train: class of the image (airplanes, automobiles, birds, cats, deer, dogs, frogs, horses, ships and trucks)

one hot encode behaves as follows:
Where we convert decimal values to their binary representation. Such that:
- the class of ```0``` is One-Hot-Encoded into ```1000000000```
- the class of ```1``` is One-Hot-Encoded into ```0100000000```
- the class of ```2``` is One-Hot-Encoded into ```0010000000```
...
- the class of ```9``` is One-Hot-Encoded into ```0000000001```

9 binary placements x x x x x x x x x x 
and for each class of the placements becomes one

from keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

---------------------------------------------

next, we build our model with the appropriate number of nodes and optimizer = 'adam' 
then we train the model with x_train and y_train
epochs = 10, shows how times it goes through the entire dataset
then the trained model is saved as baseline.keras
Now we can use the trained model in our code 'classifier.py'!  

---------------------------------------------
Reminder: 
pip install tensorflow 

pip install taipy

Credit to Python Simplified Youtube Channel : https://www.youtube.com/watch?v=h0dglh9elCw&t=560s

------------------------------------------
![Readme](https://github.com/mr-mpn/Python-ImageClassifier-NeuralNetwork-GUI/assets/135954454/8ff9a139-7773-4555-bbda-d452fd38eceb)


