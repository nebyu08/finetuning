import os
from subprocess import Popen, PIPE, STDOUT, run, CalledProcessError

def main():
    try:
        # Correctly run the chown command using subprocess
        print("Changing ownership of Elasticsearch directory...")
        run(["chown", "-R", "daemon:daemon", "elasticsearch-8.15.1"], check=True)
        print("Ownership changed successfully.")
        
        # Run Elasticsearch as a background process
        print("Starting Elasticsearch...")
        es_server = Popen(
            args=['elasticsearch-8.15.1/bin/elasticsearch'], 
            stdout=PIPE, stderr=STDOUT, preexec_fn=lambda: os.setuid(1)
        )
        
        # Wait until Elasticsearch has started
        print("Waiting for Elasticsearch to start...")
        run(["sleep", "30"], check=True)
        print("Elasticsearch should now be running.")

    except CalledProcessError as e:
        print(f"Subprocess error: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
