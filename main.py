# python3
# Miks Zeltiņš 221RDB123


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next , i + 1))
            pass

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
        
        if(opening_brackets_stack):
            return opening_brackets_stack[0].position
        else:
            return "Success"
    pass


def main():
    print("Input method I/F:")
    text = input()

    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

    elif "F" in text:
        file = input()
        with open(file) as f:       
            line = file.readLine()
        mismatch = find_mismatch(line)
        print(mismatch)
    else:
        print("Error in input text")

    
    


if __name__ == "__main__":
    main()
