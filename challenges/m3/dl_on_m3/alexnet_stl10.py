'''
This script is used to train a AlexNet on the STL10 dataset. It is based on previous HPC training materials by (https://github.com/Yusuke710)
'''

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.models as models
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch.utils.data.dataloader as dataloader

import os
import random
import numpy as np
import matplotlib.pyplot as plt

#the size of our mini batches
batch_size     = 64
#How many itterations of our dataset
num_epochs     = 10
#optimizer learning rate
learning_rate  = 1e-4
#initialise best valid accuracy 
best_valid_acc = 0
#where to load/save the dataset from 
data_set_root = "."
# store model paramter
save_checkpoint = True 
model_name = 'model.pt'



#Set device to GPU_indx if GPU is avaliable
GPU_indx = 0
device = torch.device(GPU_indx if torch.cuda.is_available() else 'cpu')


#Prepare a composition of transforms
transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize(144),
            transforms.RandomCrop(96),
            transforms.RandomHorizontalFlip(),
            transforms.Normalize([0.1307], [0.308])])

#Define our STL10T Datasets
#https://pytorch.org/docs/stable/torchvision/datasets.html
train_data = datasets.STL10(data_set_root, split='train', download=True, transform=transform)
test_data = datasets.STL10(data_set_root, split='test', download=True, transform=transform)

#We are going to split the test dataset into a train and validation set 80%/20%
validation_split = 0.8

#Determine the number of samples for each split
n_train_examples = int(len(train_data)*validation_split)
n_valid_examples = len(train_data) - n_train_examples

#The function random_split will take our dataset and split it randomly and give us dataset
#that are the sizes we gave it
#Note: we can split it into to more then two pieces!
train_data, valid_data = torch.utils.data.random_split(train_data, [n_train_examples, n_valid_examples],
                                                       generator=torch.Generator().manual_seed(42))

print(f'Number of training examples: {len(train_data)}')
print(f'Number of validation examples: {len(valid_data)}')
print(f'Number of testing examples: {len(test_data)}')


#Create the training, Validation and Evaluation/Test Datasets
train_loader = dataloader.DataLoader(train_data, shuffle=True, batch_size=batch_size)
valid_loader = dataloader.DataLoader(valid_data, batch_size=batch_size)
test_loader  = dataloader.DataLoader(test_data, batch_size=batch_size)


# define the netwrok to use
net = models.alexnet(pretrained=True)
num_ftrs = net.classifier[6].in_features
net.fc = nn.Linear(num_ftrs, 10)
net.fc = net.fc.to(device)
net = net.to(device)
#view the network
print('-----------------------------')
print('Defined Deeplearning Network:')
print(net)
print('-----------------------------')


#Pass our network parameters to the optimiser set our lr as the learning_rate
optimizer = optim.Adam(net.parameters(), lr = learning_rate)
#Define a Cross Entropy Loss
loss_fun = nn.CrossEntropyLoss()

#This function should perform a single training epoch using our training data
def train(net, device, loader, optimizer, loss_fun):
    
    #initialise counter
    epoch_loss = 0
    
    #Set Network in train mode
    net.train()
    for i, (x, y) in enumerate(loader):
        #Forward pass of image through network and get output
        fx = net(x.to(device))
        
        #Calculate loss using loss function
        loss = loss_fun(fx, y.to(device))

        #Zero Gradents
        optimizer.zero_grad()
        #Backpropagate Gradents
        loss.backward()
        #Do a single optimization step
        optimizer.step()
        
        #create the cumulative sum of the loss and acc
        epoch_loss += loss.item()

    epoch_loss /=  len(loader)
        
    #return the average loss from the epoch as well as the logger array       
    return epoch_loss


#This function should perform a single evaluation epoch, it WILL NOT be used to train our model
def evaluate(net, device, loader, loss_fun):
    
    #initialise counter
    epoch_loss = 0
    epoch_acc = 0
    
    net.eval()
    with torch.no_grad():
        for i, (x, y) in enumerate(loader):
            #Forward pass of image through network
            x = x.to(device)
            fx = net(x)
            y = y.to(device)
            #Calculate loss using loss function
            loss = loss_fun(fx, y)
            
            #log the cumulative sum of the loss
            epoch_loss += loss.item()

            #log the cumulative sum of the acc
            epoch_acc += (fx.argmax(1) == y).sum().item()

    epoch_loss /=  len(loader)
    epoch_acc /= len(loader.dataset)
    #return the accuracy from the epoch     
    return epoch_loss, epoch_acc



training_loss_logger = []
validation_loss_logger = []
validation_acc_logger = []
training_acc_logger = []

# run training 
for epoch in range(num_epochs):
    
    #call the training function and pass training dataloader etc
    train_loss = train(net, device, train_loader, optimizer, loss_fun)
    valid_loss, valid_acc = evaluate(net, device, valid_loader, loss_fun)
    training_loss_logger.append(train_loss)
    validation_loss_logger.append(valid_loss)

    if (valid_acc > best_valid_acc):
        best_valid_acc = valid_acc
        if save_checkpoint:
            print("Saving Model")
            torch.save(net, model_name)
    print(f'| Epoch: {epoch+1:02} | Train Loss: {train_loss:.2f} | Val. Loss: {valid_loss:.2f} | Val. Acc: {valid_acc*100:05.2f}%')
    
print("Training Complete")

plt.figure(figsize = (10,10))
train_x = np.linspace(0, num_epochs, len(training_loss_logger))
plt.plot(train_x, training_loss_logger, c = "y")
valid_x = np.linspace(0, num_epochs, len(validation_loss_logger))
plt.plot(valid_x, validation_loss_logger, c = "k")

plt.title("Alexnet STL10 Training Loss")
plt.legend(["Training loss", "Validation loss"])
plt.savefig('Alexnet_STL10_log.png')




# evaluate on test set 
#call the evaluate function and pass the evaluation/test dataloader etc
net = torch.load(model_name)
_, test_acc = evaluate(net, device, test_loader, loss_fun)
print("The total test accuracy is: %.2f%%" %(test_acc*100))