import os
import logging
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deploy_app():
    # Set the deployment environment
    env = os.environ.get('DEPLOY_ENV', 'dev')

    # Set the deployment directory
    deploy_dir = f'/path/to/deploy/{env}'

    # Create the deployment directory if it doesn't exist
    os.makedirs(deploy_dir, exist_ok=True)

    # Copy the application code to the deployment directory
    app_code = '/path/to/app/code'
    subprocess.run(['cp', '-r', app_code, deploy_dir], check=True)

    # Set the ownership of the deployment directory
    subprocess.run(['chown', f'{os.getuid()}:staff', deploy_dir], check=True)

    # Restart the application service
    app_service = f'/path/to/app/service'
    subprocess.run([f'systemctl restart {app_service}'], shell=True, check=True)

# Run the deployment script
if __name__ == '__main__':
    deploy_app()