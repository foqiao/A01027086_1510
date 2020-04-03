import re


def is_email(email):
    search_email = re.compile(r'\w+@[0-9a-zA-Z]+.com')
    match_email = search_email.search(email)
    if match_email:
        return True
    else:
        return False

def is_nakamoto(name):
    search_name = re.compile(r"[A-Z][a-z]+\s['Nakamoto']")
    match_name = search_name.search(name)
    if match_name:
        return True
    else:
        return False

def is_poker(input_poker):
    search_poker = re.compile(r'[akqjt]+[2-9]+')
    match_poker = search_poker.search(input_poker)
    if match_poker:
        return True
    else:
        return False

def main():
    email_input = input("Please enter an email: ")
    matched_email = is_email(email_input)
    print(matched_email)

    name_input = input("Please enter a name ended with Nakamoto: ")
    matched_name = is_nakamoto(name_input)
    print(matched_name)

    players_choice = input("Please enter a combination of poker: ")
    matched_poker = is_poker(players_choice)
    print(matched_poker)

if __name__ == '__main__':
    main()