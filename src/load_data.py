import torch
from torchvision import transforms, datasets
from os import listdir, path
from glob2 import glob
trainDataset = "./dataset/train/{posOrNeg}"
import logging


def readFromFile(fileName):
    file = open(fileName, "r") 
    return file.readlines()[0]

def getDirectoryList(dir): 
    print(glob(dir))

def getData(path, posOrNeg): 
    files = glob(path)
    data = list()
    for file in files:
        data.append([ readFromFile(file) , posOrNeg])
    return data

def load_data_set():
    logging.warning('started read from folder at : {time}')
    train_pos_data_path = trainDataset.format(posOrNeg="pos/*")
    train_pos_data = getData(train_pos_data_path, 1)
    print (train_pos_data)

load_data_set()