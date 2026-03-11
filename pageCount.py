# This function calculates the shortest page flip of a book
# that is, which way is the fastest to reach a desired page
# the front of the book or the back
# p is the desired page and n is the total number of pages in
# the book
# |0|1| -> |2|3| -> |4|5| ...

def pageCount(n, p):
    countLow = p//2
    countHigh = n//2 - countLow
    return print(min(countLow, countHigh))
        
pageCount(67,23)
