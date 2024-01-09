import gzip

''' Replace the file with your file name'''
with gzip.open('calendar.csv.gz', 'rt', newline='') as csv_file:
    csv_data = csv_file.read()
    with open('calendar.csv', 'wt') as out_file:
         out_file.write(csv_data)
