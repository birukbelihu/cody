![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/Cody)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/Cody)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/Cody)
![GitHub license](https://img.shields.io/github/license/BirukBelihu/Cody)

# 🧠 Cody - Online Code Compiler API

**Cody** is a lightweight, Docker-based online code compiler backend built with **Flask**. It safely executes code (Python & JavaScript For now) inside isolated docker containers and returns output or errors via a simple HTTP API.

---

## 🚀 Features

- 🔒 Sandboxed execution with Docker
- ✅ Supports Python and JavaScript(Probably more languages support soon)
- 🌐 REST API built using Flask
- 🐳 Per-language isolated Docker images
- 💻 Easy to run locally

---

## 🛠️ Prerequisites

Make sure you have the following installed:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)

---

## 🔧 Getting Started

### Clone the repository

```bash
git clone https://github.com/BirukBelihu/Cody.git
```


### Go inside the project

```bash
cd Cody
```

### Set up Python virtual environment(I recommend using [uv](https://github.com/astral-sh/uv) for lightning speed)

### With uv

```bash
uv venv .venv
```

### With Python

```bash
python -m venv .venv
```

# Activate virtual environment

```bash
.venv\Scripts\activate # On Windows
```

```bash
source .venv/bin/activate # On Linux, WSL & macOS
```

# Install required dependencies

### With uv

```bash
uv pip install -r requirements.txt
```

### With Python

```bash
pip install -r requirements.txt
```

---

## 🐳 Build Language Docker Images

Before running Cody, build the Docker images:

```bash
# On Windows CMD
build_images.bat
```

```bash
# On WSL/Linux/macOS
./build_images.sh
```

---

## ▶️ Start Cody

```bash
python main.py
```

Visit: `http://localhost:5000/api/v1/cody`

---

## 🧪 Example Usage(Python)

```bash
curl -X POST http://localhost:5000/api/v1/cody \
  -H "Content-Type: application/json" \
  -d '{"language": "python", "code": "print(\"Hello, Cody!\")"}'
```

## 🧪 Example Usage(JavaScript)

```bash
curl -X POST http://localhost:5000/api/v1/cody \
  -H "Content-Type: application/json" \
  -d '{"language": "javascript", "code": "console.log(\"Hello, Cody!\")"}'
```

---

## 📂 Project Structure

```plaintext
Cody/
├── app/
│   ├── code_runner.py
│   └── language_config.py
├── images/
│   ├── javascript/Dockerfile
│   └── python/Dockerfile
├── scripts/
│   ├── build_images.bat
│   └── build_images.sh
├── templates/
│   ├── images/cody.png
│   └── index.html
│   └── index.js
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
```

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for full details.
