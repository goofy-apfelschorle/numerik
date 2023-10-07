import matplotlib.pyplot as plt 
import numpy as np
from math import cos, log
def fixpoint_iteration(fun, start, N=1000):

	current_point=fun(start)
	#array of points
	points=[[start, current_point]]
	for i in range(0,N):
		points.append([current_point, current_point])
		t=fun(current_point)
		points.append([current_point,t])
		current_point=t 
		
	return points


def g(x):
	return x**(1/2)
def graph_iteration(fun, fixpoint_iteration, start, end, density, iteration_start, N):
	points=fixpoint_iteration(fun, iteration_start, N)
	iteration_X=list(map(lambda point: point[0],points)) #list of exes
	iteration_Y=list(map(lambda point: point[1],points)) #list of whys
	X=np.linspace(start,end,density)
	fun_Y=fun(X)
	plt.plot(X,X, color="blue")
	plt.plot(X,fun_Y, color="red")
	plt.plot(iteration_X,iteration_Y,color="black")
	plt.show()

if __name__ == '__main__':

	graph_iteration(g, fixpoint_iteration, 0.1, 1.5, 1000, 0.1, 20)
