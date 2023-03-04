file = open('Nuevo_documento_de_texto.txt', 'w')
file.write('¡He creado mi primer archivo!\n')
file.close()

file = open('Nuevo_documento_de_texto.txt', 'r+')
file.readline()
file.write('Esta es la segunda vez que escribo.\n')

file.seek(0)
print(file.read())
file.close()