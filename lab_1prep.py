##functions
def avg(big_boi):
    return sum(big_boi) / len(big_boi)

def compare(fuck):
    below = 0
    equal = 0
    above = 0
    average = sum(big_boi) / len(big_boi)
    for num in big_boi:
        if num < avg(big_boi):
            below = below +1
        elif num == avg(big_boi):
            equal = equal + 1
        elif num > avg(big_boi):
            above = above + 1
    print(below ,'numbers in this list are below the average')
    print(equal , 'numbers in this list are equal to the average')
    print(above , 'numbers in this list are above the average')
    return(fuck)

def starpwr(cute):
    big_boi.sort()
    for num in big_boi:
        if num < avg(big_boi):
           num = (num * '*')
           print(num)
    print(big_boi)
    return(cute)
            



##main
first = [3 , 45 , 67 , 23 , 13 , 89 , 56 , 16 , 52]
sec = [2 , 34 , 12 , 54 , 68 , 72 , 69 , 10 , 8]


##add lists together and finding the average
big_boi = first + sec
print(big_boi)
print(avg(big_boi))

##how many times a numbers in the list are above, below, or equal to the average
compare(big_boi)

##changing into stars
starpwr(big_boi)

