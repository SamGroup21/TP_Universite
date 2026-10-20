def chiffre_cesar_moins_deux(texte):
    resultat = ""
    
    for caractere in texte:
        # Traitement des lettres majuscules
        if caractere.isupper():
            # ord('A') vaut 65. On applique le décalage de -2 avec un modulo 26
            nouveau_car = chr((ord(caractere) - 65 - 2) % 26 + 65)
            resultat += nouveau_car
            
        # Traitement des lettres minuscules
        elif caractere.islower():
            # ord('a') vaut 97. On applique le décalage de -2 avec un modulo 26
            nouveau_car = chr((ord(caractere) - 97 - 2) % 26 + 97)
            resultat += nouveau_car
            
        # Si ce n'est pas une lettre (espace, point, etc.), on ne change rien
        else:
            resultat += caractere
            
    return resultat

# --- Exemple d'utilisation ---
texte_original = "Bonjour, j'apprends Python !"
texte_crypte = chiffre_cesar_moins_deux(texte_original)

print("Texte original :", texte_original)
print("Texte crypté   :", texte_crypte)
# Test avec la lettre 'b' seule pour vérifier
print("Test de la lettre 'b' :", chiffre_cesar_moins_deux("b"))  # Affiche 'z'
