# FastAPI Trade Order Service

A lightweight backend service built with **FastAPI** that accepts trade order details via a REST API, stores them in an **SQLite** database, and provides endpoints for creating and retrieving orders. The service is containerized using **Docker** and deployed to an **AWS EC2** instance, with a **CI/CD pipeline** powered by **GitHub Actions**.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Local Setup](#local-setup)
  - [Running with Docker](#running-with-docker)
- [API Endpoints](#api-endpoints)
- [Deployment on AWS EC2](#deployment-on-aws-ec2)
- [CI/CD Pipeline](#cicd-pipeline)
- [Tech Stack](#tech-stack)
- [License](#license)

---

## Project Overview

This project implements a simple trading order service with the following core features:
- **POST /orders**: Accept trade orders with fields like symbol, price, quantity, and order type (buy/sell).
- **GET /orders**: Retrieve all submitted trade orders.
- **GET /**: A health-check endpoint.

Built with **FastAPI** for fast development and interactive documentation (Swagger/OpenAPI), and using **SQLite** for lightweight data persistence.

---

## Project Structure

```
trade-order-service/
├── app/
│   ├── __init__.py
│   ├── main.py             # FastAPI app entry point
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic request/response models
│   ├── database.py         # Database setup
│   └── routers/
│       ├── __init__.py
│       └── orders.py       # /orders API routes
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions workflow
└── README.md
```

---

## Features

- ✅ REST API to create and retrieve trade orders  
- ✅ SQLite database integration via SQLAlchemy  
- ✅ Interactive API docs at `/docs`  
- ✅ Dockerized for consistent deployment  
- ✅ Deployed on AWS EC2  
- ✅ CI/CD pipeline with GitHub Actions  

---

## Getting Started

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/trade-order-service.git
   cd trade-order-service
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API docs:**
   Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t trade-order-service:latest .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --name trade_service trade-order-service:latest
   ```

3. **Open the docs:**
   Visit [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoints

- **GET /**  
  _Health-check endpoint_  
  Response:
  ```json
  { "message": "Hello, World!" }
  ```

- **POST /orders**  
  _Create a new trade order_  
  Example Request:
  ```json
  {
    "symbol": "AAPL",
    "price": 150.0,
    "quantity": 10,
    "order_type": "buy"
  }
  ```
  Example Response:
  ```json
  {
    "symbol": "AAPL",
    "price": 150.0,
    "quantity": 10,
    "order_type": "buy",
    "id": 1
  }
  ```

- **GET /orders**  
  _Retrieve all orders_  
  Example Response:
  ```json
  [
    {
      "symbol": "AAPL",
      "price": 150.0,
      "quantity": 10,
      "order_type": "buy",
      "id": 1
    }
  ]
  ```

---

## Deployment on AWS EC2

1. **Launch EC2 Instance** (Ubuntu)
   - Open ports 22 (SSH) and 8000 in security group

2. **SSH into the instance:**
   ```bash
   ssh -i /path/to/key.pem ubuntu@<EC2-IP>
   ```

3. **Install Docker:**
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

4. **Deploy the container:**
   ```bash
   docker pull your-dockerhub-username/trade-order-service:latest
   docker run -d -p 8000:8000 --name trade_service trade-order-service:latest
   ```

---

## CI/CD Pipeline

A GitHub Actions workflow automatically:
- Runs tests on pull requests
- Builds and pushes Docker images to Docker Hub
- SSHs into EC2 and redeploys the updated container

### Required GitHub Secrets

- `EC2_HOST`: EC2 public IP or DNS  
- `EC2_USER`: Typically `ubuntu`  
- `EC2_SSH_KEY`: Your EC2 private key  
- `DOCKERHUB_USERNAME` & `DOCKERHUB_PASSWORD`: Docker Hub credentials  

---

## Tech Stack

- **FastAPI** – web framework  
- **SQLite** – lightweight database  
- **SQLAlchemy** – ORM for Python  
- **Docker** – containerization  
- **GitHub Actions** – CI/CD pipeline  
- **AWS EC2** – cloud deployment  

---

## License

This project is licensed under the [MIT License](LICENSE).

