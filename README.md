# Airflow Cluster Setup

This guide will walk you through the steps to set up a Kubernetes cluster with Airflow, including building and loading Docker images, creating secrets, and installing Airflow.

## Prerequisites

- **Kind**: Kubernetes IN Docker (https://kind.sigs.k8s.io/)
- **Docker**: To build and manage container images
- **Kubectl**: Kubernetes command-line tool
- **Helm**: Kubernetes package manager
- **Values.yaml**: Your Helm chart configuration file
- **SSH Key**: For accessing the main repository

## Setup Instructions

### 1. Create the Kubernetes Cluster

Create a new Kubernetes cluster using Kind with the provided configuration file:

```bash
kind create cluster --config kind-cluster.yaml
