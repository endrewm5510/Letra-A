usuario = input("Informe uma Palavra para verificar o numero de vez(es) que a letra 'a' Aparece: ")
numeroA = usuario.lower().count('a')

if numeroA:
    print(f"A letra 'a' aparece {numeroA} vez(es) em sua Palavra.")
else:
    print("A letra 'a' não está presente em sua Palavra.")