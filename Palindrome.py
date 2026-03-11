# This function returns True if the input word
# is a palindrome, False otherwise

def Palindrome(text):
    txt = text[::-1]
    if txt == text:
     return True
    else:
     return False

Pal = Palindrome('anitalavalatina')
print(Pal)