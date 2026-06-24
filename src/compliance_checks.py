def check_late_filing(filings):
    filings['late_flag'] = filings['filing_date'] > filings['due_date']
    return filings

def check_underreporting(transactions, filings):
    tx_sum = transactions.groupby('taxpayer_id')['amount'].sum().reset_index()
    filings_sum = filings[['taxpayer_id', 'declared_income']]

    df = tx_sum.merge(filings_sum, on='taxpayer_id')
    df['underreport_flag'] = df['amount'] > df['declared_income']

    return df
