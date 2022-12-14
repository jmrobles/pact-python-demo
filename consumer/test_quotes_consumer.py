import json
from quotes_consumer import QuoteConsumer

PACT_MOCK_HOST = "localhost"
PACT_MOCK_PORT = 1234

def test_get_quote(pact):

    consumer = QuoteConsumer(f'http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}')

    expected = {
        'quote': 'A quote',
        'author': 'Anonymous'
    }

    (
        pact.given("A fixed quote")
        .upon_receiving("a request for the quote")
        .with_request("get", "/api/v1/quotes")
        .will_respond_with(200, body=expected)
    )
    with pact:
        quote = consumer.get_random_quote()
        assert quote == 'A quote, Anonymous'
        pact.verify()

def test_create_quote(pact):

    consumer = QuoteConsumer(f'http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}')

    quote = {
        'quote': 'To test or to test',
        'author': 'A tester'
    }

    (
        pact.given("A quote to add")
        .upon_receiving("a request for adding the new quote")
        .with_request("post", "/api/v1/quotes", body=quote, headers={'Content-type': 'application/json'})
        
        .will_respond_with(201)
    )

    with pact:

        is_created = consumer.put_my_quote(quote['quote'], quote['author'])
        assert is_created
        pact.verify()
