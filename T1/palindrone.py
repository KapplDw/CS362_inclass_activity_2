# Dwight Kappl
# Palindrome

def palind(txt):
    txt = txt.lower()
    temp = txt[::-1]
    if temp == txt:
        # It is a palindrome
        print(txt + " is a palindrome.")
        return True
    else:
        print(txt + " is not a palindrome.")
        return False
        



#usr = input("Enter the word to test: ").lower()

#palind(usr)


