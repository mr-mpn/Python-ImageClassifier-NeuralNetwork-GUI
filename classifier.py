from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np

class_names = {  
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck',
}

model = models.load_model('baseline.keras')  #to read the trained model


def predict_image(model , path_to_image):
    img =  Image.open(path_to_image) #Open the image the user has provided
    img = img.convert('RGB')  #make sure it's RGB  (Like how the model has been trained)
    img = img.resize((32,32)) #Make sure it's 32 pixels  (Like how the model has been trained)
    data = np.asarray(img)  #we want to normalize the recieved image , first we can make convert to an array using numpy library
    data = data/225.
    probs = model.predict(np.array([data])[:1])  #what are the probability that our image belongs to each class
    
    top_prob = probs.max()  #what is the biggest probability
    top_pred = class_names[np.argmax(probs)]  #which class has this probability
    
    return top_prob , top_pred
    
    
img_path = "placeholder_image.png"
content = ""
prob = 0
predict = ""

#index ="# Hello from python"  taipy let' us use markdown syntax it behaves the same as index ="<h1>Hello from python</h1>"
index = """
<|text-center|
<|{"logo.png"}|image|width = 25vw|>

<|{content}|file_selector|extensions=.png|>
Select an image from your file system

<|{predict}|>

<|{img_path}|image|>

<|{prob}|indicator|value = {prob}|min = 0|max = 100|width = 25vw|>
>
"""

def on_change(state,var_name,var_value):  #This function will be automatically executed when an image is uploaded by the user (It's an Event)
    # print("Variable name :",var_name) #The name of the variable will be content, since we defined the user input as {content} in the upper part of the code
    # print("The path to the variable : ",var_value) #The uploaded file will be stored in the local path of the machine which is running the code
    if var_name == "content": #Update our image
        top_prob , top_pred = predict_image(model , var_value)
        state.prob  = round(top_prob * 100)  #change the value of probability
        state.predict = "This is a " + top_pred #change the value of prediction
        print(top_pred)
        state.img_path = var_value   #Now the path of the uploaded image will be replaced with the placeholderimage
        
        
app = Gui(page = index)

if __name__ == "__main__":
    app.run(use_reloader=True)   #Runs our code on http://127.0.0.1:5000/ , #Having use_reloader=True let's us to apply changes to the code and see the results in the webpage 