import random

#
with open('ressources/dico_france.txt', 'rt', encoding='latin1') as dico:
    rd_nb = random.randint(0, 22740)

    # recup le mot a la ligne selectionné
    all_lines = dico.readlines()
dico.close()
#recup le mots en fonction de la position dans le txt
mot_choisis=all_lines[rd_nb]
print(mot_choisis)


mot_choisis = mot_choisis.rstrip()

##############################################

mot_devine = "-" * len(mot_choisis)
print(mot_devine)
lettres_deja_proposees=[]
vie=10
while mot_devine != mot_choisis and vie !=0:
    print("il vous reste : ",vie," vies")
    print("Vous avez proposée : ",lettres_deja_proposees)
    lettre = input("\nEntrez une lettre : ")

    if lettre not in mot_choisis and lettre not in lettres_deja_proposees:
        vie -= 1

    if lettre not in lettres_deja_proposees:
        lettres_deja_proposees += [lettre]

    elif lettre in lettres_deja_proposees:
        print("\nla lettre \"",lettre,"\" à déja été proposé !\nAucune vie ne vous à été déduit\n")


    for i in range(len(mot_choisis)):
        if lettre == mot_choisis[i]:
            mot_devine = mot_devine[:i] + lettre + mot_devine[i + 1:]
    print(mot_devine)

if vie ==0:
    print("\nGame Over !\n")
if mot_choisis == mot_devine:
    print('\nBravo ! Le mot', mot_choisis, 'a été trouvé\n')
