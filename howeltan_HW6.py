##My import
import random 

##Function

##6.28

def translate(phrase):
    
##I was mainly use to the problems having examples of inputs and outputs,
##so I compiled a list of things I thought were some things people would want translated
    
    german_words = {"hello": "hallo", "goodbye": "auf wiedersehen", "how are you": "wie geht es ihnen", "dog": "hund", "cat": "katze", "where is the bathroom": "wo is die toilette"}


##In here I tried using phrase.lower() but it wouldn't work. Thoughts?
    if phrase in german_words:

        print(phrase, "in german is ", german_words[phrase], "!")

    else:

       print("____")




##6.33

def diceprob(roll):

##Counters for both the total amount of rolls as well as the amount of times
##our chosen number appears

    total_rolls = 0
    num_counter = 0


##This took forever but I think my main issue was that I was taking a range of 2 to 13 instead of realizing
## I should be considering two pairs of dice. If I could've done it with one random.randrange then I would love to know.

    while num_counter < 100:

        dice_roll = random.randrange(1, 7) + random.randrange(1, 7)
        total_rolls = total_rolls + 1

        if dice_roll == roll:
            num_counter = num_counter + 1


    print("It took ", total_rolls, "to get 100 rolls of ", roll, ".")
        
    
    
    
    
    







##Main


##6.28

##Again, I didn't really know if there was a certain way you wanted this to look,
##so I did what I thought was sufficient

       
print('Welcome to my English to German translator!')

while True:
    phrase = input('Please enter a phrase you would like translated (or "stop"): ')

    if phrase == 'stop':
        break
    else:
        translate(phrase)


##6.33
while True:

    diceprob(int(input( )))

##I wasn't sure on how to stop this program, as it only takes integers.
##So sadly the only way to stop it is to kill it :( RIP diceprob he was so young

##This is what I believed to be right. Feedback?
##    if diceprob == 'stop':
##        break




