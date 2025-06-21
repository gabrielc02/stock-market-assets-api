"""
Main module for FastAPI GRAPHQL.
"""
from fastapi import FastAPI
from ariadne import load_schema_from_path, QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from yahoofinance import HistoricalPrices

# Load schema from file
type_defs = load_schema_from_path("./src/schema.gql") # just turn schema in a string do not turn it executable
query = QueryType()
schema = make_executable_schema(type_defs, query)

# Creata FASTAPI instance
app = FastAPI()

# Mount GraphQL under a route like "/graphql"
app.mount("/graphql", GraphQL(schema, debug=True))


# GRAPHQL RESOLVERS
@query.field("asset")
async def resolver_product(_, info):
    request = info.context["request"]
    user_agent = request.get("HTTP_USER_AGENT", "guest")
    return await "Hello, %s!" % user_agent

# REAST ENDPOINTS
@app.get("/")
def first_root():
    """Endpoint to test API availability."""
    return{"message": "API IS RUNNING"}


