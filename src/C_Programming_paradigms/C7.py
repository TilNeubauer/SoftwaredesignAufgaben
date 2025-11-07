

def main() -> None:
    #C7.1 find palindromes
    str_list = ["Hello", "World", "anna"]

    is_palindromes = lambda a: a == a[::-1]
    str_lsit_palindromes = filter(is_palindromes, str_list)

    print(f"{list(str_lsit_palindromes) = }")

    #C7.2
    word = "HalloWorld"

    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    is_vowel = lambda a: a in vowel
    vowels_in_word = filter(is_vowel, word)

    print(f"{len(list(vowels_in_word)) = }")

if __name__ == "__main__":
    main()