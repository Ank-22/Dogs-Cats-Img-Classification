
🐶 & 🐱
# Dogs-Cats-Img-Classification 


### INFO

This is to try on basic image-classification using Tansfer Learning and CNN-(Convolutional Neural Network) for classifying cats and dogs. The dataset is taken from [Microsoft cat & dog dataset](https://www.microsoft.com/en-us/download/details.aspx?id=54765) 

### Approch

1. I will read all the images and convert them to a multi-dimension array. I have seen a lot of other approaches online where people have converted the image in greyscale but for a challenge, I will be doing with RGB. 

2. After converting in an array, the image will be label whether Cat or Dogs.

3. The arrays of the image which will be stacked on top using NumPy for giving the input to NN-(Neural Network)

4. After Training of the model depending on the statics the fine-tuning of the model will be done or feature engineering for increasing the accuracy of the model 


### File Description

#### Data_Preprocessing.py 

- This script file read images from the location and converts its in numpy array and saves it to.

- This file also spilts the data in train and test for each X and Y 

- The file are made of function so it can be imported and used in other projects

#### Data

This floder contain an sample of test data_set which is maded by [Data_Preprocessing.py](Data_Preprocessing.py)




### Version

V0.0.0 - Intialization of Reppo

V0.0.1 - Deciding Apporach 

V0.1.0 - Made Data_precoressing.py 

V0.1.1 - Made Data_Preprocessing.py in funtional/Modular manner

V0.1.2 - Added Sample Data of X_test and Y_test 
