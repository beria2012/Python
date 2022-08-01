import hashlib


s = "Python Bootcamp"

def custom_hash(input):
    m = hashlib.sha256()
    m.update(input.encode("utf-8"))
    return m.hexdigest()

def main():
    hasged_s = custom_hash(s)
    print("The 'Python Bootcamp' hash value is: " + str(hasged_s))

if __name__ == '__main__':
    main()