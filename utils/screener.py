import pandas as pd

def run_stock_filter():
    try:
        tickers = pd.read_csv("nasdaq_tickers.csv")
        # 간단 필터 예시
        return {"count": len(tickers), "sample": tickers.head(5).to_dict(orient="records")}
    except Exception as e:
        return {"error": str(e)}
