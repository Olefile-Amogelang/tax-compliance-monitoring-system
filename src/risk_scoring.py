def compute_risk_score(df):
    df['risk_score'] = 0

    df.loc[df['underreport_flag'] == True, 'risk_score'] += 50

    return df
