import nox

nox.options.sessions = []
nox.options.reuse_existing_virtualenvs = True

# These should match what is in the `pr_checks.yml` file for CI runs
TESTED_PYTHON_VERSIONS = ["3.9", "3.10", "3.11"]
TESTED_PYDANTIC_VERSIONS = ["2.3.0", "2.4.2",  "2.5.3", "2.6.4", "2.7.1"]
TESTED_PYYAML_VERSIONS = ["5.4.1", "6.0.1"]


def install_requirements(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.install("-r", "dev-requirements.txt")


@nox.session(python=TESTED_PYTHON_VERSIONS)
@nox.parametrize("pydantic_version", TESTED_PYDANTIC_VERSIONS)
@nox.parametrize("pyyaml_version", TESTED_PYYAML_VERSIONS)
def tests(session: nox.Session, pydantic_version: str, pyyaml_version: str) -> None:
    install_requirements(session)
    session.install(".")
    session.install(f"pydantic=={pydantic_version}")
    session.install(f"pyyaml=={pyyaml_version}")
    if session.posargs:
        test_args = session.posargs
    else:
        test_args = [""]
    session.run("pytest", *test_args)


@nox.session()
def pytest(session: nox.Session) -> None:
    """Runs the pytest suite with default versions."""
    install_requirements(session)
    session.install(".")
    session.run("pytest")


@nox.session()
def black(session: nox.Session) -> None:
    install_requirements(session)
    session.run("black", "--check", "src/")


@nox.session()
def mypy(session: nox.Session) -> None:
    install_requirements(session)
    session.run("mypy")


@nox.session()
def pylint(session: nox.Session) -> None:
    install_requirements(session)
    session.run("pylint", "--jobs", "0", "src/")


@nox.session()
def xenon(session: nox.Session) -> None:
    install_requirements(session)
    session.run(
        "xenon",
        "src",
        "--max-absolute",
        "B",
        "--max-modules",
        "B",
        "--max-average",
        "A",
        "--ignore",
        "data,tests,docs",
        "--exclude",
        "src/fideslang/_version.py",
    )


@nox.session()
def static_checks(session: nox.Session) -> None:
    """Run the static checks."""
    session.notify("black")
    session.notify("xenon")
    session.notify("pylint")
    session.notify("mypy")


@nox.session()
def check_all(session: nox.Session) -> None:
    """Run static checks as well as tests."""
    session.notify("static_checks")
    session.notify("tests")
