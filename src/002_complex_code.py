import sys


def translation(input):
    ja_calls = ["虎", "火", "人造",  "繊維", "海女", "振動", "化繊"]
    en_calls = ["tiger", "fire", "cyber", "fiber", "diver", "viber"]
    i = 0
    j = 0
    is_unmatch = False
    for c in ja_calls:
        if c != input:
            is_unmatch = True
        if c == input:
            is_unmatch = False
        if is_unmatch:
            i = i + 1
            continue
        for cc in en_calls:
            if j != i:
                j += 1
                continue
            return_value = en_calls[j]

    if return_value:
        return return_value
    else:
        return_value = "jya-jya-"
    return return_value

if __name__ == "__main__":
    input = sys.argv[1]
    output = translation(input)
    print(output)
