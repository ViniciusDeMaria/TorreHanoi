#Autor: Vinicius Henrique Bonazzoli Fogaça de Maria
#Data da Última atualização: 28/06/2024

casas = ['A', 'B', 'C']

def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Mova o disco de {origem} para {destino}')
    else:
        torres_de_hanoi(n-1, origem, auxiliar, destino)
        print(f'Mova o disco de {origem} para {destino}')
        torres_de_hanoi(n-1, auxiliar, destino, origem)

def main():
  n = int(input("Digite o número de discos (ou 0 para sair): "))
  if n == 0:
    print("Encerrado execução")
    return
  casa = int(input("Informe em qual casa deseja iniciar 1 - A, 2 - B ou 3 - C:"))
  if casa != 1 and casa != 2 and casa != 3:
    print("Casa inválida")
    return
  origem = casas[casa - 1]
  casas.pop(casa - 1)
  destino = int(input(f"Informe em qual casa deseja montar a torre 1- {casas[0]}, 2- {casas[1]}: "))
  if destino != 1 and destino != 2:
    print("Destino inválido")
    return
  if destino == 1:
    destino = casas[0]
    auxiliar = casas[1]
  elif destino == 2:
    destino = casas[1]
    auxiliar = casas[0]

  print(f"Solução para {n} discos:")
  torres_de_hanoi(n, origem, destino, auxiliar)
  print("Encerrado execução")

main()
