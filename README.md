# Star Wars API

![Star Wars Logo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F6%2F6c%2FStar_Wars_Logo.svg%2F2560px-Star_Wars_Logo.svg.png&f=1&nofb=1&ipt=fe0de95c2f1c74544dd8657457218743f2e01e96abd9dd86cef04e5e9b89c1b2&ipo=images)

In this project we will find a python code that will allow us to interact with the [Star Wars API](https://swapi.dev/) so we can see data releted to our favourites characters from the franchise.


## Code

The code is allocated in **__starwars__** folder where we can find the next different files: 

#### main.py

This is the main code of the application. This files creates an api with an unique endpoint which will collect, fetch and show the data of all the characters of star wars that are stored in the Star Wars API /people endpoint.
In order to create this api it was necessary to use different modules and libraries. The ones used here were **__FastAPI__**, **__Requests__**, **__HTTPException__**, **__logging__** and **__time__**
FastAPI was selected because is one of the easiest frameworks to build an API in python, it is simple and it fits perfectly for the porpuse of the project. Requests is other library which makes HTTP request and returns a complete object with a lot of information aboute the HTTP response.
HTTPException is used to control the responses of the HTTP requests to the Star Wars API, it provides control about the exceptions and it´s used to show messages to the user in case something goes wrong during the communication of the application and the SW API.
Logging is used to create records of each action that application does, so it shows in the regular standar output what the applications is doing. And finally, time is used to create a time interval during the flow test, doing this we ensure that Star Wars API has enought time to reply.

Once we introduced the different modules, les´t explain the code. First of all we configure the loggers as it has to record the different actions that the application does, it needs to be configure at the beginning of the code. We set a basic configuration of the logger just adding the log level at **__INFO__**. After that, we create an object called __app__ which is an instance of the FastAPI, this object will be the application.
Then we use FastAPI framework to add a HTTP Get method for our application with the path "/fetch" and we have to define an action for this function. In the function will find a loop that will iterate to call Star Wars API using the counter of the loop as index of the request. A flow control check if the response of the API is valid or not, in case is not valid, the loop is broken and an exception is triggerd. Each valid response is stored in a variable and once we have all the data of every character available in the API, which means that the API returned a response with http status equal to 404, the process is done and the results are sorted by name before being shown.

#### test.py

This file can be use to generate traffic to the application. This is a quite simple code, it just has a loop with a counter with the goal of make HTTP request to the application. Before running this file, we need to run the main.py first to the application is running.

#### requirements.txt

This file contains the list of the modules and libraries and the versions used in the project. It will be used when the docker image of the application is buildt.

## Docker

In the root of the repository we can find Dockerfile and Dcoker Compose file to use with the aplication. The Dockerfile will create a docker image which runs the application in the port 8000.

## Kubernetes

In subfolder **__kubernetes starwars__** we can find the files related to kubernetes. 

### deployment.yaml

This file creates a kubernetes deployment using the docker image of the python application.

### service.yaml

This file creates a kubernetes service resource which maps traffict to python application using port 80.

### hpa.yaml

This file creates a horizontal pod autoscaler for the kubernetes deployment running the python application. The HTP increases the number of replicas of the pod
running the application once it matches the properties described in the file, in this case, once it reaches a high level of cpu or memory usage, a new replica
is created.


This a summary of the Star Wars APi python project!!