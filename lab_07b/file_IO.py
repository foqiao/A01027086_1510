def file_IO(user_input):
    number_of_words_dictionary = {}

    with open(user_input, "r") as read_file:
        lines = read_file.readlines()
        for line in lines:
            words = line.split(' ')
            for word in words:
                if word in number_of_words_dictionary.keys():
                    number_of_words_dictionary[word] += 1
                else:
                    number_of_words_dictionary[word] = 1

    return number_of_words_dictionary

def rank_words(word_dictionary):
    ranked_words = sorted([(value, key) for key, value in word_dictionary.items()], reverse=True)
    return ranked_words[0:9]


def main():
    user_input = input("Please enter the name of the file with .txt before read it: ")
    word_count_dictionary = file_IO(user_input)
    print(rank_words(word_count_dictionary))

if __name__ == '__main__':
    main()