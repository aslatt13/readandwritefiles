#using the file steps.csv, calculate the average steps taken each month.
# Each row represents one day. Output should have the name of the month and the 
# corresponding average steps for that month (such as 'January, 5246.19')

def main():
    import csv

    infile = open('steps.csv','r')
    outfile = open('avg_steps.csv','w')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    outfile.write('Month, Avg Steps\n')



    for record in csvfile:
        month = record[0]
        
        avg_steps = 

        outfile.write(month + ',' + avg_steps + '\n')

    outfile.close()






main()