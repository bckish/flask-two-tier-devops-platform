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

For a database-backed local run without Docker or cloud resources:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirement.txt pytest
DB_DRIVER=sqlite .venv/bin/python app.py
# In another terminal:
.venv/bin/python -m pytest -q
```

Open http://127.0.0.1:5000. SQLite is a local-only alternative; Compose still uses MySQL.

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

## Verified local Kubernetes results

Test date: 25 November 2026. Environment: Docker Desktop on Apple Silicon, Kind v0.30.0, Kubernetes v1.34.3. Local images were imported into the isolated cluster; no images were pushed to a registry and no paid cloud resources were created.

Tested code: `131d125` (merged main). The actual Flask Docker build and MySQL 8.4 were deployed into Kind; both pods became Ready. MySQL used a bound 1 GiB local PVC. The Flask health endpoint, message submission and retrieval passed, and a direct SQL count confirmed the inserted test row.

```bash
docker build -t bckish-local/flask:runtime .
docker pull mysql:8.4
kind load docker-image --name YOUR_LOCAL_KIND bckish-local/flask:runtime mysql:8.4
kubectl --kubeconfig /path/to/local-kind.kubeconfig create namespace flask-local
kubectl --kubeconfig /path/to/local-kind.kubeconfig apply -f local-k8s/app.yaml
kubectl --kubeconfig /path/to/local-kind.kubeconfig -n flask-local port-forward --address 127.0.0.1 service/flask 25000:5000
```

The [local fixture](local-k8s/app.yaml) uses synthetic test-only database values; do not reuse them outside a disposable local cluster. The initial app restart during MySQL initialization recovered successfully. AWS EC2 and Jenkins delivery were not deployed or verified.

## Dependency maintenance (26 November 2026)

The existing dependency set passed local Python tests with deprecation warnings treated as errors; Docker Compose configuration also validated. No forced dependency upgrade was necessary. CI now runs `python -m pytest -q -W error::DeprecationWarning` to prevent regressions.

The follow-up Compose test exposed a startup race with MySQL's temporary initialization server. The readiness check now verifies an authenticated `SELECT 1` over TCP against the actual application database. Two subsequent fresh local database runs passed Flask health, message creation and retrieval with Python deprecations treated as errors.
