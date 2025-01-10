#Reverter string sem usar funções prontas

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

# Teste
texto = input("Informe a string: ")
print("String invertida:", reverse_string(texto))
