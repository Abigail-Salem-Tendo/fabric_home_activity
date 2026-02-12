# Fabric home activity
This project provides a script to automate MYSQL setup on a remote Ubuntu server.

## Setup
1. clone the repository.
2. Create a `.env` file in the project root;
```angular2html
HOST=your_server_ip
USER=your_ssh_user
SSH_KEY=path_to_private_key
SSH_PASSPHRASE=your_key_passphrase
DB_NAME=your_database_name
```
3. Make sure your SQL, dump.sql, is also in th project root.

## Usage
Run the script with:

```python3 fabric_deploy.py```

The script will perform all deployment steps automatically.

### Notes
- Since the script is using `sudo` for the MYSQL commands, a MYSQL user or password is not required.