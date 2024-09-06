import sys

import nox
from nox_poetry import Session, session

locations = "hello_poetry_and_nox", "tests", "noxfile.py"
nox.options.envdir = ".cache"
nox.options.reuse_existing_virtualenvs = True
nox.options.stop_on_first_error = True
nox.options.sessions = (
    "black",
    "lint",
    "mypy",
    "tests",
)


@session(python=["3.12"])
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", "--line-length", "82", *args)


@session(python=["3.12"])
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "flake8",
    )
    session.run("flake8", *args)


@session(python=["3.12"])
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or [
        "--install-types",
        "--non-interactive",
        "hello_poetry_and_nox",
        "tests",
    ]
    session.install(".")
    session.install("mypy", "pytest")
    session.run("mypy", *args)
    if not session.posargs:
        session.run("mypy", f"--python-executable={sys.executable}", "noxfile.py")


@session(python=["3.12"])
def tests(session: Session):
    args = session.posargs or [
        "--cov",
        "--cov-report",
        "term",
        "--cov-report",
        "html",
    ]
    session.install("pytest", "pytest-cov", ".")
    session.run("pytest", *args)
