ligne1=['_ ','_ ','_ ']
ligne2=['_ ','_ ','_ ']
ligne3=['_ ','_ ','_ ']

def affichage():
    # affiche le terrain
    print("   [1][2][3]")
    print("[1]", ligne1[0], ligne1[1], ligne1[2])
    print("[2]", ligne2[0], ligne2[1], ligne2[2])
    print("[3]", ligne3[0], ligne3[1], ligne3[2])

player1="jackie"
player2="michel"
tempo=0
affichage()
# déroulement d'un tour
def tour(tempo):
    if tempo == 0 :
        joueur = player1
    elif tempo == 1:
        joueur = player2

    print("tour de ",joueur)
    if joueur == player1:
        token = "X "
    elif joueur == player2:
        token = "O "
    colone = int(input("colone : ")) - 1
    ligne = int(input("ligne : "))

    if ligne == 1:
        ligne1[colone] = token
        print("test")
    elif ligne == 2:
        ligne2[colone] = token
        print("test")
    elif ligne == 3:
        ligne3[colone] = token
    else:
        print("pas la bonne ligne ducon")

    if tempo == 0:
        tempo=1
    else :
        tempo=0
    return tempo,joueur

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

while '_ ' in ligne1 and '_ ' in ligne2 and '_ ' in ligne3:
    tempo,joueur =tour(tempo)
    victoire=gagné()
    if victoire==1:
        affichage()
        print("le joueur",joueur,"a gagné" )
        break
    affichage()

