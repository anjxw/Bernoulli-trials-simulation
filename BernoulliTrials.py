# Anja Vujacic 2021/0307

import math
import numpy as np
from matplotlib import pyplot as plt

def BernoullisTrials(n, p, N):
	f = np.zeros(n + 1)
	for simulation in range(0, N):
		countSuccessfulTrials = 0
		for trial in range(0, n):
			if np.random.rand() < p:
				countSuccessfulTrials += 1
		f[countSuccessfulTrials] += 1
	return f / N

def BinomialDistribution(n, p):
	f = np.arange(n + 1) * 1.0
	for x in f.astype(int):
		f[x] = math.comb(n, x) * (p**(x)) * ((1-p)**(n-x))
	return f

def PlotHistogram(a, b, N):
    	x = np.arange(len(a))
    	fig, ax = plt.subplots(figsize=(8, 6))
    	w = 0.4
    	bar1 = ax.bar(x-w/2, a, w, align='center', alpha=0.8, label='Simulation', color='lightsteelblue', edgecolor='black')
    	bar2 = ax.bar(x+w/2, b, w, align='center', alpha=0.8, label='Binomial Distribution', color='mediumslateblue', edgecolor='black')
    	ax.set_xticks(x)
    	ax.set_title('Histogram (N={})'.format(N), fontsize=14)
    	ax.set_xlabel('Number of Successes', fontsize=12)
    	ax.set_ylabel('Relative Frequency', fontsize=12)
    	ax.legend()
    	ax.grid(True)
    	ax.set_facecolor('whitesmoke')
    	ax.tick_params(axis='both', labelsize=10)
    	plt.ylim([0, 0.3])
    	plt.show()


def RunSimulation(n, p, N):
	# Simulate trials and binomial distribution
	relativeFreqSimulation = BernoullisTrials(n=n, p=p, N=N)
	relativeFreqTrue = BinomialDistribution(n=n, p=p)
	np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})
	print("Simulation (n={}, p={}) for {} trials:\n{}".format(n, p, N, relativeFreqSimulation))
	print("Binomial distribution (n={}, p={}) for {} trials:\n{}".format(n, p, N, relativeFreqTrue))
	# Calculate and print error
	absoluteError = np.abs(relativeFreqTrue - relativeFreqSimulation)
	print("Absolute error:\n{}".format(absoluteError))
	RMSE = math.sqrt(np.square(np.subtract(relativeFreqTrue, relativeFreqSimulation)).mean())
	print("Root Mean Square Error: {}\n\n".format(RMSE))
	# Plot histogram
	PlotHistogram(relativeFreqSimulation, relativeFreqTrue, N)

def main():
	# First simulation (100 trials)
	RunSimulation(n=10, p=0.7, N=100)
 	# Second simulation (1000 trials)
	RunSimulation(n=10, p=0.7, N=1000)

if __name__=="__main__":
	main()
