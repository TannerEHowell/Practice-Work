##Functions
def avg(all_temps):
    return sum(all_temp) / len(all_temp)

def offset(difference):
    normal = 32
    if avg(all_temp) > normal:
        print('This was', round(avg(all_temp) - 32, 2) , ' above normal.')
    elif avg(all_temp) == normal:
        print('This is the normal temperature.')
    elif avg(all_temp) < normal:
        print('This was', round(avg(all_temp) - 32, 2),  ' below normal.')
##To test, I threw in some extra numbers and it worked!

def compare(ranges):
    below = 0
    equal = 0
    above = 0
    norm_min = 24
    norm_max = 40
    for num in all_temp:
        if num < norm_min:
            below = below +1
        elif num > 40:
            above = above + 1
        else:
            equal = equal + 1
    print(below ,'readings in this list are below the average')
    print(equal , 'readings in this list are equal to the average')
    print(above , 'readings in this list are above the average')
    return(ranges)
##I decided to make variables for this function, I don't know however if my norm_min and norm_max variables are
##needed, however I wasn't quite sure on what else to do as I tried doing normal = range(24, 40) and yet that didn't work out.

def frequency (city):
    first = range(10, 19)
    sec = range(20, 29)
    third = range(30, 39)
    frth = range(40, 49)
    ffth = range(50, 59)
    sxth = range(60, 65)
    fn = 0
    sn = 0
    tn = 0
    ftn = 0
    ffn = 0
    xn = 0
    for num in city:
        if num in first:
            fn = fn + 1
        if num in sec:
            sn = sn + 1
        if num in third:
            tn = tn + 1
        if num in frth:
            ftn = ftn + 1
        if num in ffth:
            ffn = ffn + 1
        if num in sxth:
            xn = xn + 1
    print('10 - 19F : ', fn *'*')
    print('20 - 29F : ', sn *'*')
    print('30 - 39F : ', tn *'*')
    print('40 - 49F : ', ftn *'*')
    print('50 - 59F : ', ffn *'*')
    print('60 - 65F : ', xn *'*')
##I don't know if this was the exact way to do it HOWEVER since it worked I'm pretty stoked (and surprised)
##I find it strange that I could use range in this function but yet I wasn't able to make it work in the compare function, feedback?



##Main
indy_temps = [27, 24, 64, 48, 34, 23, 61, 19, 17, 53, 19, 44, 44, 28, 10, 55, 31, 36, 32, 52]
bloomington_temps = [64, 56, 30, 26, 20, 46, 13, 41, 57, 10, 32, 43, 53, 23, 59, 41, 18, 44, 24, 20]
lafayette_temps = [55, 56, 13, 49, 30, 36, 16, 26, 58, 17, 53, 57, 14, 57, 60, 15, 54, 28, 56, 10]
evansville_temps = [44, 34, 36, 34, 38, 57, 63, 21, 59, 43, 41, 58, 51, 43, 44, 27, 12, 63, 19, 21]
fort_wayne_temps = [19, 61, 19, 53, 63, 32, 61, 60, 43, 28, 25, 61, 14, 57, 12, 34, 52, 17, 29, 11]

all_temp = indy_temps + bloomington_temps + lafayette_temps + evansville_temps + fort_wayne_temps

##Section 1
print(all_temp)
print('The average of all temperatures is: ', avg(all_temp), 'F.')
offset(all_temp)
print()


## Section 2
compare(all_temp)
print()

##Section 3
print('Temperature Chart for Bloomington IN')
print('-' * 50)
frequency(bloomington_temps)
print('-' * 50)
print()

print('Temperature Chart for Ft Wayne IN')
print('-' * 50)
frequency(fort_wayne_temps)
print('-' * 50)
print()

##Always looking forward to feedback, thanks!!
