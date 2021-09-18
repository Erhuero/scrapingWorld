message = 'Python language is awesome'
count = {} #initialisation d'un dictionnaire

for c in message :
	count.setdefault(c, 0)#dans le dictionnaire count initialiser le nombre caracteres, s'assure que la cle est dans le dictionnaire sinon renvoie 0
	count[c] = count[c] + 1
print(count)