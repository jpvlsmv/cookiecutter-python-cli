# noxfile.py
import nox

nox.options.sessions = [ "tests" ]

@nox.session(python=False)
def all(session):
    """Run all sessions"""
    for runner, enabled in session._runner.manifest.list_all_sessions():
        if runner.name != "all":
            print(f'all meta-session running session {runner.name}')
            runner.execute()

@nox.session(python=["3.9", "3.7"], reuse_venv=True)
def tests(session):
    """FullBuild"""
    args = session.posargs or ["--cov", "--cov-report=term-missing"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.9"], reuse_venv=True)
def lint(session):
    """Style Checking"""
    session.run("poetry", "install", "--no-root", external=True)
    session.run("black", "-l", "79", "--diff", "src", "tests")
    session.run("flake8", "src", "tests")
    session.run("mypy", "src", "tests")


@nox.session(python=False)
def docs(session):
    """BuildDocs"""
    session.chdir("docs")
    session.run("make", "html", external=True)
