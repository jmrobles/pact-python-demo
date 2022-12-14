import atexit
import os

import pytest

from pact import Consumer, Provider

PACT_BROKER_URL = "http://localhost:9292"
# PACT_BROKER_USERNAME = "pactbroker"
# PACT_BROKER_PASSWORD = "pactbroker"

PACT_MOCK_HOST = "localhost"
PACT_MOCK_PORT = 1234

# Where to output the JSON Pact files created by any tests
PACT_DIR = os.path.dirname(os.path.realpath(__file__))

def pytest_addoption(parser):
    parser.addoption(
        "--publish-pact", type=str, action="store", help="Upload generated pact file to pact broker with version"
    )

    parser.addoption("--provider-url", type=str, action="store", help="The url to our provider.")


@pytest.fixture(scope="session")
def pact(request):

    version = request.config.getoption("--publish-pact")
    publish = True if version else False

    pact = Consumer("QuoteCLI", version=version).has_pact_with(
        Provider("QuoteServer"),
        host_name=PACT_MOCK_HOST,
        port=PACT_MOCK_PORT,
        pact_dir=PACT_DIR,
        publish_to_broker=publish,
        broker_base_url=PACT_BROKER_URL,
    )

    pact.start_service()

    atexit.register(pact.stop_service)

    yield pact

    pact.stop_service()

    pact.publish_to_broker = False
