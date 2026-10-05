import csv





if __name__ == '__main__':


    with open('output/output/csv/payers.csv') as f:
        reader = csv.DictReader(f)

        result = {}

        for row in reader:
            

            if row['NAME'] in result.keys():
                
                result[row['NAME']] = result[row['NAME']]+float(row['AMOUNT_COVERED'])
                
            else:
                result[row['NAME']] = float(row['AMOUNT_COVERED'])

        print(result)

            
            





