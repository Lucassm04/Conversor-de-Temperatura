"""Conversor de Temperatura"""

def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_para_kelvin(f):
    return celsius_para_kelvin (fahrenheit_para_celsius(f))

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return celsius_para_fahrenheit(kelvin_para_celsius(k))

def exibir_menu():
    print('\n=== Conversor de Temperatura ===')
    print('1 - Celsius para Fahrenheit e Kelvin')
    print('2 - Fahrenheit para Celsius e Kelvin')
    print('3 - Kelvin para Fahrenheit e Celsius')
    print('0 - Sair')

def ler_temperatura(unidade):
    while True:
        try:
            return float(input(f'Digite a temperatura em {unidade}: '))
        except ValueError:
            print('Valor inválido. Digite um número (ex: 30 ou 25.5).')

def main():
    while True:
        exibir_menu()
        opcao = input ('Escolha uma opção: ').strip()

        if opcao == '1':
            c = ler_temperatura('Celsius')
            print(f'{c}ºC = {celsius_para_fahrenheit(c):.2f}ºF')
            print(f'{c}ºC = {celsius_para_kelvin(c):.2f}K')

        elif opcao == '2':
            f = ler_temperatura('Fahrenheit')
            print(f'{f}ºF = {fahrenheit_para_celsius(f):.2f}ºC')
            print(f'{f}ºF = {fahrenheit_para_kelvin(f):.2f}K')

        elif opcao == '3':
            k = ler_temperatura('Kelvin')
            print(f'{k}K = {kelvin_para_celsius(k):.2f}ºC')
            print(f'{k}K = {kelvin_para_fahrenheit(k):.2f}ºF')

        elif opcao == '0':
            print('Até mais!')
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()


