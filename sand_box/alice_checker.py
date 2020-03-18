import io

file_name_input ="C:/Users/foqia/Downloads/alice.txt"

def read_file(file_name):
    with open(file_name, 'r') as file_project:
        file_project.seek(io.SEEK_SET)