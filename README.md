# How to get this party started

There's two methods to run this (native or in k8s), neither has any particular advantage, but running native will get you going quicker. I did the kubernetes parts mainly for the purpose of showing that I know how it works.

## Running native

before you do anything, install the python requirements with `pip install -r requirements.txt`, then run `app/models.py` to generate the DB (this will gen in your current directory), and `app/app.py` to get the webserver running.

## Running in kubernetes
#### Optionally push to dockerhub if you're not using the defualt app
If you've modified the app and want to use the modified container, build the image with docker-compose:
`docker-compose build`

Then push the image to the docker hub registry after tagging it:
`docker tag api-exercise_api_excercise <your-repo>/api-exercise:latest`
`docker push <your-repo>/api-exercise:latest`
Change `k8s/deployment.yaml` to reflect your repo instead of pulling from the one used in this project
### Get it all inside kubernetes
Deploy by running:
`kubectl create -f k8s/*`

Pow, it's all running. If you're running minikube like me where networking is not exactly like a proper cluster, you can easily get the address like so:
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
*Update a person*
```
~/git/API-Exercise >>> curl -X PUT -H "Content-Type: application/json" \                                                                                                                                                                                     -d '{ "survived": false, "passengerClass": 3, "name": "Mr. Tom Bombadil", "sex": "male", "age": 99, "siblingsOrSpousesAboard": 2, "parentsOrChildrenAboard":0, "fare":00.0}' \
 http://192.168.99.100:31578/people/{uuid}
```
