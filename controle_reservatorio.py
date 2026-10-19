
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=False)

# Lista com as situações do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que mostra a cor de cada nível
def definir_cor(nivel):
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE
    ]

    return cores[nivel - 1]


# Funço que mostra a situação do reservatório
def mostrar_nivel(nivel):
    if 1 <= nivel <= 5:
        situacao = niveis[nivel - 1]
        cor = definir_cor(nivel)

        print(cor + f"Nível {nivel}: {situacao}"
              + Style.RESET_ALL)
    else:
        print("Nível inválido!")


# Simulação dos cinco níveis do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===")

for nivel in range(1, 6):
    mostrar_nivel(nivel)

print("=== FIM DO MONITORAMENTO ===")
