import cv2
import numpy as np
import os
import glob
from tqdm import tqdm
from sklearn.model_selection import train_test_split


def create_lable(label):
    if label == 'Dog':
        return [1, 0]
    elif label == 'Cat':
        return [0, 1]
    else:
        return [0, 0]


def create_dataset(data_path, filename, path, imgSize):
    data = []
    labels = os.listdir(data_path)
    for i in labels:
        new_path = os.path.join(data_path, i)
        for img_name in glob.glob(new_path + "/*.jpg"):
            try:
                img=cv2.imread(img_name)
                img = cv2.resize(img,(imgSize, imgSize))
                label=create_lable(i)
                data.append([img, label])
            except Exception as e:
                print("error")
    file_path = path + '/' + filename
    np.save(file_path, data)
    return data


def create_train_test(dataset, imgSize , filepath ,test_name, train_name):
    X=[]
    y=[]
    np.random.shuffle(dataset)
    for features, labels in dataset:
        X.append(features)
        y.append(labels)
    X=np.array(X).reshape(-1, imgSize, imgSize, 3)
    X_test=X[-2500:]
    Y_test=y[-2500:]
    X=X[:-2500]
    y=y[:-2500]
    np.save(filepath+'/X'+test_name,X_test)
    np.save(filepath+'/Y'+test_name,Y_test)
    np.save(filepath+'/X'+train_name,X)
    np.save(filepath+'/Y'+train_name,y)
    print("All Files are created and save at : ", filepath)




def main():
    print("Starting data pre-processing")

   # META Data / INPUT
    Size=100
    data_filename = "data.npy"
    train_filename = "traindata.npy"
    test_filename = "testdata.npy"
    data_path = "./DATA"
    data = create_dataset(data_path, data_filename, data_path, Size)
    create_train_test(data, Size,data_path, test_filename,train_filename)

    print("Finished data pre-processing")
if __name__ == '__main__':
    main()

