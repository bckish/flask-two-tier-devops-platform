# Flask Two-Tier DevOps Platform

A two-tier DevOps learning application demonstrating modern DevOps practices using Flask, MySQL, Docker, Jenkins, and AWS.

---

## Project Overview

This project demonstrates how to build, containerize, deploy, and automate a Flask-based web application using industry-standard DevOps tools.

The application consists of two services:

- Flask Web Application
- MySQL Database

Both services can run locally via Docker Compose or on an approved AWS EC2 host. Jenkins defines a build and Compose deployment pipeline; cloud deployment is not verified here.

Infrastructure as Code, GitOps, security and observability are future enhancements, not implemented production claims.

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

## Local run

```bash
git clone https://github.com/bckish/flask-two-tier-devops-platform.git
cd flask-two-tier-devops-platform
docker compose config
docker compose up --build -d
curl --fail http://localhost:5000/health
docker compose down
```

The Compose configuration is for local practice only; use dedicated credentials and do not expose the database publicly. Run Jenkins on a dedicated lab agent after reviewing its deployment stage. See [PROJECT_REPORT.md](PROJECT_REPORT.md) for project context.

## Attribution

The inherited Jenkinsfile references [prashantgohel321/DevOps-Project-Two-Tier-Flask-App](https://github.com/prashantgohel321/DevOps-Project-Two-Tier-Flask-App.git). Verify upstream redistribution rights before further distribution; no new license is asserted here.

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

Cloud | DevOps | Platform | AI Engineering
