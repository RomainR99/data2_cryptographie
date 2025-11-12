import string

def cesar_cipher(text, key):
    crypted_text = ""
    for char in text:
        crypted_text += chr((ord(char) + key)%1_114_112) #permet de chiffre malgé une clé audessus du nombre d'élément dans la table ascii
    return crypted_text
print(cesar_cipher("chocolat", 531200000000))#53120 dans la table asci

#le souci c'est une chaine de caractere donc immuable avec toute une copie de chaine de caracrter
#donc on fait une liste qui prendra moins de palace.

def cesar_cipher(text, key):
    list_of_crypted_chars = []
    for char in text:
        list_of_crypted_chars.append(chr((ord(char) + key) % 1_114_112))
    crypted_text ="".join(list_of_crypted_chars) #"" c'est la jointure ici rien , on peut mettre " "
    #permet de chiffre malgé une clé audessus du nombre d'élément dans la table ascii
    return crypted_text
print(cesar_cipher("chocolat", 531200000000))

#Refactorer

def cesar_cipher(text, key):
    if ...
    return "".join([chr((ord(chr)+key)%1_114_112)])



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
            print(""*20)

#Chiffrement de Vigenere	
# def convert_password_to_list_of_keys(password):
 #   return [ord(char)for char in password]
#print(convert_password_to_list_of_keys("Azerty12345"))
def vigenere_cipher(text,password):
    list_of_keys = [ord(char)for char in password]
    crypted_text = []
    for index, char in enumerate(text): #ennumerate indique"tuple", index du charatere + charactere
        current_key = list_of_keys[index %len(list_of_keys)]
        #on chiffre à l'aide de la current_key et je le rajoute à ma liste
        crypted_text.append(cesar_cipher(char,current_key))
    return "".join(crypted_text) #il faut join crypted_text
    

def vigenere_uncipher(text,password):
    return vigenere_cipher(text, -password)

            
           

