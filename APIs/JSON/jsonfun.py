"""Play with json files."""

import requests


def download_page(url: str) -> str:
    res = requests.get(url)
    # while res.status_code != requests.codes.ok:
    #     pass
    res.raise_for_status()
    print(len(res.text))
    print(res.text[:250])  # prints the first 250 characters
    contents = res.text
    return contents


def main():
    value = download_page('https://www.gutenberg.org/files/28054/28054-0.txt')
    print(value)


if __name__ == "__main__":
    main()