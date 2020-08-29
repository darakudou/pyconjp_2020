import sys


def order_menu(menu):
    if menu in ["egg", "bacon", "baked bean"]:
        return f"spam,{menu}, spam and spam!"
    return f"spam, spam, spam, spam, spam and spam"


if __name__ == "__main__":
    input = sys.argv[1]
    print(order_menu(input))
