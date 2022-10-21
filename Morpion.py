print("Bonjour voulez vous jouer ou voir les scores")
menu=0
while menu ==0:
    choix = input("jouer   scores\n")
    if choix == "jouer" or choix == "Jouer":
        joueur1=input("Username 1 Croix :")
        joueur2=input("Username 2 Rond  :")
        menu=1
    elif choix == "scores" or choix == "Scores" or choix == "score" or choix == "Score":
      print("pas encore fait")
      menu=1
    else:
        print (choix, "n'est pas une option valable")