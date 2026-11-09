# Kubernetes Full Stack Application

## Project Description

This project demonstrates deploying a full-stack
application using Flask, Express.js, Docker,
Kubernetes and Minikube.

## Technologies Used

- Python
- Flask
- Node.js
- Express.js
- Docker
- Kubernetes
- Minikube
- kubectl

## Application Architecture

The application consists of:

1. Flask Frontend
2. Express Backend
3. Kubernetes Deployments
4. Kubernetes Services

## Frontend

Flask frontend runs on port 5000.

## Backend

Express backend runs on port 5001.

## Kubernetes Services

Frontend: NodePort 30080

Backend: ClusterIP 5001

## Deployment

Start Minikube:

minikube start --driver=docker

Build images:

minikube image build -t flask-frontend:v1 ./frontend

minikube image build -t express-backend:v1 ./backend

Apply Kubernetes files:

kubectl apply -f kubernetes/

Check pods:

kubectl get pods

Check services:

kubectl get services

Access frontend:

minikube service frontend-service