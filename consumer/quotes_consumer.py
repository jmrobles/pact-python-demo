import requests


class QuoteConsumer:

    QUOTES_EP =  '/api/v1/quotes'

    def __init__(self, host: str):

        self.host = host

    def get_random_quote(self) -> str:

        response = requests.get(self.host + self.QUOTES_EP)
        data = response.json()
        return f"{data['quote']}, {data['author']}"


    def put_my_quote(self, quote: str, author: str) -> bool:

        response = requests.post(self.host + self.QUOTES_EP, json={'quote': quote, 'author': author})
        return response.status_code == 201


if __name__ == '__main__':

    # Put a quote
    if not put_my_quote(quote, 'Today is a great day to do CDC testing', 'Aristestoles'):
        print('Something went wrong!')

    # Get a quote
    print(f'Quote of the day => {get_random_quote()}')
