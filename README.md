![GitHub Repo stars](https://img.shields.io/github/stars/BirukBelihu/Cody)
![GitHub forks](https://img.shields.io/github/forks/BirukBelihu/Cody)
![GitHub issues](https://img.shields.io/github/issues/BirukBelihu/Cody)
![GitHub license](https://img.shields.io/github/license/BirukBelihu/Cody)

# 🧠 Cody - Online Code Compiler API

**Cody** is a lightweight, Docker-based online code compiler backend built with [Flask](https://flask.palletsprojects.com/). It safely executes code (Python & JavaScript For now) inside isolated docker containers and returns output or errors via a simple HTTP API.

---

## 🚀 Features

- 🔒 Sandboxed execution with Docker
- ✅ Supported Languages 
    * Python
    * JavaScript
- 🌐 REST API built using Flask
- 🐳 Per-language isolated Docker images
- 💻 Easy to run locally

---

## 🔧 Getting Started

Make sure you have the following installed:

- [Git](https://git-scm.com/)

```bash
git --version
```

- [Python](https://www.python.org/)

```bash
python --version
```

- [Docker](https://www.docker.com/)

```bash
docker --version
```

---

### Clone the repository

```bash
git clone https://github.com/birukbelihu/cody.git
```

### Go inside the project

```bash
cd cody
```

### Set up Python virtual environment(I recommend using [uv](https://github.com/astral-sh/uv) for lightning speed)

### With uv

```bash
uv venv
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

### Go inside the scripts directory

```bash
cd scripts
```

## 🐳 Build Language Docker Images

> [!NOTE]
> Before building docker images make sure Docker instance is running by typing this command:
>
> ```bash
> docker stats
> ```
>
> If it's running, you will see the list of running containers. otherwise you’ll see an error like this:
>
> ```
> error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.50/containers/json": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
> ```

build the Docker images

```bash
# On Windows CMD
build_images.bat
```

```bash
# On WSL/Linux/macOS
./build_images.sh
```

### Go back to the project root folder

```bash
cd ..
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

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for full details.
