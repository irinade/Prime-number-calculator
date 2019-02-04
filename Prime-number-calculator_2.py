nb_premier = []

def prime_number(born):

	born = int(born)
	j = True
	for i in range (2, born):
		if born%i == 0 :
			j = False
			break
	return(j)

born = input("born :")
born = int(born)
a = list(range(2, born))
for k in a:
	if prime_number(k) == True:
		nb_premier.append(k)

print(nb_premier)