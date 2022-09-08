#python program that reads the employeepay.csv file and prints out 
# details of each employee

from signal import pause


def main():
    import csv

    infile = open('EmployeePay.csv','r')
    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        A = record[3] 
        B = record[4]
        print(record[0] + ', ' + record[1] + ', ' + record[2] + ', ' + '$' + record[3] + ', ' + record[4] + '%' + A * B)
       
        input('Press ENTER to continue to next employee')

main()
