some_words = ["hello", "world", "how", "are", "you", "doing", "today"]


def contains_i(words):
    i_words = []
    for word in words:
        if "i" in word:
            i_words.append(word)
    return i_words


def contains_i_gen(words):
    for word in words:
        if "i" in word:
            yield word


print(contains_i(some_words))
print(list(contains_i_gen(some_words)))
