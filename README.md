# How to get this party started

## Create the image (optional)
Build the image with docker-compose:
`docker-compose build`

Push the image to the docker hub registry after tagging it:
`docker tag api-exercise_api_excercise lsdneels/api-exercise:latest`
`docker push lsdneels/api-exercise:latest`

## Deploy to kubernetes

Deploy that little container to kubernetes:
`kubectl create -f k8s/*`

Pow, it's all running. If you're running minikube, you can easily get the address like so:
```
user@host : minikube service list
|--------------|----------------------|-----------------------------|
|  NAMESPACE   |         NAME         |             URL             |
|--------------|----------------------|-----------------------------|
| api-exercise | api-exercise         | http://192.168.99.100:31578 |
| default      | kubernetes           | No node port                |
| kube-system  | kube-dns             | No node port                |
| kube-system  | kubernetes-dashboard | No node port                |
|--------------|----------------------|-----------------------------|
```

An example of the type of curl request this things will do:


*Get everyone*
```
curl -X GET -H "Content-Type: application/json"  http://localhost:8080/people
```
*Get a specific person*
```
curl -X GET -H "Content-Type: application/json"  http://localhost:8080/people/{uuid}
```
*Create a person*
```
curl -X POST -H "Content-Type: application/json" \                                                                                                                                                                                     
 -d '{ "survived": true, "passengerClass": 3, "name": "Mr. Tom Bombadil", "sex": "male", "age": 100, "siblingsOrSpousesAboard": 0, "parentsOrChildrenAboard": 0, "fare": 00.0}' \
 http://192.168.99.100:31578/people
```
*Delete a person*
```
curl -X DELETE -H "Content-Type: application/json"  http://localhost:8080/people/{uuid}
```
*Update a persnon*
```
~/git/API-Exercise >>> curl -X PUT -H "Content-Type: application/json" \                                                                                                                                                                                     -d '{ "survived": false, "passengerClass": 3, "name": "Mr. Tom Bombadil", "sex": "male", "age": 99, "siblingsOrSpousesAboard": 2, "parentsOrChildrenAboard":0, "fare":00.0}' \
 http://localhost:8080/people/{uuid}
```
---

# API-exercise

This exercise is to assess your technical proficiency with Software Engineering, DevOps and Infrastructure tasks.
There is no need to do all the exercises, but try to get as much done as you can, so we can get a good feel of your skillset.  Don't be afraid to step outside your comfort-zone and try something new.

If you have any questions, feel free to reach out to us.

## Exercise

This exercise is split in several subtasks. We are curious to see where you feel most comfortable and where you struggle.

### 0. Fork this repository
All your changes should be made in a **private** fork of this repository. When you're done please, please:
* Share your fork with the **container-solutions-test** user (Settings -> Members -> Share with Member)
* Make sure that you grant this user the Reporter role, so that our reviewers can check out the code using Git.
* Reply to the email that asked you to do this API exercise, with a link to the repository that the **container-solutions-test** user now should have access to.

### 1. Setup & fill database
In the root of this project you'll find a csv-file with passenger data from the Titanic. Create a database and fill it with the given data. SQL or NoSQL is your choice.

### 2. Create an API
Create an HTTP-API (e.g. REST) that allows reading & writing (maybe even updating & deleting) data from your database.
Tech stack and language are your choice. The API we would like you to implement is described in [API.md](./API.md)

### 3. Dockerize
Automate setup of your database & API with Docker, so it can be run everywhere comfortably with one or two commands.
The following build tools are acceptable:
 * docker
 * docker-compose
 * groovy
 * minikube (see 4.)

No elaborate makefiles please.

#### Hints

- [Docker Install](https://www.docker.com/get-started)

### 4. Deploy to Kubernetes
Enable your Docker containers to be deployed on a Kubernetes cluster.

#### Hints

- Don't have a Kubernetes cluster to test against?
  - [MiniKube](https://kubernetes.io/docs/setup/minikube/) (free, local)
  - [GKE](https://cloud.google.com/kubernetes-engine/) (more realistic deployment, may cost something)

### 5. Whatever you can think of
Do you have more ideas to optimize your workflow or automate deployment? Feel free to go wild and dazzle us with your solutions.
