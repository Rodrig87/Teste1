string = input("Digite uma string para inverter: ")

string_inv = ""

for i in range(len(string) - 1, -1, -1):
    string_inv += string[i]

print("String original:", string)
print("String invertida:", string_inv)
