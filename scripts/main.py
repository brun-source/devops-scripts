import os
import shutil
import yaml
from datetime import datetime

def backup_config_file():
    config_file_path = 'config.yaml'
    if os.path.exists(config_file_path):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(os.getcwd(), f'config_{timestamp}.yaml')
        shutil.copy2(config_file_path, backup_path)
        print(f'Config file backed up to {backup_path}')

def load_config():
    config_file_path = 'config.yaml'
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    else:
        print('Config file not found.')
        return None

def main():
    config = load_config()
    if config:
        print(f'Config loaded: {config}')
    else:
        backup_config_file()
        print('Config file backed up. Please update config.yaml.')

if __name__ == '__main__':
    main()