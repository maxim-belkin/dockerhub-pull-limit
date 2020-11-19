# Docker Hub Rate Limit

Determine your limit for anonymous pull requests on Docker Hub.
See [this page][docker-hub-rate-limit] for more information.

## Usage

```sh
python3 dockerhub_pull_limit.py
```

## Requirements

This script requires the following Python libraries:

- `requests`
- `json`
- `jwt` or `PyJWT`
- `jq`

```sh
python3 -m pip install -r requirements.txt
# or
python3 -m pip install -r requirements_alt.txt
```

[docker-hub-rate-limit]: https://docs.docker.com/docker-hub/download-rate-limit/
