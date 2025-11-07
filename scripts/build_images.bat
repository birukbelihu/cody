@echo off
echo 🚀 Building Docker images for Cody...

docker build -t cody_python ..\images\python

if errorlevel 1 (
    echo ❌ Failed to build Python Docker image
    exit /b 1
)

docker build -t cody_javascript ..\images\javascript

if errorlevel 1 (
    echo ❌ Failed to build JavaScript(Node.js) Docker image
    exit /b 1
)

echo ✅ All docker images built successfully!!!
pause
