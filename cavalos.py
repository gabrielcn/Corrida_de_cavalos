# Define o número de cavalos e cria a lista de cavalos
num_horses = 3
horses = []

# Classe para representar um cavalo
class Horse:
  def __init__(self, name, position, speed):
    self.name = name
    self.position = position
    self.speed = speed

# Função para simular a corrida
def simulate_race():
  while True:
    # Para cada cavalo, atualiza sua posição baseado em sua velocidade
    for horse in horses:
      horse.position += horse.speed

    # Verifica se algum cavalo cruzou a linha de chegada
    for horse in horses:
      if horse.position >= 100:
        print(horse.name + " é o vencedor!")
        return

# Inicializa os cavalos e adiciona à lista
horses.append(Horse("Cavalo Vermelho", 0, 5))
horses.append(Horse("Cavalo Preto", 0, 3))
horses.append(Horse("Cavalo Branco", 0, 1))

# Inicia a simulação da corrida
simulate_race()
