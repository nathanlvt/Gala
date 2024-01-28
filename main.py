def lire(nom_fichier):
    nomPrenom = []
    with open(nom_fichier) as donnees:
        for ligne in donnees:
            ligne = ligne.strip("\n")
            L = []
            if nom_fichier == "inscription_gala.csv":
                ligne = ligne.split(";")
                L.append(ligne[3].strip('" '))
                L.append(ligne[4].strip('" '))
                nomPrenom.append(L)
            elif nom_fichier == "liste_cotisants.csv":
                ligne = ligne.split(",")
                L.append(ligne[0].strip('" '))
                L.append(ligne[1].strip('" '))
                nomPrenom.append(L)
    return nomPrenom[1:]

def IsCotisant(L1, L2):
    nom1, prenom1 = L1
    nom2, prenom2 = L2
    return (nom1.lower() == nom2.lower()) and (prenom1.lower() == prenom2.lower())

def main():
    L = []
    L_gala = lire("inscription_gala.csv")
    L_cotisant = lire("liste_cotisants.csv")

    for i in range(len(L_gala)):
        e = False
        for j in range(len(L_cotisant)):  
            if IsCotisant(L_gala[i], L_cotisant[j]):
                e = True
        if not e:
            L.append(L_gala[i])
    if L == []:
        print("Aucun menteur trouvé.")
    else:
        with open("liste_menteur.txt", "w") as f:
            for i in range(len(L)):
                f.write(L[i][0] + " " + L[i][1] + "\n")

# print(main())

print(lire("inscription_gala.csv"))

# print(IsCotisant(["Bouvié", "Pierre"], ["Bouvié", "Pierre"]))
chaine = "Élève"
chaine_lower = chaine.casefold()

print(chaine_lower)
