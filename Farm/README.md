# CD_opdracht
# Continuous Deployment Pipeline Report

## Components

1. **Digital Ocean VPS**:
   - A virtual private server where the Flask application is hosted. It provides the computing resources required to run the application and handles incoming web traffic.

2. **GitHub Actions**:
   - A CI/CD service provided by GitHub that automates the testing and deployment process. It ensures that any code pushed to the repository is tested and, if successful, deployed to the VPS.

3. **SSH and Bash Scripts**:
   - Secure Shell (SSH) is used for secure communication between GitHub Actions and the VPS. Bash scripts automate the deployment process, including pulling the latest code, installing dependencies, and restarting the application.

## Problems Encountered and Solutions

1. **SSH Key Management**:
   - *Problem*: Securely transferring the SSH key to GitHub Actions.
   - *Solution*: Generated an SSH key pair and added the private key as a secret in GitHub, ensuring secure access to the VPS.

2. **Service Management**:
   - *Problem*: Ensuring the Flask application restarts with new code.
   - *Solution*: Created a systemd service for the Flask application, allowing easy management and ensuring it restarts upon code updates.

3. **Workflow Configuration**:
   - *Problem*: Configuring GitHub Actions to correctly test and deploy the application.
   - *Solution*: Defined a workflow in `deploy.yml` that runs tests with Pytest and deploys the application using SSH and Bash scripts only if the tests pass.

## Additional Notes

- Automating deployment reduces the risk of human error and ensures a consistent deployment process.
- Using GitHub Actions secrets keeps sensitive information secure, aligning with best practices in DevOps.

