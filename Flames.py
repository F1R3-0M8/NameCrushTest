def Flames(name1, name2):
    nameConcat = name1 + name2

    for carac in nameConcat:
        if nameConcat.count(carac) != 1:
            nameConcat = nameConcat.replace(carac, "")
    
    letterCount = len(nameConcat)
    
    #f friend
    #l love
    #a affection
    #m mariage
    #e enemy
    #s siblings

    modulo = letterCount % 6
    # while modulo > 5:
    #     modulo = modulo % 6
    #Ce modulo ne sert à rien car le reste max d'un modulo (X % n) est égale à N-1, ici 6-1 = 5 donc "Dans la bagarre"
    
    switcher= {
    1: "FriendZoné",
    2: "Amoureux ",
    3: "Trop in love l'un pour l'autre",
    4: "Bientot marrié (OULAH!)",
    5: "Dans la bagarre",
    0: "Des frérots"
    }

    return switcher.get(modulo, "Insignifiant l'un pour l'autre")


n1 = input("Ecris ton prénom : ").upper()
n2 = input("Ecris le nom de ton crush : ").upper()

print(f"Vous êtes : {Flames(n1, n2)}")

