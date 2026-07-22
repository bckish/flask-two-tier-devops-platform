# Flask Two-Tier DevOps Platform

## Technical Project Report

Author: Kishore Billu

---

# 1. Introduction

This project demonstrates the implementation of a production-style two-tier web application using Flask and MySQL deployed on AWS.

The objective is to automate the complete software delivery lifecycle using Docker and Jenkins while following DevOps best practices.

---

# 2. Objectives

The primary objectives of this project are:

- Deploy a Flask application
- Configure a MySQL database
- Containerize the application
- Implement Docker Compose
- Configure Jenkins CI/CD
- Deploy automatically on AWS EC2
- Build a reusable DevOps deployment workflow

---

# 3. Technology Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Framework | Flask |
| Database | MySQL |
| Container | Docker |
| Orchestration | Docker Compose |
| CI/CD | Jenkins |
| Cloud | AWS EC2 |
| Version Control | GitHub |
| OS | Ubuntu Linux |

---

# 4. System Architecture

(Add your architecture diagram here.)

---

# 5. Project Workflow

Developer

↓

GitHub Push

↓

Jenkins Trigger

↓

Clone Repository

↓

Build Docker Image

↓

Docker Compose Deployment

↓

Flask + MySQL Containers

↓

Application Available

---

# 6. AWS Infrastructure

## EC2

Ubuntu 22.04 LTS

Instance Type

t2.micro

Security Groups

- SSH (22)
- HTTP (80)
- Flask (5000)
- Jenkins (8080)

---

# 7. Docker Configuration

Explain:

- Dockerfile
- Base Image
- Dependencies
- Working Directory
- Build Process
- Runtime

---

# 8. Docker Compose

Explain:

- Flask Service
- MySQL Service
- Network
- Volumes
- Health Checks

---

# 9. Jenkins Pipeline

Pipeline stages include:

1. Clone Source Code
2. Build Docker Image
3. Deploy Containers
4. Verify Deployment

Future stages:

- Unit Testing
- Security Scan
- Image Push
- Kubernetes Deployment

---

# 10. Deployment Process

1. Push code to GitHub
2. Jenkins detects changes
3. Repository cloned
4. Docker image built
5. Existing containers stopped
6. New containers started
7. Application becomes available

---

# 11. Validation

Verify:

- Jenkins Build Success
- Docker Containers Running
- Flask Application Accessible
- MySQL Connectivity
- Application Logs

Commands

docker ps

docker logs

docker compose ps

systemctl status jenkins

---

# 12. Challenges

Examples:

- Docker networking
- Jenkins permissions
- MySQL startup timing
- Container communication
- Environment variables

---

# 13. Lessons Learned

This project provided practical experience in:

- Docker
- Jenkins
- AWS
- CI/CD
- Linux
- Production Deployment

---

# 14. Future Improvements

- GitHub Actions
- SonarQube
- Trivy
- Terraform
- Amazon ECR
- Amazon EKS
- Argo CD
- Prometheus
- Grafana
- Loki
- OpenTelemetry
- GitOps
- Blue/Green Deployment

---

# 15. Conclusion

This project demonstrates the end-to-end implementation of a containerized Flask application deployed on AWS using Docker and Jenkins.

It serves as the foundation for building a production-ready cloud-native DevOps platform that will continue to evolve with Infrastructure as Code, Kubernetes, GitOps, security, and observability.