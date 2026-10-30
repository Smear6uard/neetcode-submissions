from typing import List

def contains_duplicate(words: List[str]) -> bool:
    list_len = len(words)
    set_change = set(words)
    set_len = len(set_change)
    if list_len != set_len:
        return True
    else:
        return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
