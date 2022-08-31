from sys import argv

def func():

    if len(argv) < 2:
        return 0

    textToPrint = argv[1]

    if "." in argv[1]:
        textToPrint = argv[1].rsplit(".", 1)[0]

    f = open(argv[1], "a")
    f.write(textToPrint)
    f.close()

if __name__ == "__main__":
    func()
#test
