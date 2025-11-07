LANGUAGE_CONFIG = {
    "java": {
        "docker_image": "cody_java",
        "file_name": "Main.java",
        "run_cmd": ["/bin/sh", "-c", "javac Main.java && java Main"]
    },

    "python": {
        "docker_image": "cody_python",
        "file_name": "main.py",
        "run_cmd": ["python", "main.py"]
    },

    "javascript": {
        "docker_image": "cody_javascript",
        "file_name": "main.js",
        "run_cmd": ["node", "main.js"]
    },
}
