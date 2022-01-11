import xlrd
import csv
import os

inputdir = "data/"

filenames = os.listdir(inputdir)      

def csv_from_excel(filename):
    print(filename + 'starting..')
    wb = xlrd.open_workbook(inputdir + filename)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(filename+'.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    print(filename + 'ending..')
    your_csv_file.close()

# runs the csv_from_excel function:
for filename in filenames:
    csv_from_excel(filename)
