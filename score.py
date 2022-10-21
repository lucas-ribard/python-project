#format joueur : "XXXXX"   XX victoires  XX draw  XX défaite ?
#nom et victoire au minimum

def actualiserScore():
    print("placeholder")
    #nb_ligne=readline(joueur)
    #readline(nb_ligne)
    #split infos
    #actualiser info
    #remettre dans 1 string
    #write a la bonne ligne


#affiche les scores
def checkScore ():
    file_score=open("ressources/Score.txt","r")
    print("\n",file_score.read())

def changeScore():
    file_score = open("ressources/Score.txt", "r")
    #temp
    joueur="test"
    victoires=10
    entrée=[joueur,victoires]

    if joueur in file_score:
        actualiserScore()
    else:
        print("placeholder")
        #creer utilisateur avec score

    file_score.write()