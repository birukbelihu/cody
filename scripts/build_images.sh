#!/bin/bash

echo "🚀 Building Docker images for Cody..."

docker build -t cody_python ../images/python || {
  echo "❌ Failed to build Python docker image.";
  exit 1;
}

docker build -t cody_javascript ../images/javascript || {
  echo "❌ Failed to build JavaScript(Node.js) docker image.";
  exit 1;
}

echo "✅ All docker images built successfully!!!"