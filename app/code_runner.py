import os
import uuid
import docker
import tempfile
from app.language_config import LANGUAGE_CONFIG

docker_client = docker.from_env()


def run_code(language, code):
    if language not in LANGUAGE_CONFIG:
        return {"error": f"Cody doesn't support {language}"}

    config = LANGUAGE_CONFIG[language]
    file_name = config["file_name"]
    docker_image = config["docker_image"]
    run_cmd = config["run_cmd"]

    temporary_directory = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
    os.makedirs(temporary_directory, exist_ok=True)

    code_path = os.path.join(temporary_directory, file_name)

    with open(code_path, 'w') as file:
        file.write(code)

    try:
        container = docker_client.containers.run(
            image=docker_image,
            command=run_cmd,
            volumes={temporary_directory: {"bind": "/app", "mode": "ro"}},
            working_dir="/app",
            stderr=True,
            stdout=True,
            network_disabled=True,
            detach=True,
            mem_limit="100m",
            pids_limit=50,
            auto_remove=True
        )

        exit_status = container.wait(timeout=5)
        logs = container.logs(stdout=True, stderr=True).decode(errors="ignore").strip()

        if exit_status["StatusCode"] == 0:
            return {"output": logs}
        else:
            return {"error": logs}

    except Exception as e:
        return {"error": str(e)}