@echo off
echo 🚀 Building Docker images for Cody...

docker build -t code_runner_python images\python
if errorlevel 1 (
    echo ❌ Failed to build Python image
    exit /b 1
)

docker build -t code_runner_javascript images\javascript
if errorlevel 1 (
    echo ❌ Failed to build JavaScript(Node.js) image
    exit /b 1
)

echo ✅ All docker images built successfully.
pause
