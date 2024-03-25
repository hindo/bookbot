def read_file_contents(file_path):
    with open("./books/frankenstein.txt") as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_leters(text):
    count_dict = {}
    lowercased_text = text.lower()
    for letter in lowercased_text:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

    return count_dict

def print_report(letter_count_dict):
    def sort_on(dict):
        return dict["count"]

    letter_count_list = []
    for sign in letter_count_dict:
        if sign.isalpha():
            letter_count_list.append({
                "letter": sign,
                "count": letter_count_dict[sign]
            })
    
    letter_count_list.sort(reverse=True, key=sort_on)

    for entry in letter_count_list:
        print(f"The '{entry["letter"]}' character was found {entry["count"]} times")

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = read_file_contents(file_path)

    word_count = count_words(file_contents)
    letter_count = count_leters(file_contents)

    print(file_contents)
    print(word_count)
    print(letter_count)

    print_report(letter_count)


if __name__ == "__main__":
    main()
