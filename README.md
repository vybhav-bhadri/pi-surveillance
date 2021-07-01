## Pi Survelliance Camera
This is a simple DIY project. IP survelliane camera is implemeted using Rasberry Pi. It rins a flask server which provides live video feed locally and remotely.

## Table of contents
* [Technolgies](#technologies)
* [Setup](#setup)

## Technologies
Project is created using:
* Python 3
* Flask
* HTML,CSS
* Bootstrap 4 

## Pi camera Setup
In this project Pi acts as a IP camera. Before running code, check if pi camera is working.
Open termianl
```
$ sudo raspi-config
```
Selelt Interface, then enable Pi camera and select Finish.
Check that camera is working by running this command in terminal
```
$ raspistill -o image.jpg

```
## Project Setup
Clone the project using the following command
```
$git clone git@github.com:vybhav-bhadri/pi-surveillance.git
```
This project is using openCV which creates camera objects. Install openCV using the folllowing commnads.
```
$sudo apt update
$sudo pip install python3-opencv
```
Navigate to the repository directory
```
$ cd pi-survelliance
```
Install all the dependencies by running this command
```
$pip install -r requirements.txt
```
## Run the Program
Start server
```
$python3 run.py
```
Stream can be viewed by entering localhost:5000 in your browser.You can also access the stream locally by entering ip address of the rasberry pi running the server.
To find the local IP address of your Pi, open terminal and run
```
$ifconfig
```
To access stream remotely, use ngrok to expose a local tunnel. Start the local server and run ngrok with this command,
visit [ngrok](https://ngrok.com/) and check documentation for setup.
```
$./ngrok http 5000
```
This will generate a link and use this link to access stream.

Note : Current implementation is a prototype of a survelliance system. To use this in real world features such as user authentication, admin panel and auto startup of the camera need to be implemented.




