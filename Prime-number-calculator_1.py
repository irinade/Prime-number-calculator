a = int(input("Please enter the maximum number value : "))
non_premier = [i for i in range (0,a) for n in range(2,a) if n!=i and i%n==0]
o = list(range(2, a))

nb_premier = list(set(o).difference(set(non_premier)))
nb_premier.sort()

print(nb_premier)
