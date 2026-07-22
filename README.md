# Flask Two-Tier DevOps Platform

A production-oriented two-tier web application demonstrating modern DevOps practices using Flask, MySQL, Docker, Jenkins, and AWS.

---

## Project Overview

This project demonstrates how to build, containerize, deploy, and automate a Flask-based web application using industry-standard DevOps tools.

The application consists of two services:

- Flask Web Application
- MySQL Database

Both services are deployed as Docker containers using Docker Compose on an AWS EC2 instance. Jenkins automates the CI/CD pipeline by building and deploying the application whenever new changes are pushed to GitHub.

This repository is continuously enhanced with production-grade DevOps practices including Infrastructure as Code, Kubernetes, GitOps, Security, and Observability.

---

## Architecture

```
Developer
      │
      ▼
 GitHub Repository
      │
      ▼
 Jenkins Pipeline
      │
      ▼
Docker Build
      │
      ▼
Docker Compose
      │
      ▼
AWS EC2
 ├── Flask Container
 └── MySQL Container
```

---

## Technology Stack

### Programming

- Python
- Flask

### Database

- MySQL

### Containerization

- Docker
- Docker Compose

### CI/CD

- Jenkins

### Cloud

- AWS EC2

### Version Control

- Git
- GitHub

### Operating System

- Ubuntu Linux

---

## Features

- Flask Web Application
- MySQL Integration
- Dockerized Application
- Multi-container Deployment
- Jenkins CI/CD Pipeline
- AWS Deployment

---

## Project Structure

```
.
├── app.py
├── Dockerfile
├── Jenkinsfile
├── docker-compose.yml
├── templates/
├── diagrams/
├── PROJECT_REPORT.md
└── README.md
```

---

## Future Enhancements

- GitHub Actions
- SonarQube
- Trivy
- Amazon ECR
- Terraform
- Amazon EKS
- Argo CD
- Prometheus
- Grafana
- Loki
- OpenTelemetry

---

## Learning Objectives

This project demonstrates practical experience with:

- CI/CD
- Containerization
- Cloud Deployment
- DevOps Automation
- Infrastructure Design
- Production Deployment

---

## Author

Kishore Billu

Cloud | DevOps | Platform | AI Engineeringyolo
