# aws-ecs-devops-platform

> Production Flask REST API deployed on AWS ECS Fargate with automated CI/CD pipeline.

## What this project does
A Task Manager REST API containerized with Docker, deployed on AWS using Terraform IaC, with automated GitHub Actions CI/CD pipeline and Prometheus/Grafana monitoring.

## Architecture
GitHub push → GitHub Actions → Docker build → ECR → ECS Fargate

↑

Terraform provisions → VPC → ALB → ECS → RDS MySQL

↓

CloudWatch + Prometheus + Grafana

## Tech Stack
| Layer | Tools |
|-------|-------|
| App | Python, Flask |
| Container | Docker, Amazon ECR |
| Cloud | AWS ECS Fargate, RDS, ALB, VPC |
| IaC | Terraform (modular) |
| CI/CD | GitHub Actions |
| Config | Ansible |
| Monitoring | Prometheus, Grafana, CloudWatch |
| K8s | Kubernetes manifests |

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Run locally
```bash
docker-compose up --build
curl http://localhost:5000/health
```

## Run tests
```bash
cd app && pytest tests/ -v
```

## Deploy to AWS
```bash
cd infra
terraform init
terraform apply -auto-approve
# destroy after testing!
terraform destroy -auto-approve
```

## Key features
- ✅ Multi-stage Docker build
- ✅ Terraform modular IaC (6 modules)
- ✅ GitHub Actions CI/CD (test → build → deploy)
- ✅ ECS Fargate (serverless containers)
- ✅ Private subnets + least privilege IAM
- ✅ CloudWatch alarms + SNS email alerts
- ✅ Prometheus + Grafana monitoring
- ✅ Ansible server hardening playbooks
- ✅ Kubernetes manifests ready

## Author
**Rohan Rajesh** — DevOps Engineer
LinkedIn: [rohan-r-37077b216](https://linkedin.com/in/rohan-r-37077b216)
GitHub: [rohan-rajesh94](https://github.com/rohan-rajesh94)