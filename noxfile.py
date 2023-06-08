import nox

def install_requirements(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.install("-r", "dev-requirements.txt")

@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
@nox.parametrize('pydantic_version', ['1.8.2', '1.9.2', '1.10.9'])
def tests(session: nox.Session, pydantic_version: str) -> None:
    install_requirements(session)
    session.install(f'pydantic=={pydantic_version}')
    session.install(".")
    session.run('pytest')
