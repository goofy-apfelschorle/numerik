import sympy as sp 
import numpy as np
import scipy as sc
import functools as fuc
from math import sqrt

def the_norm_numeric(n):  #numerical version
	H=sc.linalg.hilbert(n)
	#print(H)
	e_n=np.ones((n,1))
	#print(e_n)
	G=np.matmul(H,np.matmul(np.linalg.inv(H),e_n))-e_n
	norm=np.linalg.norm(G,ord=2)
	return norm
	#print(np.matmul(H,e_n))
	#print(np.linalg.inv(H))

def the_norm_exact(n):    #exact version
	e_n=sp.Matrix(np.ones((n,1),dtype=sp.Rational))
	H=np.zeros((n,n), dtype=sp.Rational)
	for i in range(0,n):
		for j in range(0,n):
			H[i][j]=sp.Rational(1,(i+j+1)) #i+1+j+1-1=i+j+1 because indices
	H=sp.Matrix(H)
	I=H.inv()	
	G=H*(I*e_n)-e_n
	J= np.array(G, dtype = sp.Rational).flatten()
	norm=sp.sqrt(fuc.reduce(lambda acc, x: acc+x**2,list(J)))
	print(norm)

	
def condition_number(n):
	H=sc.linalg.hilbert(n)
	I=np.linalg.inv(H)
	#T=np.matrix.transpose(H)
	#R=np.matrix.transpose(I)
	condition_number=sc.linalg.norm(H,2)*sc.linalg.norm(I,2)

	print(condition_number)


	#print(e_n)
	#G=np.matmul(H,np.matmul(np.linalg.inv(H),e_n))-e_n
	#norm=np.linalg.norm(G,ord=2)
	#return norm
	#print(np.matmul(H,e_n))
	#print(np.linalg.inv(H))	





if __name__ == "__main__":

	#print(the_norm_exact(20))
	#print(the_norm_numeric(20))
	print(condition_number(2))