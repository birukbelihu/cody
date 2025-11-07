#!/bin/bash

echo "🚀 Building Docker images for Cody..."

docker build -t code_runner_python ../images/python || {
  echo "❌ Failed to build Python docker image.";
  exit 1;
}

docker build -t code_runner_javascript ../images/javascript || {
  echo "❌ Failed to build JavaScript(Node.js) docker image.";
  exit 1;
}

echo "✅ All docker images built successfully!!!"