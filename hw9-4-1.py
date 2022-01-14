# Author: ATN 1/14/22

def smash(words):
    for word in words:
        if(word == ' '):
            words.remove(word)
    return words

print(smash(['these', ' ', 'are', ' ', 'words']))
