def cesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        crypted_text += chr((ord(char) + key)%1_114_112) #permet de chiffre malgé une clé audessus du nombre d'élément dans la table ascii
    return crypted_text
print(cesar_cipher("chocolat", 531200000000))#53120 dans la table asci

#exadecimal base 16

def cesar_uncipher(crypted_message,key):
    return cesar_cipher(crypted_message, -key)

messge ="chocolat"
crypted_message = cesar_cipher(message,5212000)
initial_message = #on verrifie un bouleen avec True pour voir que le message se reverse bien
	