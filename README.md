````md
# DevSecOps CI/CD Pipeline

Hands-on DevOps/DevSecOps learning project built with **GitHub Actions and AWS**.

The project started as an experiment with a **self-hosted EC2 GitHub Actions runner using an IAM instance profile**, and was later expanded to explore modern CI/CD security practices.

## Pipeline

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ├── Gitleaks
   │     └── Secret scanning
   │
   ├── SonarQube
   │     └── Code quality & security analysis
   │
   └── pip-audit
         └── Dependency vulnerability scanning
   │
   ▼
Security Checks Passed
   │
   ▼
Docker Build
   │
   ▼
Trivy
   └── Container vulnerability scanning
   │
   ▼
GitHub OIDC
   │
   ▼
AWS IAM Role
   │
   ▼
Amazon ECR
   │
   ▼
Docker Image Push
````

## What I Learned

* GitHub Actions CI/CD workflows
* Self-hosted GitHub Actions runners on EC2
* AWS IAM instance profiles
* GitHub Actions → AWS authentication using **OIDC**
* Eliminating long-lived AWS access keys from CI/CD
* Gitleaks secret scanning
* SonarQube/SonarCloud static analysis and quality gates
* Python dependency vulnerability scanning with `pip-audit`
* Docker image security scanning with Trivy
* Security gates that prevent vulnerable artifacts from progressing
* Docker base-image vulnerabilities and remediation
* Amazon ECR image publishing
* Immutable image tagging using Git commit SHA


## AWS Authentication

The final pipeline uses GitHub Actions OIDC instead of storing AWS access keys:

```text
GitHub Actions
      │
      │ OIDC
      ▼
AWS IAM Role
      │
      ▼
Temporary Credentials
      │
      ▼
Amazon ECR
```

## **

Personal hands-on **DevOps/DevSecOps learning project** focused on understanding how security controls can be integrated into a CI/CD pipeline.



