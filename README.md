## Foreword

This was done as an exercise to gauge my own skills with the tools involved. It's unprofessional and inefficient.

# How to get this party started

## Running manually (you savage)

First run `app/models.py` to generate the DB, then run `app/app.py` to get the webserver running

## Deploy to kubernetes (optional)
# Create the image (can just pull the image too y'know)
Build the image with docker-compose:
`docker-compose build`

Push the image to the docker hub registry after tagging it:
`docker tag api-exercise_api_excercise lsdneels/api-exercise:latest`
`docker push lsdneels/api-exercise:latest`

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


## Example API Calls

*Get everyone*
```
curl -X GET -H "Content-Type: application/json"  http://192.168.99.100:31578/people
```
*Get a specific person*
```
curl -X GET -H "Content-Type: application/json"  http://192.168.99.100:31578/people/{uuid}
```
*Create a person*
```
curl -X POST -H "Content-Type: application/json" \                                                                                                                                                                                     
 -d '{ "survived": true, "passengerClass": 3, "name": "Mr. Tom Bombadil", "sex": "male", "age": 100, "siblingsOrSpousesAboard": 0, "parentsOrChildrenAboard": 0, "fare": 00.0}' \
 http://192.168.99.100:31578/people
```
*Delete a person*
```
curl -X DELETE -H "Content-Type: application/json"  http://192.168.99.100:31578/people/{uuid}
```
*Update a persnon*
```
~/git/API-Exercise >>> curl -X PUT -H "Content-Type: application/json" \                                                                                                                                                                                     -d '{ "survived": false, "passengerClass": 3, "name": "Mr. Tom Bombadil", "sex": "male", "age": 99, "siblingsOrSpousesAboard": 2, "parentsOrChildrenAboard":0, "fare":00.0}' \
 http://192.168.99.100:31578/people/{uuid}
```
