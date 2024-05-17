# Taskmates Demo

## Clone this repo

```shell
git clone git@github.com:taskmates/demo.git /var/demos/taskmates-demo
```

## Install some taskmates


```shell
git clone git@github.com:taskmates/taskmates-directory.git /opt/taskmates/taskmates
```

## Login to the github container registry

```shell
echo $GH_ACCESS_TOKEN | docker login ghcr.io -u $GH_USERNAME --password-stdin
```

## taskmates daemon

Remove the env vars you don't need

```shell
docker pull ghcr.io/srizzo/taskmates:main

docker run -it --rm --name taskmates -e JIRA_API_KEY -e JIRA_PROJECT -e JIRA_SERVER -e JIRA_USER -e ANTHROPIC_API_KEY -e OPENAI_API_KEY -e ENTERPRISE_GATEWAY_ENDPOINT=http://host.docker.internal:10100 -e ENABLE_TRACING=false -e GOOGLE_API_KEY -e GOOGLE_CSE_ID -e JIRA_USER -e JIRA_API_KEY -e JIRA_PROJECT -e JIRA_SERVER -e JIRA_USER --add-host=host.docker.internal:host-gateway -p 5000:5000 -v /opt/taskmates/:/opt/taskmates/ ghcr.io/srizzo/taskmates:main
```

## enterprise-gateway (via docker)

Start the server

```shell
docker pull ghcr.io/taskmates/enterprise-gateway:main

docker run -it --name enterprise_gateway -p 10100:10100 -v /var/demos/taskmates-demo:/var/demos/taskmates-demo -v /var/demos/taskmates-demo:/private/var/demos/taskmates-demo ghcr.io/taskmates/enterprise-gateway:main
```

## enterprise-gateway (locally)

You can run it locally, but you will not have the file_editing_magics extension (until I publish them as a proper package).

```shell
# install using pip from pypi
pip install --upgrade jupyter_enterprise_gateway
```

```shell
# install using conda from conda forge
conda install -c conda-forge jupyter_enterprise_gateway
```

```shell
# start it up
jupyter enterprisegateway --port=10100 --EnterpriseGatewayApp.list_kernels=True
```

To autoload the file_editing_magics (e.g. `%%append_to_file` etc) extension (used by some dev taskmates to speed up file editing tasks), add the following to your ipython_config.py file (usually located at ~/.ipython/profile_default/ipython_config.py

```python
# ~/.ipython/profile_default/ipython_config.py
c.InteractiveShellApp.extensions = ['taskmates_enterprise_gateway.file_editing_magics'] 
```

Optionaly, ask the taskmate to use the default `%%writefile`


## Play around with it

1. Semi-automated coding: [coding.md](coding.md)
2. Jupyter environment: [jupyter-environment.md](Features%2F10.%20Jupyter%20environment%2Fjupyter-environment.md)

Explore:  [Features](Features)
