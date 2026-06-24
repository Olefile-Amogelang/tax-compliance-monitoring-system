import pandas as pd

def load_data():
    taxpayers = pd.read_csv("data/taxpayers.csv")
    filings = pd.read_csv("data/filings.csv")
    transactions = pd.read_csv("data/transactions.csv")
    return taxpayers, filings, transactions
