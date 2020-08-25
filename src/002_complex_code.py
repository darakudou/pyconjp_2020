
def order(order):

    menus = ["egg and spam", "bacaon and spam", "egg bacon and spam",]
    is_egg = False
    for menu in menus:
        if "egg" in order:
            is_egg = True
        if is_egg:
            for m in menus:
                if "egg" in m:
                    return m
    return "spam spam spam and spam"

if __name__ == "__main__":
    input = sys.argv[1]
    orderd_menu = order(imput);
    print(orderd_menu)
