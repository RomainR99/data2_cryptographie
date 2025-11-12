import string

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
#initial_message = #on verrifie un bouleen avec True pour voir que le message se reverse bien

def hack_cesar_cipher(crypted_message):
    for possible_key in range(0,1_114_112) #au lieu de mettre 1114112 plus visible
        possible_uncription = cesar_uncipher(crypted_message, possible_key)
        if possible_uncryption[0] in string.printabal: #taille de la table string.principal contient 100 élément au lieu de 1_114_112 donc plus rapide à décoder
            print(possible_key)
            print(cesar_unicipher(crypted_message, possible_key))#donne tous les décodage possible
            print(_""*20)
	