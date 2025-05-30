# 🧪 Game Review Tracker – Test Automation Suite

A portfolio-ready project that demonstrates full-stack test automation for a RESTful web service. Built using Python, Pytest, Requests, and Selenium, this suite covers end-to-end API and UI testing, complete with CI/CD integration via GitHub Actions.

---

## 📌 Project Overview

The Game Review Tracker is a mock application designed to track games and user-submitted reviews. This repository contains automated tests for both the API and UI layers, showcasing best practices in test case design, negative testing, and continuous integration.

---

## ✅ Features

- 🔹 **API Testing** using `pytest` + `requests`
- 🔹 **UI Testing** using `Selenium` WebDriver
- 🔹 **Mock API** powered by `json-server`
- 🔹 **Edge Case Coverage** for invalid data and failed requests
- 🔹 **CI Pipeline** using GitHub Actions (runs tests on every push)
- 🔹 **Modular Test Structure** for easy maintenance and scalability

---

## 🛠 Tech Stack

| Layer         | Tools/Frameworks                   |
|--------------|------------------------------------|
| Language      | Python 3.11+                       |
| API Testing   | `requests`, `pytest`               |
| UI Testing    | `selenium`                         |
| Mock API      | `json-server`                      |
| CI/CD         | GitHub Actions                     |
| Versioning    | Git, GitHub                        |
| Optional      | AWS Lambda (future deployment)     |

---

## 🚀 Getting Started

-- STEP-BY-STEP INSTRUCTIONS TO RUN LOCALLY --

### 📦 Prerequisites

Make sure you have the following installed:

- Python 3.10+ (`python3 --version`)
- Node.js + npm (`node -v`, `npm -v`)
- `json-server` installed globally  
  Install with:
  ```bash
  npm install -g json-server

## 🛠 Installation & Setup
### 1. Clone the repository

git clone https://github.com/nate-whitham18/game-review-tester.git
cd game-review-tester

### 2. Create a Python virtual environment

python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

### 3. Install Python dependencies

pip install -r requirements.txt

### 4. Start the Mock API server

json-server --watch mock-api/db.json --port 3001

Your API will be available at:
http://localhost:3001/games
http://localhost:3001/reviews

## 🧪 Running the Tests
### 5. Run API tests

pytest api_tests/ -v
(Optional) Run UI tests

Ensure the HTML page or frontend app is accessible locally, then run:
pytest ui_tests/ -v

## ⚙️ Continuous Integration
This project uses GitHub Actions to run tests automatically on every push to the main branch.

## 📁 Project Structure
game-review-tester/
├── api_tests/               # API test cases (pytest)
│   └── test_games_api.py
├── ui_tests/                # UI test cases (selenium)
│   └── test_ui_form.py
├── mock-api/                # JSON Server mock API
│   └── db.json
├── .github/workflows/       # GitHub Actions config
│   └── tests.yml
├── requirements.txt
├── README.md
└── test_plan.md             # (Optional) Manual test cases or planning notes

## 📌 Portfolio Value
This project highlights:

Strong test design for APIs and UI flows

Python automation across layers

Real-world CI pipeline experience

Use of Selenium, Pytest, GitHub Actions, JSON Server

It’s designed to reflect skills required for modern SDET roles

## 🧠 Future Improvements
Deploy mock API via AWS Lambda (serverless demo)

Add Postman collection for manual API testing

Expand UI tests to include cross-browser testing (BrowserStack/Selenium Grid)

👤 Author
Nate Whitham

