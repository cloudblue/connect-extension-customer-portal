# Deployment
There are two ways in which the extension can be deployed:

## Deploy through docker image

1. Checkout code from `https://github.com/cloudblue/connect-extension-customer-portal`
2. Configure the portal as per [Configuration Page](configuration.md) for docker run.
3. Modify the code as per your requirements.
4. Rum following command on command prompt to run the project:
```shell
docker compose up app
```
4. Open browser with URL `http://localhost:8080`
5. You can publish docker image with your modified code and deploy that image in kubernetes cluster.

