import os

from fastapi import FastAPI, HTTPException
from t_tech.invest import Client

app = FastAPI(title="T-Invest Bridge")


TOKEN = os.environ["TBANK_TOKEN"]
ACCOUNT_ID = os.environ["TBANK_ACCOUNT_ID"]


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "t-invest-bridge",
        "endpoints": ["/portfolio", "/positions"]
    }


@app.get("/portfolio")
def portfolio():
    try:
        with Client(TOKEN) as client:
            response = client.operations.get_portfolio(
                account_id=ACCOUNT_ID
            )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"T-Bank API error: {str(e)}"
        )


@app.get("/positions")
def positions():
    try:
        with Client(TOKEN) as client:
            response = client.operations.get_positions(
                account_id=ACCOUNT_ID
            )

        return response

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"T-Bank API error: {str(e)}"
        )
