import csv, os

os.makedirs('header_removed', exist_ok=True)

for filename in os.listdir():
    if filename.endswith(' .csv'):
        print('remove head from ' + filename + '...')

file_rows = []
with open(filename) as csv_file:
    my_reader = csv.reader(csv_file)
    for row in my_reader:
        if my_reader.line_num != 1:
            file_rows.append(row)

with open(os.path.join('header_removed', filename), 'w', newline='') as csv_file:
    csv_writer =csv.writer(csv_file)
    for row in file_rows:
        csv_writer.writerow(row)