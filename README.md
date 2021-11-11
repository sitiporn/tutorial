# tutorial


### Activate tensorboard option 

1. On remote server 

map the remote port to a local port run on local machine

```bash
ssh -L 6006:localhost:6006 containner_name
```
2. On local machine 

- 2.1 Normal tensorboard 
```bash
tensorboard --logdir=runs
```
- 2.2 Dev Tensorboard (able to share link)

```bash
tensorboard dev upload --logdir runs
```

### Losses 


![image](https://user-images.githubusercontent.com/31414731/141222725-8a8b037f-2d25-4829-b4f7-e8b6c4d8e67b.png)


### Weight distribution


![image](https://user-images.githubusercontent.com/31414731/141222818-20d12839-b427-43f1-8c89-aa541229e341.png)

![image](https://user-images.githubusercontent.com/31414731/141222844-e5cb903c-74d0-49cf-81c9-f539eee4b3e2.png)


### Hyperparameters interaction 



![image](https://user-images.githubusercontent.com/31414731/141223000-5f8986b4-d898-46a1-a8f9-db38cb4ae1f2.png)
