# Criando uma lista com diversos elementos
minha_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Usando o método append() para adicionar um elemento ao final da lista
minha_lista.append(7)
print("Lista após adicionar 7:", minha_lista)

# Usando o método insert() para inserir um elemento em uma posição específica
minha_lista.insert(2, 8)  # Insere 8 na posição 2
print("Lista após inserir 8 na posição 2:", minha_lista)

# Usando o método remove() para remover o primeiro elemento com o valor especificado
minha_lista.remove(5)  # Remove o primeiro 5 encontrado
print("Lista após remover o primeiro 5:", minha_lista)

# Usando o método pop() para remover e retornar o elemento em uma posição específica
elemento_removido = minha_lista.pop(3)  # Remove e retorna o elemento na posição 3
print("Elemento removido:", elemento_removido)
print("Lista após remover o elemento na posição 3:", minha_lista)

# Usando o método sort() para ordenar a lista em ordem crescente
minha_lista.sort()
print("Lista ordenada:", minha_lista)

# Usando o método reverse() para inverter a ordem da lista
minha_lista.reverse()
print("Lista invertida:", minha_lista)

# Usando o método index() para encontrar o índice do primeiro elemento com o valor especificado
indice_do_3 = minha_lista.index(3)
print("O índice do primeiro 3 é:", indice_do_3)

# Usando o método count() para contar o número de ocorrências de um elemento
numero_de_5 = minha_lista.count(5)
print("O número de 5s na lista é:", numero_de_5)
