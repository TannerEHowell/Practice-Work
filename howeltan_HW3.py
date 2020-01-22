##Function

def distance(time):
    meters = 340.29 * time
    kilometers = meters * .001
    return (kilometers)
    
    




##Main
time = eval(input('Please input the seconds between the flash and the thunder: ' ))
print('Wow! The lightning strike was approximately ' , distance(time), 'kilometers away!')

##I wanted to input some more dialogue into the  statement as to make it more understandable
