import csv





if __name__ == '__main__':


    with open('output/output/csv/payers.csv') as f:
        reader = csv.DictReader(f)

        result = {}

        for row in reader:

            if 'NAME' in result.keys():


                result[row['NAME']] = row['NAME']+row['AMOUNT_COVERED']
                
            else:
                result[row['NAME']] = row['AMOUNT_COVERED']

        print(result)

            
            





