##Functions

##4.23
##I wasn't sure if I was to write return(avg) as the problem instructions said
##"Your function should return the average length of a word in the sentence"
##but returning didn't work so I decided to go with a print statement
def average():
    sentence = input('Enter a sentence: ')
    new_sen = list(sentence)
    let = 0
    space = 0
    for i in sentence:
        if i != ' ':
            let = let + 1
        if i == ' ':
            space = space + 1
    avg = let / (space + 1)
    print(avg)        
            

##4.25
##I tried to do "for letter in new_phrase" and "if 'a' in new_phrase:" initially.
##I'm wondering why that wouldn't work and would appreciate feedback on that.
##I'm guessing it's because I set it as a list so it would make sense to do the "i in new_phrase" statement.

def vowelCount(phrase):
    new_phrase = list(phrase.lower())
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    print(new_phrase)
    for i in new_phrase:
        if i == 'a':
            a_count = a_count + 1
        elif i == 'e':
            e_count = e_count + 1
        elif i == 'i':
            i_count = i_count + 1
        elif i == 'o':
            o_count = o_count + 1
        elif i == 'u':
            u_count = u_count + 1
    print('a, e, i, o, and u appear, respectively, ', a_count,',', e_count,',', i_count,',', o_count,',', u_count, 'times. ')






##Main
##4.23
average()



##4.25
phrase = input('Enter a phrase: ')
vowelCount(phrase)

##hey is works thats gotta mean SOMETHING right?? 
