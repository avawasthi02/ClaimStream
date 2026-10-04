import pandas as pd





if __name__ == '__main__':

    df = pd.read_csv("output/output/csv/payers.csv")
    print(df.columns)

    print(df[['NAME','AMOUNT_COVERED']])



