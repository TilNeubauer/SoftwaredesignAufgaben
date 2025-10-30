from collections.abc import Iterable

def lst2falt_lst(lst: list)-> list:
    flat = []
    for s in lst:
        if isinstance(s, Iterable):
            for e in s:
                flat.append(e)
        else:
            flat.append(s)

    return flat


def main() -> None:
    list_of_sets_1 = [(1, 2, 3), (4, 5, 6), (7, 8)]
    list_of_sets_2 = [(1, 2, 3), (4, 5, 6), (7, 8), (9)]
    list_of_sets_3 = [(1, 2, 3), (4, 5, 6), (7, 8), (9,)]
    list_of_lists_4 = [[1, 2, 3], [4, 5, 6], [7, 8], [9]]

    print(f"1: {lst2falt_lst(list_of_sets_1)}")
    print(f"2: {lst2falt_lst(list_of_sets_2)}")
    print(f"3: {lst2falt_lst(list_of_sets_3)}")
    print(f"4: {lst2falt_lst(list_of_lists_4)}")

    sentence = "I spy with my little eye a tricky" \
           " list and dict comprehension coming up"
    words = sentence.split()
    words_len = list(map(lambda x: len(x), words))
    print(f"5: words = {words}")
    print(f"6: {words_len}")

    
    dict_sentence = {}
    for word in words:
        l = len(word)
        if l not in dict_sentence:
            dict_sentence[l] = set()
        dict_sentence[l].add(word)

    sentence2 = "I love Python!"
    dict_sentence2 = {length: {w for w in sentence2.split() if len(w) == length} for length in set(map(len, sentence2.split()))}

    print(f"7: {dict_sentence}")
    print(f"8: {dict_sentence2}")


if __name__ == "__main__":
    main()