import time
from pyscript import document


#Variables
decided = False
validCode = False
encoding = bool

#Functions
def makeEncrypt(event):
    encoding = True
    main()

def makeDecrypt(event):
    encoding = False
    main()

def encrypt(text, key): #Function takes 'text' and shifts it by 'shift'
    shifted = ""
    keyNumberPosition = 0 #Which value of list is going to be selcted

    shift = key[keyNumberPosition] #How much the value of the letter will be shifted
    for i in text: #Iterates through the characters in 'text' and values in 'key'
        if keyNumberPosition > (len(key) - 1):
            keyNumberPosition -= len(key)
        shift = key[keyNumberPosition]
        if not i.isalpha(): #If selected character isn't a letter, leave it alone
            addedCharacter = i
        elif i.isalpha(): #If selected character is a letter, increase it's value by 'shift'
            shiftedCharacter = ord(i) + shift
            if shiftedCharacter > ord("z"): #If shifted character's value exceeds that of z, decrease it to a
                shiftedCharacter -= 26
            addedCharacter = chr(shiftedCharacter)
            keyNumberPosition += 1

        shifted += addedCharacter      
        outputDiv = document.querySelector("#outputMessage")
        outputDiv.innerText = shifted
        time.sleep(0.2)


    return shifted

def decrypt(text, key): #Function takes 'text' and shifts it by 'shift'
    shifted = ""
    keyNumberPosition = 0 #Which value of list is going to be selcted

    shift = key[keyNumberPosition] #How much the value of the letter will be shifted
    for i in text: #iterates through the characters in 'text' and values in 'key'
        if keyNumberPosition > (len(key) - 1):
            keyNumberPosition -= len(key)
        shift = key[keyNumberPosition]
        if not i.isalpha(): #If selected character isn't a letter, leave it alone
            addedCharacter = i
        elif i.isalpha(): #If selected character is a letter, increase it's value by 'shift'
            shiftedCharacter = ord(i) - shift
            if shiftedCharacter < ord("a"): #If shifted character's value exceeds that of z, decrease it to a
                shiftedCharacter += 26
            addedCharacter = chr(shiftedCharacter)
            keyNumberPosition += 1

        shifted += addedCharacter
        outputDiv = document.querySelector("#outputMessage")
        outputDiv.innerText = shifted
        time.sleep(0.2)

    return shifted

def main():
    text = document.querySelector("#userText")
    userText = str.lower(text.value)

    key = document.querySelector("#userKey")
    codeWord = str.lower(key.value)

    #Convert userKey into a list
    userKey = []
    for i in codeWord: #Appends values of each letter in code word to a list
        letterValue = ord(i) - 96
        userKey.append(letterValue)

    stringKey = ""
    for i in userKey:
        stringKey += str(i)
        stringKey += ", "
    stringKey = stringKey.rstrip(stringKey[-1])
    stringKey = stringKey.rstrip(stringKey[-1])


    #Running the functions
    if encoding:
            newText = encrypt(userText, userKey)
    if not encoding:
            newText = decrypt(userText, userKey)

    confirm = f"Message: {userText}\nCode word: {codeWord}\nValues: {stringKey}"
    confirmationDiv = document.querySelector("#confirmationArea")
    confirmationDiv.innerText = confirm

    outputDiv = document.querySelector("#outputMessage")
    outputDiv.innerText = f"The final output was: {newText}"

