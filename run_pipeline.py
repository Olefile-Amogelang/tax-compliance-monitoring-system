from src.ingestion import load_data
from src.compliance_checks import check_late_filing, check_underreporting
from src.risk_scoring import compute_risk_score
from src.database import save_to_db

taxpayers, filings, transactions = load_data()

filings = check_late_filing(filings)
df = check_underreporting(transactions, filings)
df = compute_risk_score(df)

save_to_db(df)

print("Compliance pipeline executed successfully")
