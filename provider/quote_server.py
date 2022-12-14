import random

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

class Quote(BaseModel):

    quote: str
    author: str

router = APIRouter()

app = FastAPI()

quotes = []

@app.get('/api/v1/quotes')
def get_random_quote():
    print(f'>>> Quotes: {quotes}')
    return random.choice(quotes)

@app.post('/api/v1/quotes', status_code=201)
def create_new_quote(quote: Quote):
    quotes.append({'quote': quote.quote, 'author': quote.author})
    return ''
