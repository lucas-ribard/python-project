from score import checkScore

tempo=0

# des couleurs pour faire jolie
# syntaxe ( print( " texte " + bcolors.RESET) )
class bcolors:
    WIN = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


# fonction qui affiche la grille de jeux
def affichage():
    # affiche le terrainbcolors.WIN +
    print("\n   [1][2][3]       <    Colonne")
    print("[1]", ligne1[0], ligne1[1], ligne1[2])
    print("[2]", ligne2[0], ligne2[1], ligne2[2])
    print("[3]", ligne3[0], ligne3[1], ligne3[2])
    print("\n^")
    print("ligne")
# Fonction qui dit qui joue
def tempocontrol(tempo):
    if tempo == 0:
        tempo=1
    elif tempo==1:
        tempo=0
    return tempo

# fonction de déroulement d'un tour
def tour(tempo):
    global token, joueur

    # selon valeur de tempo, c'est le tour du joueur 1 ou 2
    if tempo == 0 :
        joueur = joueur1
    elif tempo == 1:
        joueur = joueur2

    # annonce qui doit jouer
    print(bcolors.WARNING +"\ntour de ",joueur,"\n"+bcolors.RESET)

    # selon le joueur leur token sera soit la croix, soit le rond
    if joueur == joueur1:
        token = "X "
    elif joueur == joueur2:
        token = "O "
    # demande la ligne et la colone sur laquelle entrer le token
    colone = int(input("colone : ")) - 1 # moins 1 pour alligner les coordonée x et y sur la grille  (sinon X =0 ,1 ,2  et  y = 1, 2 et 3)
    ligne = int(input("ligne : "))

    if colone <= 2:
        # Logique de positionnement sur la grille
        if ligne == 1:
            if ligne1[colone] == "_ ":
                ligne1[colone] = token
                tempo = tempocontrol(tempo)
            else:
                print(bcolors.FAIL +"case déja posé"+bcolors.RESET)

        elif ligne == 2:
            if ligne2[colone] == "_ ":
                ligne2[colone] = token
                tempo=tempocontrol(tempo)
            else:
                print(bcolors.FAIL +"case déja posé"+bcolors.RESET)
        elif ligne == 3:
            if ligne3[colone] == "_ ":
                ligne3[colone] = token
                tempo = tempocontrol(tempo)
            else:
                print(bcolors.FAIL +"case déja posé"+bcolors.RESET)

        else:
            print(bcolors.FAIL +"pas la bonne ligne"+bcolors.RESET)
    else:
        print(bcolors.FAIL +"pas la bonne colonne"+bcolors.RESET)

    return tempo,joueur

#Fonction de condition de victoire
def gagné():
    if (ligne1[0] == ligne1[1]) and (ligne1[1] == ligne1[2]) and (ligne1[0] != "_ "):
        return 1
    if (ligne2[0] == ligne2[1]) and (ligne2[1] == ligne2[2]) and (ligne2[0] != "_ "):
        return 1
    if (ligne3[0] == ligne3[1]) and (ligne3[1] == ligne3[2]) and (ligne3[0] != "_ "):
        return 1
    if (ligne1[0] == ligne2[1]) and (ligne2[1] == ligne3[2]) and (ligne1[0] != "_ "):
        return 1
    if (ligne3[0] == ligne2[1]) and (ligne2[1] == ligne1[2]) and (ligne1[2] != "_ "):
        return 1
    if (ligne1[0] == ligne2[0]) and (ligne2[0] == ligne3[0]) and (ligne3[0] != "_ "):
        return 1
    if (ligne1[1] == ligne2[1]) and (ligne2[1] == ligne3[1]) and (ligne1[1] != "_ "):
        return 1
    if (ligne1[2] == ligne2[2]) and (ligne2[2] == ligne3[2]) and (ligne1[2] != "_ "):
        return 1


#menu de lancement
print("Bonjour voulez vous jouer ou voir les scores")
menu=0
#boucle meni
while menu ==0:
    choix = input("jouer   scores\n")
    if choix == "jouer" or choix == "Jouer":
        joueur1=input("Username 1 Croix :")
        joueur2=input("Username 2 Rond  :")
        menu=1
    elif choix == "scores" or choix == "Scores" or choix == "score" or choix == "Score":
        checkScore()
        menu=1
        exit()
    else:
        print (bcolors.FAIL +choix, "n'est pas une option valable"+bcolors.RESET)

#init du tableau
ligne1=['_ ','_ ','_ ']
ligne2=['_ ','_ ','_ ']
ligne3=['_ ','_ ','_ ']


affichage()

#lance la partie
while '_ ' in ligne1  or  '_ ' in ligne2  or  '_ ' in ligne3:
    tempo,joueur =tour(tempo)
    victoire=gagné()
    if victoire==1:
        affichage()
        print(bcolors.WIN +"\nle joueur",joueur,"a gagné" +bcolors.RESET)
        break
    affichage()

if victoire !=1:
    print(bcolors.WARNING +"EGALITE"+bcolors.RESET)