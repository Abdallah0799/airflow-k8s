# Airflow Cluster Setup

This guide will walk you through the steps to set up a Kubernetes cluster with Airflow, including building and loading Docker images, creating secrets, and installing Airflow.

## Prerequisites

- **Kind**: Kubernetes IN Docker (https://kind.sigs.k8s.io/)
- **Docker**: To build and manage container images
- **Kubectl**: Kubernetes command-line tool
- **Helm**: Kubernetes package manager
- **Values.yaml**: Your Helm chart configuration file
- **SSH Key**: For accessing the main repository
- **Environment variables**: You need to fill manually environment variables in the values.yaml

## Setup Instructions

### 1. Create the Kubernetes Cluster

Create a new Kubernetes cluster using Kind with the provided configuration file:

```bash
kind create cluster --config kind-cluster.yaml
```
### 2. Build and Load the Docker Image

Build the Docker image and load it into the Kind cluster:

```bash
docker build --pull --tag my-airflow:1.0.0 .
kind load docker-image my-airflow:1.0.0
```
### 3. Create an SSH Secret

Create a Kubernetes secret for the SSH key used to access the main repository. Replace path/to/ssh-key with the actual path to your SSH key file:

```bash
kubectl create secret generic airflow-ssh-secret --from-file=path/to/ssh-key
```

### 4. Create a namespace

Create a namespace in Kubernetes for the Airflow deployment:

```bash
kubectl create namespace my-namespace
```


### 5. Install Airflow

Use Helm to install the Airflow chart into the created namespace. Make sure to use your own values.yaml file if necessary:

```bash
helm install first-release apache-airflow/airflow -f values.yaml --namespace my-namespace
```

### 6. Access the Airflow Web Server

Port-forward the Airflow web server service to your local machine so you can access the Airflow UI:
```bash
kubectl port-forward svc/first-release-webserver 8080:8080 --namespace my-namespace
```
You can now access the Airflow web server at [http://localhost:8080](http://localhost:8080) and view the DAGs from the main repository.


