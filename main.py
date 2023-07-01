"""main"""
import subprocess
import time


def check_process_running(process_name):
    """check if process is running"""
    try:
        command = f"ps aux | grep '{process_name}' | grep -v grep"
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )
        output = result.stdout.lower()
        if process_name.lower() in output:
            return True
    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f"An error occurred: {str(error)}")
    return False


while True:
    try:
        if not check_process_running("et_client_app.py"):
            with subprocess.Popen(["python3", "et_client_app.py"]) as process:
                process.wait()
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"An error occurred: {str(e)}")
    time.sleep(0.3)
