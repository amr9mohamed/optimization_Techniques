import numpy as np

class Differentiable_fn():
    def gradient(self):
        pass

class Differentiable_square(Differentiable_fn):
    def __init__(self, fn):
        self.fn = fn
        self.cache = ()

    def __call__(self):
        return np.square(self.fn())

    def gradient(self):
        return 2*self.fn()

class Differentiable_max(Differentiable_fn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
        self.cache = ()

    def __call__(self):
        fn1_mask = (self.fn1()>self.fn2()).astype(int)
        fn2_mask = (self.fn1()>self.fn2()).astype(int)
        self.cache = (fn1_mask, fn2_mask)
        return np.maximum(self.fn1(), self.fn2())

    def gradient(self):
        fn1_mask, fn2_mask = self.cache
        return fn1_mask * self.fn1.gradient() + fn2_mask * self.fn2.gradient()

class Differentiable_add(Differentiable_fn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
    
    def __call__(self):
        return self.fn1() + self.fn2()

    def gradient(self):
        return self.fn1.gradient() + self.fn2.gradient()


class Differentiable_mult(Differentiable_fn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
    
    def __call__(self):
        return fn1() * fn2()

    def gradient(self):
        return fn1.gradient() * fn2() + fn1



class PentaltyOptimizer:
    def optimize(self, f_n, equality_constraints,
                 inequality_constraints, steps, c=10,
                  lr=1e-10):

        r_k = 1
        phi = f_n 



