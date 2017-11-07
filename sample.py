def usqlml_main(df):
    df1 = df.query('SepalLength > 5').assign(SepalRatio = lambda x: x.SepalWidth / x.SepalLength, PetalRatio = lambda x: x.PetalWidth / x.PetalLength)
    return df1,
    