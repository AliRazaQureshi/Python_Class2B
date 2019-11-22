d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def key_present(a):
    if a in d:
        print("Key is present in dictionary")
    else:
        print("Key is not present in dictionary")

key_present(4)
key_present(7)