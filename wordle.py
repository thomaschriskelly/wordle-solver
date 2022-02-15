from english_words import english_words_lower_alpha_set
import argparse

def main():
    parser = argparse.ArgumentParser(description='Solve Wordle')
    parser.add_argument("whitelist", help="Whitelisted letters")
    parser.add_argument("blacklist", help="Blacklisted letters")
    parser.add_argument("positions", help="Known letter positions. eg C*AM*")
    args = parser.parse_args()

    five_letter_words = [
        word for word in english_words_lower_alpha_set
        if len(word) == 5
    ]
    whitelist = set([letter for letter in args.whitelist])
    whitelisted = [
        word for word in five_letter_words
        if all(letter in word for letter in whitelist)
    ]
    blacklist = set([letter for letter in args.blacklist])
    blacklisted = [
        word for word in whitelisted
        if not any(letter in word for letter in blacklist)
    ]
    position_filtered = [
        word for word in blacklisted
        if all(
            letter == '*' or
            (letter.islower() and letter == word[index]) or
            (letter.isupper() and letter.lower() != word[index])
            for index, letter in enumerate(args.positions)
        )
    ]
    for word in position_filtered:
        print(word)

main()