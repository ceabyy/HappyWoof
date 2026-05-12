**HappyWoof: an AI-powered tool to help understand your dogs' feelings!**

This website is a project I decided to work on after graduating from my Bachelor of Science (Technology), where I majored in Signal Processing and Machine Learning. It mainly uses a **Deep Convolutional Neural Network (DCNN)**, a type of neural network I encountered during my bachelor thesis work. The model is trained on ResNet18.

ResNet18 was a good choice to use the dataset on, given the limited computational resources I have at home, and the efficiency is suitable. The model was trained on a labelled dataset of 4000 images of dogs from Kaggle. The dataset can be found through this link (https://www.kaggle.com/datasets/danielshanbalico/dog-emotion).

***The dogs' emotions can be classified into four categories: Happy, Sad, Relaxed and Angry.***

**Motivation**

I wanted to reinforce my practical learning from my studies, and understand the practical applications better from the theoretical parts of my studies. I also really love dogs (and animals in general), so I thought to myself, why not try out a project that incorporates them somehow? Additionally, I wanted to learn HTML and CSS better so that I had a platform for the machine learning to be used.

**Process**

I worked on the model first, using the pyTorch library. The model was trained on a dog emotion images dataset from Kaggle (as linked earlier). I had some help from Claude to understand some syntax and to translate some of my knowledge from previously using TensorFlow in a course. pyTorch seemed to be much more useful, so I stuck with it. I then made a frontend through a website, and I struggled a bit refining the CSS-grid layouts so using Claude I managed to restrict the overflow to make sure that the photo grid is a fixed size. I then used JavaScript and Flask to make the website functional, and so that I could call the model function in Python from the JS script, and receive the data as well. 

After the core functionalities were done, I deployed the backend (Python) on a Hugging Face space, and used Github pages for the frontend. A bit of troubleshooting needed to be done (mostly to do with respository problems), so I used Claude to help with these unique problems.

**What I learned**

I mainly learned a lot more about pyTorch, and I look forward to using it in another future project to get used to the workflow and remember the syntax better. I also got a deeper understanding of CSS, and a better understanding of how Git version control can streamline my processes between local testing and testing after deployment. I also became a lot more familiar with the works around implementing a CNN practically, after having researched them for my bachelor thesis.

**Future Considerations**
I may introduce a toggle/setting so that the website can also detect human emotions, or cat emotions, for instance. So the user has the ability to choose whose emotions they want the model to figure out. This would mean I would need to train a few other models and find suitable datasets. I have also considered making it so that the photos are saved even if you log off, but that seems a bit too extra for a project like this.
