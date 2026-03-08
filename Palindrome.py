def Palindrome(text):
    txt = text[::-1]
    if txt == text:
     return True
    else:
     return False

Pal = Palindrome('anitalavalatina')
print(Pal)