
import time

def countdown(timer):
    while timer > 0:
        print(timer)
        time.sleep(1)  # espera por 1 segundo
        timer -= 1
    print("Tempo esgotado!")

def main():
    try:
        timer = int(input("Digite o tempo em segundos para a contagem regressiva: "))
        countdown(timer)
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()