"""Play with CSV files."""

import csv


def read_CSV(filename: str) -> None:
    with open(filename) as example_file:
        example_reader = csv.reader(example_file)
        file_as_list = list(example_reader)
        print(file_as_list)
        # for row in example_reader:
        #     print(row)


def create_file(filename: str) -> None:
    with open(filename, 'w', newline='') as example_file:
        printed = 0
        output_writer = csv.writer(example_file)
        printed += output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
        printed += output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
        printed += output_writer.writerow([1, 2, 3.141592, 4])
        print(printed, "characters printed")


def write_dict():
    with open('names.csv', 'w', newline='') as csvfile:
        column_headers = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=column_headers)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Peanut Butter Cups'})


def main():
    # read_CSV("example.csv")
    # create_file("sohungry.csv")
    write_dict()




if __name__ == "__main__":
    main()