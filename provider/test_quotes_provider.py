from multiprocessing import Process

import pytest
from pact import Verifier

from pact_quotes_server import run_server


PACT_BROKER_URL = "http://localhost:9292"
PROVIDER_URL = "http://localhost:8000"

@pytest.fixture(scope="module")
def server():
    proc = Process(target=run_server, args=(), daemon=True)
    proc.start()

    yield proc

    proc.kill()


def test_quote_service(server):

    verifier = Verifier(provider="QuoteServer", provider_base_url=PROVIDER_URL)
    success, logs = verifier.verify_with_broker(
        broker_url=PACT_BROKER_URL,
        verbose=True,
        provider_states_setup_url=f"{PROVIDER_URL}/_pact/provider_states",
        enable_pending=False,
        publish_verification_results=True,
        publish_version="1"
    )
    assert success == 0
