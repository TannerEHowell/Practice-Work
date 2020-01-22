##Functions

##5.39
def exclamation(wstring):
    n_string = list(wstring.lower())
    phrase = ''

    for i in n_string:

        if i in 'aeiouAEIOU':
            i = i*4
        else:
            i = i*1
        phrase = phrase + i
        
    print(phrase + '!')

##5.43
##I really didn't know what to do here. I had gone to some people who were well versed in python but I really couldnt find any solution
##I know this takes my grade for this assignment down but I am unsure of what to do here.
##If in the feedback, if you could show me what the answer was that would be great, it's okay if you can'
##Sorry for leaving this unfinished, I'll do better next time!!

##def evenrow(nums):
##    my_sum = 0
##    for i in nums:
##        my_sum += sum(i)
##        if my_sum % 2 == 0:
##            return True
##        elif my_sum %2 ==1:
##            return False
##





##Main

##5.39
wstring = input('Please enter a word: ')
exclamation(wstring)

##5.43
##evenrow([[1,3], [2,4], [0,6]])

##other input to test is [[1,3], [3,4], [0,5]]
##and ([[1,3,2], [3, 4, 7], [0, 5, 2]])
