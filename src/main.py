"""
Main module for FastAPI GRAPHQL.
"""
from fastapi import FastAPI
from ariadne import load_schema_from_path, QueryType, make_executable_schema
from ariadne.asgi import GraphQL
import yfinance as yf

# Load schema from file
type_defs = load_schema_from_path("./src/schema.gql") # just turn schema in a string, do not turn it executable
query = QueryType()
schema = make_executable_schema(type_defs, query)

# Creata FASTAPI instance
app = FastAPI()

# Mount GraphQL under a route "/graphql"
app.mount("/graphql", GraphQL(schema, debug=True))


# GRAPHQL RESOLVERS
# GRAPHQL TRABALHA COM OBJETO, TANTO PRA REQUISICOES QUANTO PARA O RETORNO
@query.field("assetz")
async def resolver_product(_, info):
    apple = yf.Ticker("AAPL")
    price = apple.info['regularMarketPrice']
    return { "Symbol": "AAPL", "Price": price }

@query.field("asset")
def resolve_asset(_, info):
    return {
        "symbol": "AAPL",
        "price": 213.45  # valor fixo só pra teste
    }


# REST ENDPOINTS
@app.get("/")
def first_root():
    """Endpoint to test API availability."""
    return{"message": "API IS RUNNING!!!"}


