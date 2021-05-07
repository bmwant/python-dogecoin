import pytest


@pytest.fixture
def db(request):
    session = request.session
    if hasattr(session, '_mysql_container'):
        print('Skip cleaning state')
        return


def pytest_addoption(parser):
    parser.addoption('--gc-collect', action='store_true',
                     default=False,
                     help="Perform GC collection after every test")


@pytest.mark.trylast
def pytest_runtest_teardown(item, nextitem):
    if item.config.getoption('--gc-collect'):
        gc.collect()
    return nextitem

def pytest_addoption(parser):
    parser.addoption('--run-slow', action='store_true',
                     default=False,
                     help="Run slow tests")

def pytest_runtest_setup(item):
    if ('slowtest' in item.keywords and
            (not item.config.getoption('--run-slow'))):
        pytest.skip('Need --run-slow to run')
