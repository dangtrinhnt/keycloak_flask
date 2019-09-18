# KEYCLOAK FLASK

**keycloak_flask** is an example FLASK app that uses Keycloak for user
registration and OIDC authentication. This project also provides different
ways to run the application such as Docker container on your local machine
or in a Kubernetes cluster with Istio installed.


## Prerequisites

* Have a Keycloak instance up and running and you know the admin user
  credentials
* If you want to deploy the app on a Kubernetes cluster with Istio installed,
  make sure you have admin privileges to the cluster. You also need to install
  **istioctl**

## Run the application normally

1. Clone the repo, install the requirements

```
git clone https://github.com/dangtrinhnt/keycloak_flask
cd keycloak_flask
virtualenv ~/keycloak_flask
source ~/keycloak_flask/bin/activate
pip install -r requirements.txt
```

2. Copy **keycloak_flask/settings.py** to **keycloak_flask/local_settings.py**
and modify the variables with your own values

3. While in the root directory of this repository, run the application

```
export FLASK_APP=keycloak_flask.user
export FLASK_DEBUG=1
export KEYCLOAK_FLASK_SETTINGS=local_settings.py
flask run
```

## Run the application in a Docker container on your local machine

1. Copy **keycloak_flask/settings.py** to **keycloak_flask/local_settings.py**
and modify the variables with your own values

2. Build the Docker image

```
docker image build -t keycloak_flask .
```

3. Run the Docker container

```
docker run -p 5000:5000 -d keycloak_flask
```

## Run the application in a Kubernetes cluster with Istio

1. Deploy the application into the cluster

```
kubectl apply -f <(istioctl kube-inject -f k8s_app_deploy.yaml)
```

2. Because our application will be exposed on port 5000 of the Istio gateway
   which is not opened by default, we need to open it following this
   tutorial https://www.dangtrinh.com/2019/09/how-to-open-custom-port-on-istio.html 

3. Create a new Istio gateway to route traffic to the application

```
kubectl apply -f k8s_istio_gw.yaml
```

4. Access the application through the Istio ingress gateway on port 5000

Find the ingress address:

```
kubectl -n istio-system get service istio-ingressgateway
```
