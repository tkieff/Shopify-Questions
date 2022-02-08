import numpy as np

#thanks for choosing a message without the letter J
key = "ADA LOVELACE"

message = "LVFPPNMQDOORAYIVKHPGPBTPKHNZFOAY"

alphabet = ['A','B','C','D','E','F','G',
            'H','I','K','L','M','N',
            'O','P','Q','R','S','T','U',
            'V','W','X','Y','Z']

#create the cipher table using the key and the alphabet
cipher = []
for i in key:
    if i in alphabet:
        #add the characters from the key and remove them from our alphabet
        cipher.append(i)
        alphabet.remove(i)
#add the remainder to the cipher
cipher.extend(alphabet)
#numpy is awesome
cipher = np.reshape(cipher, (5,5))

#seperate the message into pairs
pairs = [message[2*i:2*i+2] for i in range(int(len(message)/2))]

decrypted_message = []

for pair in pairs:

    loc1 = np.where(cipher == pair[0])
    loc2 = np.where(cipher == pair[1])
    #np.where returns a 2d numpy array so I need [][] to get the values
    #surely there's a better way but it's not worth
    #if you're in the same row shift the columns left
    #left because you're decoding, this took me an embarassingly long time to figure

    if loc1[0] == loc2[0]:

        loc1[1][0] -= 1
        loc2[1][0] -= 1

    #if you're in the same column shift up the rows not down!
    elif loc1[1] == loc2[1]:

        loc1[0][0] -= 1
        loc2[0][0] -= 1
    #pick the corners of the box formed by the pair
    #trial and error is good to figure out how to map the corners to the pair of letters

    else:
        loc1[1][0], loc2[1][0] = loc2[1][0], loc1[1][0]


    #this handles the wrapping of the indices
    loc1 = np.where(loc1 == np.array(-1), np.array(4),loc1)

    loc2 = np.where(loc2 == np.array(-1), np.array(4),loc2)

    #append it to the decrypted message
    decrypted_message.append(cipher[loc1[0][0]][loc1[1][0]])
    decrypted_message.append(cipher[loc2[0][0]][loc2[1][0]])




print(cipher)
#turn list into string
msg = ''
for char in decrypted_message:

    msg += char

print(msg)




