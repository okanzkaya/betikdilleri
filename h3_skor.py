import random
def macsonucu():
    fb = random.randint(0,10)
    gs = random.randint(0,10)
    if fb>gs:
        print("GS kazanır")
    elif fb==gs:
        print("Berabere")
    else:
        print("FB kazanır")


if __name__ == '__main__':
    macsonucu()
