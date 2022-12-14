import uvicorn
from fastapi import APIRouter
from pydantic import BaseModel

from quote_server import app, quotes, router as main_router

pact_router = APIRouter()


class ProviderState(BaseModel):
    state: str  # noqa: E999


@pact_router.post("/_pact/provider_states")
async def provider_states(provider_state: ProviderState):
    mapping = {
        "A fixed quote": setup_fixed_quote,
        "A quote to add": setup_add_quote,
    }
    mapping[provider_state.state]()

    return {"result": mapping[provider_state.state]}


# Make sure the app includes both routers. This needs to be done after the
# declaration of the provider_states
app.include_router(main_router)
app.include_router(pact_router)


def run_server():
    uvicorn.run(app)


def setup_fixed_quote():

    quotes.clear()
    quotes.append({'quote': 'A quote', 'author': 'Anonymous'})


def setup_add_quote():

    quotes.clear()
