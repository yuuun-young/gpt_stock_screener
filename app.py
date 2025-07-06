from fastapi import FastAPI
from utils.screener import run_stock_filter

app = FastAPI()

@app.get("/filter_stocks")
def filter_stocks():
    return run_stock_filter()
