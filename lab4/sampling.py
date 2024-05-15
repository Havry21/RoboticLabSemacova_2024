import math
import numpy as np
from scipy. stats import norm
import timeit
import matplotlib.pyplot as plt

def sample_normal_distribution(u,q):
    return u + 0.5 * np.sum(np.random.uniform(-q,q, 12))    

def sample_distribution(u, q):
    while True:
        x = sample_normal_distribution(u,q)
        y = np.random.uniform(0,norm(u,q).pdf(u)) 
        if(y < norm(u,q).pdf(x)):
            return x
        
def sample_normal_boxmuller(mu,q):
    u = np.random.uniform(0, 1, 2)
    x = math.cos(2*np.pi*u[0]) * math.sqrt(-2*math.log(u[1]))
    return mu + q * x

def evaluate(sample_function, _plot):
    u = 0
    q = 2
    sample_count = 1000
    sample = []
    tic = timeit.default_timer()
    for i in range(sample_count):
        sample.append(sample_function(u,q))
    
    dt = timeit.default_timer() - tic
    print("------------------------------------------------")
    print(f"{sample_function.__name__}, sample_count - {sample_count}")

    print(f"time = {dt}")
    print(f"means {np.mean(sample)}, std {np.std(sample)}")
    print("------------------------------------------------\n")

    count, bins, ignored = _plot.hist(sample, 100)
    _plot.plot(bins, norm(u, q).pdf(bins), linewidth=2, color='r')
    # _plot.xlim([u - 3*q, u + 3*q])
    _plot.set_title(sample_function.__name__)

def main():
    fig, (pl1,pl2,pl3,pl4) = plt.subplots(1,4)
    plot = [pl1,pl2,pl3,pl4]
    s_func = [
       sample_normal_distribution,
        sample_distribution,
        sample_normal_boxmuller,
        np.random.normal
    ]
    for fn, pl in zip(s_func, plot):
        evaluate(fn,pl)
        
    plt.show()

if __name__ == '__main__':
    main()
