import sys

def translationCall(Input):
    if Input == "虎":
        return "tiger" 
    if Input == "火":
        return "fire"
    return "jya-jya-";


if __name__ == "__main__":
    Input  = sys.argv[1] 
    returnVAlue = translationCall(Input);
    print(returnVAlue)