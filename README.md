# hello-poetry-and-nox

## Installation, run and test

### Requirements

- pyenv
- pipx

```shell
% pyenv install 3.12.0
% pipx install poetry
% pipx install nox
% pipx inject nox nox-poetry
```

### Install

```shell
% poetry install
```

### Run linters and tests

```shell
% nox
```

### Run in development mode

```shell
% poetry run fastapi dev hello_poetry_and_nox/main.py
```

## Test with curl

```shell
% curl -i http://localhost:8000
HTTP/1.1 200 OK
date: Thu, 05 Sep 2024 14:16:59 GMT
server: uvicorn
content-length: 18
content-type: application/json

{"Hello":"World!"}
```
