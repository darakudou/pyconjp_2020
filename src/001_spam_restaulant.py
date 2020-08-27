import sys
import datetime

def OrderMenu(menuName):
    guests = "Viking"   
    return f"spam, {menuName}, spam and spam!"

if __name__ == "__main__":
    Input  = sys.argv[1]
    orderdMenu = OrderMenu(Input);
    print(orderdMenu)