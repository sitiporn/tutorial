import torch 
from torch.utils.tensorboard import SummaryWriter # to print to tensorboard  
from torch.utils.data.dataloader import DataLoader
import torchvision
import  torch.optim as optim
from network import Net
import torch.nn as nn 
import torchvision.transforms as transforms


#configs 
batch_sizes = [8, 16, 32, 64]
learning_rates = [0.01, 0.001, 0.0001]
momentum= 0.9
num_epochs = 3  

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
# Preprocessing 

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# load data
trainset = torchvision.datasets.CIFAR10(root='../dataset/dataset/', train=True,
                                        download=True,transform=transform)


classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')





# specify path where we write to and tensorboard can read 

#Hyperparameter search 
for batch_size in batch_sizes:
    for lr in learning_rates: 
         
        trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,shuffle=True, num_workers=2)
       
        #  CNN network 
        net = Net()
        net = net.to(device)

        # loss and optimizer 
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(net.parameters(),lr=lr,momentum=momentum)


        writer = SummaryWriter(f'./runs/exp3/batch_size={batch_size}_lr={lr}_momentum={momentum}')
       
        step = 0  
        print(f"Hyper parameters : batch_size={batch_size}_lr={lr}_momentum={momentum}") 
        losses = [] 
        for epoch in range(num_epochs): # loop over dataset 

            running_loss = 0.0 
              
            for i, data in enumerate(trainloader):
              # get the inputs; data is a list of [inputs, labels]
              inputs, labels = data

              inputs = inputs.to(device)
              labels = labels.to(device)

              # zero the parameters gradients
              optimizer.zero_grad()

              # foward + backward + optimize 
              outputs = net(inputs)
              loss = criterion(outputs,labels)
              loss.backward()
              optimizer.step()
              
              running_loss += loss.item()
              losses.append(loss.item())
              
              # visualize images of each batch 
              #image_grid = torchvision.utils.make_grid(inputs)
              #writer.add_image('Cifar10_images',image_grid)

              # To see distribution of last linear layer for each batch
              writer.add_histogram('fc3',net.fc3.weight,step)
            
              # print statistic eg. loss  
              writer.add_scalar('Training_Loss',loss,step)

                 
              
              
                            
              step += 1 
                            
              
              
              if i % 100 == 100: # print every 2000 mini-batches 
                  print('[%d, %5d] loss: %.3f' %(epoch+1,i+1,running_loss/100))
                  running_loss = 0.0 
                  writer.flush()

        writer.add_hparams({'lr': lr, 'bsize': batch_size},{'hparam/loss': sum(losses)/len(losses)})


writer.close()
print("Training Done !")



"""
    's say we use batch_size equal to daset set 
    # so no need to loop through batch 
    # dummy loss
    loss = (start-epoch+2+torch.randn(1))
    # if your batch_size = dataset size 
    # step = epoch
    step = epoch
    writer.add_scalar('Training_Loss',loss,step)



""" 
