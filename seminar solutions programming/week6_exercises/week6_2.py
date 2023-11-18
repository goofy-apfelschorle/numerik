#week 6 problem 2

#a
print(2**(-24))
print(2**(-53))





#b
def calculate_a():
	return (1-1)+10**(-16)

def calculate_b():
	return 1-(1+10**(-16))

#c
def c(t):
	binary_t=[]
	pow_2 = 0
	for i in range(15):
		t*=2
		pow_2-=1
		if t//1 == t:
			break
	t//=1
	while t>0:
		binary_t = [str(int(t%2))] + binary_t
		t//=2	
	return ''.join(binary_t), pow_2



print(calculate_a())
print(calculate_b())

def tinysum(n):
	return 0.1*n+0.1*n+0.1*n==0.3*n	

if __name__ == "__main__":

	print(c(0.3))
	print(tinysum(5)) #it appears to be true for 5 and false for 2