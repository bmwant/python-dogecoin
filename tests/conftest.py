import pytest


@pytest.fixture
def db(request):
    session = request.session
    if hasattr(session, "_mysql_container"):
        print("Skip cleaning state")
        return


def pytest_addoption(parser):
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Execute integration tests too",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-integration"):
        return

    integration_marker = pytest.mark.skip("Need --run-integration to run")
    for item in items:
        if "integration" in item.keywords:
            item.add_marker(integration_marker)


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: requires testnet to be lauched")
