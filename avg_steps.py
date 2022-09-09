#using the file steps.csv, calculate the average steps taken each month.
# Each row represents one day. Output should have the name of the month and the 
# corresponding average steps for that month (such as 'January, 5246.19')

def main():
    import csv

    infile = open('steps.csv','r')
    outfile = open('avg_steps.csv','w')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    steps = [0]
    days = [0]
    month = 1

    for row in csvfile:
        if int(row[0]) != month:
            month += 1
            steps.append(0)
            days.append(0)
        steps[month-1] += int(row[1])
        days[month-1] += 1

    infile.close()
        

    outfile.write('Month, Avg Steps\n')

    month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']

    for month in range(len(days)):
        avg_steps = steps[month] / days[month]
        outfile.write(month_list[month] + ',' + '{:0.2f}'.format(avg_steps) + '\n')

    outfile.close()



main()