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
            
        if next in ")]}":

            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
        
    if(not opening_brackets_stack):
        return "Success"
    
    else:
        return opening_brackets_stack[-1].position
        


def main():
    text = input()

    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)

        if not mismatch:
            print("Success")
        else:
            print(mismatch)

    elif "F" in text:
        file = input()
        with open(file) as f:       
            line = file.readLine()
        mismatch = find_mismatch(line)

        if not mismatch:
            print("Success")
        else:
            print(mismatch)

    
    


if __name__ == "__main__":
    main()
