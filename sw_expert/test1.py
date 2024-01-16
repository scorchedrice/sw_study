alpha = input()
list_alpha = []
ord_alpha = []
for i in range(0, len(alpha)):
	list_alpha.append((alpha[i]))
    ord_alpha.append(list_alpha[i])
    
ord_alpha = ord_alpha - [ord('A')-1]*len(list_alpha)
print(ord_alpha)