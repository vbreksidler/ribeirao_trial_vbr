## 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def check_letter(string):
    count = string.lower().count('a')

    if count > 0:
        print(f"A letra 'a' aparece {count} na palavra.")
    else:
        print("A letra 'a' não aparece na palavra.")

def main():
    string = input("Informe uma palavra: ")
    check_letter(string)

if __name__ == "__main__":
    main()
