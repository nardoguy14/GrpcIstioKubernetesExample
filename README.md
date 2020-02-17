# About

This working example will deploy two versions of a GRPC service to Minikube, a single local Node instance of Kubernetes.
Istio will be setup to handle L7 load balancing across the two versions and to visualize our services.

# Setup Working Environment

## Download Docker

`https://hub.docker.com`

## Download Minikube
(a single node instance of Kubernetes)

`https://kubernetes.io/docs/tasks/tools/install-minikube/#before-you-begin`

## Download Istio

`https://istio.io/docs/setup/getting-started/#platform`

## Setup Service Graph

`https://istio.io/docs/tasks/observability/kiali/`

# Setup Code

## Download protoc for Grpc

`pip install grpcio-tools`

# Generate GRPC Stubs and Service Code

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. auth_service.proto`

# Generate Containers

We need to build the containers for Minikube to use within its own
docker instance so first we get setup up for that environment.

`eval $(minikube docker-env)`

Now we build the containers.

`docker build -t auth_service:v1-f Dockerfile .`

Now we change `authorization_server.py` code to print out different return value of v2.

We will rebuild a second version of the container.

`docker build -t auth_service:v2 -f Dockerfile .`

# Deploy to Kubernetes Minikube

First we will handle the deployment of the grpc instances and service which points to both.

`kubectl apply -f auth_service.yaml`

Next we will amke the service reachable outside the cluster.

`kuberctl apply -f auth_service_gateway.yaml`

You will need to find out the ingress host and port that is reachable.

`https://istio.io/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports`

`export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT`

# Call Services

First find out your host and port.

`echo $GATEWAY_URL`

Use this value in `grpc_service_caller.py` to call the service in

`channel = grpc.insecure_channel('<REPLACE ME PLEASE>')`

Visit the Kiali dashboard to see logs, traffic, and more.