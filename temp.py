import torch 
import torch.nn as nn
import os
import pandas as pd

# /home/satya/Desktop/Research papers/yolo/data/test.csv
train_path = os.path.join('data','train.csv')
test_path = os.path.join('data','test.csv')
train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)


train_data[:100].to_csv('sample_train.csv',index = False)
test_data[:100].to_csv('sample_test.csv', index = False)


