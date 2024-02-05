from utils import gen_points_powers_of_tau, polynomial_with_roots, gen_points_powers_of_tau_t
from random import randint

def trusted_setup(degree, field):
    tau = field(randint(1, 100000))
    p1 = gen_points_powers_of_tau(int(tau), degree, 1)
    p2 = gen_points_powers_of_tau(int(tau), degree, 2)
    t = polynomial_with_roots(degree, field)
    p3 = gen_points_powers_of_tau_t(int(tau), degree, int(t(tau)))
    return p1, p2, p3

export = {
    trusted_setup
}