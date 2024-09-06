# hello-hypermodern-python-tooling

A small project to play with the toolchain outlined in the orignal article series [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)[^1].

A "postmodern" and much simpler toolchain can now be built around [uv](https://github.com/astral-sh/uv)[^2].

## Installation, run and test

### Requirements

- pyenv
- pipx
- poetry
- nox
- nox-poetry

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

## References

[^1]: [Claudio Jolowicz (2024): Hypermodern Python Tooling](https://www.oreilly.com/library/view/hypermodern-python-tooling/9781098139575/)
[^2]: [Chris Arderne (2024): Beyond Hypermodern: Python is easy now](https://rdrn.me/postmodern-python/)
