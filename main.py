# We import the algorithm (You can use from pyade import * to import all of them)
import pyade.lshade
import numpy as np


def callback(population_size, individual_size, bounds, func, opts, memory_size, callback, max_evals, seed, population,
             init_size, m_cr, m_f, archive, all_indexes, current_generation, num_evals, n, i, max_iters, r, cr, f, p,
             mutated, crossed, k, fitness, c_fitness, indexes, weights, new_population_size, best_indexes=None):
    print(f'Generation #{int(current_generation)}:')
    mean = np.mean(population)
    print(f'\tmean: {mean}')


# You may want to use a variable so its easier to change it if we want
algorithm = pyade.lshade

# We get default parameters for a problem with two variables
params = algorithm.get_default_params(dim=1)

# We define the boundaries of the variables
params['bounds'] = np.array([[-75, 75]])

# We indicate the function we want to minimize
params['func'] = lambda x: x[0] ** 2

params['callback'] = callback

# We run the algorithm and obtain the results
solution, fitness = algorithm.apply(**params)

print(f'Solution: {solution}, fitness: {fitness}')
