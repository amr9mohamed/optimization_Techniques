import numpy as np

class Differentiable_fn():
    def gradient(self):
        pass

class Differentiable_square(Differentiable_fn):
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, vec):
        return np.square(self.fn(vec))

    def gradient(self, vec):
        return 2*self.fn(vec)

class Differentiable_max(Differentiable_fn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2

    def __call__(self, vec):
        return np.maximum(self.fn1(vec), self.fn2(vec))

    def gradient(self, vec):
        fn1_mask = (self.fn1(vec)>self.fn2(vec)).astype(int)
        fn2_mask = (self.fn1(vec)>self.fn2(vec)).astype(int)
        
        return fn1_mask * self.fn1.gradient(vec) + fn2_mask * self.fn2.gradient(vec)

class Differentiable_add(Differentiable_fn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
    
    def __call__(self, vec):
        return self.fn1(vec) + self.fn2(vec)

    def gradient(self, vec):
        return self.fn1.gradient(vec) + self.fn2.gradient(vec)


class Differentiable_mult(Differentiable_fn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
    
    def __call__(self, vec):
        return self.fn1(vec) * self.fn2(vec)

    def gradient(self, vec):
        return self.fn1.gradient(vec) * self.fn2(vec) + self.fn1.gradient(vec) * self.fn2(vec)

class Differentiable_constant(Differentiable_fn):
    def __init__(self, value):
        self.value = value

    def __call__(self, vec):
        return self.value()

    def gradient(self, vec):
        return 0

    def __add__(self, scaler):
        self.value += scaler

    def __mul__(self, scaler):
        self.value *= scaler
    



class PentaltyOptimizer:
    def optimize(self, fn, equality_constraints,
                 inequality_constraints, initial_vec, steps,
                 speed_up_every=1, c=10, lr=1e-1):

        def _constraints_satisfied(vec):
            return all([constraint(vec) == 0 for constraint in equality_constraints]) and \
                   all([constraint(vec) <= 0 for constraint in inequality_constraints])


        r_k = Differentiable_constant(1)

        zero = Differentiable_constant(0)

        equality_constraints_fn = zero

        for constraint in equality_constraints:
            equality_constraints_fn = Differentiable_add(equality_constraints_fn, 
                                                         Differentiable_square( constraint) ) 

        inequality_constraints_fn = zero
        
        for constraint in inequality_constraints:
            sq_max = Differentiable_square(Differentiable_max(constraint, zero))
            inequality_constraints_fn = Differentiable_add(inequality_constraints_fn, sq_max)
                                                           

        equality_constraints_fn = Differentiable_mult(r_k, equality_constraints_fn)

        inequality_constraints_fn = Differentiable_mult(r_k, inequality_constraints_fn)

        constraints_fn = Differentiable_add(inequality_constraints_fn, equality_constraints_fn)
    
        penalty_fn = Differentiable_add(fn, constraints_fn)

        curr_vec = initial_vec

        for _ in range(steps):
            penalty_gradient = penalty_fn.gradient(curr_vec)
            curr_vec = curr_vec - penalty_gradient








