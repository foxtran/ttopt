"""The demo of using ttopt. Simple example with "scalar" input.

We'll find the minimum for the simple analytic function of the form f(x), where
input x is the [dimension] numpy array (not vectorized!).

Run it from the root of the project as "python demo/vect.py".

As a result of the script work we expect the output in console like this:
"
...
Simple-5d | k=1.00e+04 | t_cur=1.54e-01 | e_x=3.55e-02 e_y=1.03e-04
----------------------------------------------------------------------
Simple-5d | k=1.00e+04 | t_all=1.75e-01 | e_x=3.55e-02 e_y=1.03e-04
"

"""
import numpy as np
from scipy.optimize import rosen


from ttopt import TTOpt
from ttopt import ttopt_init


np.random.seed(42)


d = 5                       # Number of function dimensions:
rank = 4                    # Maximum TT-rank while cross-like iterations
def f(x):                   # Target function
    return np.sin(0.1 * x[0])**2 + 0.1 * np.sum(x[1:]**2)


# We initialize the TTOpt class instance with the correct parameters:
tto = TTOpt(
    f=f,                    # Function for minimization. X is [samples, dim]
    d=d,                    # Number of function dimensions
    a=-1.,                  # Grid lower bound (number or list of len d)
    b=+1.,                  # Grid upper bound (number or list of len d)
    n=2**6,                 # Number of grid points (number or list of len d)
    evals=1.E+4,            # Number of function evaluations
    name='Simple',          # Function name for log (this is optional)
    x_opt_real=np.zeros(d), # Real value of x-minima (x; this is for test)
    y_opt_real=0.,          # Real value of y-minima (y=f(x); this is for test)
    is_vect=False,          # The function accepts only one spatial point
    with_log=True)


# And now we launching the minimizer:
tto.optimize(rank)


# We can extract the results of the computation:
x = tto.x_opt          # The found value of the minimum of the function (x)
y = tto.y_opt          # The found value of the minimum of the function (y=f(x))
k_c = tto.k_cache      # Total number of cache usage (should be 0 in this demo)
k_e = tto.k_evals      # Total number of requests to func (is always = evals)
k_t = tto.k_total      # Total number of requests (k_cache + k_evals)
t_f = tto.t_evals_mean # Average time spent to real function call for 1 point
                       # ... (see "ttopt.py" and docs for more details)


# We log the final state:
print('-' * 70 + '\n' + tto.info() +'\n\n')
