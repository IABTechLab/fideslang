import nox

nox.options.sessions = ["check_all"]
nox.options.stop_on_first_error = True


def install_requirements(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.install("-r", "dev-requirements.txt")


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
@nox.parametrize("pydantic_version", ["1.8.2", "1.9.2", "1.10.9"])
def tests(session: nox.Session, pydantic_version: str) -> None:
    install_requirements(session)
    session.install(f"pydantic=={pydantic_version}")
    session.install(".")
    if session.posargs:
        test_files = session.posargs
    else:
        test_files = [""]
    session.run("pytest", "-x", *test_files)


@nox.session(python="3.8")
def black(session: nox.Session) -> None:
    install_requirements(session)
    session.run("black", "--check", "src/")


@nox.session(python="3.8")
def mypy(session: nox.Session) -> None:
    install_requirements(session)
    session.run("mypy")


@nox.session(python="3.8")
def pylint(session: nox.Session) -> None:
    install_requirements(session)
    session.run("pylint", "src/")


@nox.session(python="3.8")
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


@nox.session(python="3.8")
def check_static(session: nox.Session) -> None:
    black(session)
    pylint(session)
    mypy(session)
    xenon(session)


@nox.session(python="3.8")
def check_all(session: nox.Session) -> None:
    check_static(session)
    session.notify("tests")
