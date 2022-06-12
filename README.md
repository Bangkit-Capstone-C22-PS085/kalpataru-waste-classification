
![Logo Kalpataru](https://raw.githubusercontent.com/Bangkit-Capstone-C22-PS085/kalpataru-waste-classification/master/assets/logo.png)
<h2>A machine learning model build with Tensorflow to waste classification</h2>
<h1></h1>
<p>Hi. this is our repository for our project in capstone project Bangkit 2022. Our team consist of 2 people from Machine Learning Path.

All of the project management we take a place with Github repository, to distinguish each path we create a different repository.</p>

## Our Machine Learning Member
|            Nama          |  Bangkit ID  |       Path       |
|:------------------------:|:------------:|:----------------:|
|  Eko Nur Cahyo           |  M7110F1434  | Machine Learning |
|  Rizal Saifulloh Fatah   |  M2110F1433  | Machine Learning |

## Simple Description About Our Project
In this project we created a machine learning that is used to detect a waste and classify the waste into several classifications including 
- cardboard 
- metal 
- glass
- plastic
- paper 
<br>Then we also give some decisions for the results by showing the accuracy of the predictions.

## Our Infrastructure
![Machine Learning Infrastructure](https://raw.githubusercontent.com/Bangkit-Capstone-C22-PS085/kalpataru-waste-classification/master/infrastructure.png)

## Our Import Library on Project
For development you must install several import in your local computer (on Jupyter Notebook) or you can run on Google Colaboratory:
```text
flask==2.1.2
matplotlib==
zipfile==3.10.5
tensorflow==2.8.0
numpy==1.22.3
Pillow==9.0.1
protobuf<=3.20.0
gunicorn==20.1.0
```

For using our project you must clone this machine learning project at first, this below the link:
`git clone https://github.com/Bangkit-Capstone-C22-PS085/kalpataru-waste-classification.git`
after you clone you can use our machine learning project. Then you can use our main machine learning file
`waste_classification.ipynb` our has a several model, you can choose model dependent on your need, you can check on `/api-services-model/model_ml/` `trash-classification.h5` and `trash_exception.h5`.

## Dataset and Additional Dataset
Dataset : [https://github.com/garythung/trashnet](https://github.com/garythung/trashnet)
<br>
Additional dataset Google Drive : [https://drive.google.com/drive/folders/1d0CX9xGEwKoTrGSHxyTOcei2dbr3w3NL?usp=sharing](https://drive.google.com/drive/folders/1d0CX9xGEwKoTrGSHxyTOcei2dbr3w3NL?usp=sharing)