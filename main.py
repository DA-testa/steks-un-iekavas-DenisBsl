# python3
# Deniss Buslajevs 221RDB188
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if (not opening_brackets_stack or not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char, next)):
                return i + 1
            opening_brackets_stack.pop()
    if (opening_brackets_stack):
        return len(opening_brackets_stack)
    else:
        return False

def main():
    text = input()
    if (text == "F"):
        text = input()
        with open(text) as f:
            text = f.readline()
    else:
        text = input()

    mismatch = find_mismatch(text)
    if (mismatch):
        print(mismatch)
    else:
        print("Success")


if __name__ == "__main__":
    main()
