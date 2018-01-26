from csc131 import Dictionaries

def main():
    print("Main")
    d = Dictionaries.get_personal_data()
    print(d)
    for key in sorted(d.keys())
        print("%s: %s" % (key, d[key]))



if __name__ == '__main__':
    main()
