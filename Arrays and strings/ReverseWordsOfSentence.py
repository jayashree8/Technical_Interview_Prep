'''
Given a sentence, reverse the words of the sentence.

For example,"i live in a house" becomes "house a in live i"
'''
def reverseSent(s):
    new = ""
    j = len(s)-1
    for i in range(len(s)-1,0,-1):
        if s[i] == " ":
            if len(new) > 0:
                new = new + " "
            new = new + s[i+1:j+1]  
            j = i - 1
    new = new + " " + s[0:j+1]
    return new


s = "i live in a house"
print(s)
print(reverseSent(s))

s = ""
print(s)
print(reverseSent(s))

s = "a bat is"
print(s)
print(reverseSent(s))

s = " "
print(s)
print(reverseSent(s))