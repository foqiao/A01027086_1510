def file_IO(user_input):
    file = 'project gutenberg.txt'
    appear_ranking = []
    appear_times = 1
    if user_input == "project gutenberg":
        with open(file, "r") as read_file:
            for i in file:
                index_i = file.index(i)
                read_file.read(index_i)
                for j in file:
                    index_j = file.index(j)
                    read_file.read(index_j)
                    if i == j and file.index(i) != file.index(j):
                        word_index = file.index(i)
                        appear_ranking[word_index] = appear_times + 1
                    else:
                        appear_ranking.append(appear_times)
            appear_ranking.sort(reverse=True)
            return appear_ranking[0]
    else:
        return None

def main():
    user_input = str(input("Please enter the name of the file before read it: "))
    print(file_IO(user_input))

if __name__ == '__main__':
    main()