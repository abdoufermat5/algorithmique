def tri_insertion(tab):
	n = len(tab)
	
	for i in range(1, n):
		current = tab[i]
		j = i - 1
		while j >= 0 and tab[j] > current:
			tab[j + 1] = tab[j]
			j -= 1
		tab[j + 1] = current
	return tab