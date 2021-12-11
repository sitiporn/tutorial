# Purpose of this tutorial to help students 


### Activate tensorboard option 

1. Running TensorBoard remotely

- When working on a remote server, you can use SSH tunneling to forward the port of the remote server to your local machine at port (port 6006 in this example)

  - containner on remote server 
  -
```bash
ssh -L 6006:localhost:6006 containner_name 
```
or  
  - remote server_name (eg. puffer)
  
```bash
ssh -L 6006:localhost:6006 puffer 
```

-  Then launch on remote server with 2.1 or 2.2 command
2. On local machine 

- 2.1 Normal tensorboard 
```bash
tensorboard --logdir=runs
```
- 2.2 Dev Tensorboard (able to share link)

```bash
tensorboard dev upload --logdir runs
```
### Usage
- write log to runs file 
```bash
python3 demo2.py
```

## Examples after follow instructions

### Losses 


![image](https://user-images.githubusercontent.com/31414731/141222725-8a8b037f-2d25-4829-b4f7-e8b6c4d8e67b.png)


### Weight distribution


![image](https://user-images.githubusercontent.com/31414731/141222818-20d12839-b427-43f1-8c89-aa541229e341.png)

![image](https://user-images.githubusercontent.com/31414731/141222844-e5cb903c-74d0-49cf-81c9-f539eee4b3e2.png)


### Hyperparameters interaction 



![image](https://user-images.githubusercontent.com/31414731/141223000-5f8986b4-d898-46a1-a8f9-db38cb4ae1f2.png)
