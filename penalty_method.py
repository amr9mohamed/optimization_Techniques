import numpy as np

class DifferentiableFn():
    def gradient(self):
        pass

class DifferentiableSquare(DifferentiableFn):
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, vec):
        return np.square(self.fn(vec))

    def gradient(self, vec):
        return 2*self.fn(vec) * self.fn.gradient(vec)

class DifferentiableMax(DifferentiableFn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2

    def __call__(self, vec):
        return np.maximum(self.fn1(vec), self.fn2(vec))

    def gradient(self, vec):
        fn1_mask = (self.fn1(vec)>self.fn2(vec)).astype(int)
        fn2_mask = (self.fn1(vec)>self.fn2(vec)).astype(int)
        return fn1_mask * self.fn1.gradient(vec) + fn2_mask * self.fn2.gradient(vec)

class DifferentiableAdd(DifferentiableFn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
    
    def __call__(self, vec):
        return self.fn1(vec) + self.fn2(vec)

    def gradient(self, vec):
        return self.fn1.gradient(vec) + self.fn2.gradient(vec)


class DifferentiableMult(DifferentiableFn):
    def __init__(self, fn1, fn2):
        self.fn1 = fn1
        self.fn2 = fn2
    
    def __call__(self, vec):
        return self.fn1(vec) * self.fn2(vec)

    def gradient(self, vec):
        return self.fn1.gradient(vec) * self.fn2(vec) + self.fn1(vec) * self.fn2.gradient(vec)

class DifferentiableConstant(DifferentiableFn):
    def __init__(self, value):
        self.value = value

    def __call__(self, vec):
        return self.value

    def gradient(self, vec):
        return 0

    



class PentaltyOptimizer:

    def __init__(self, speed_up_every=1, c=10, lr=1e-1):
        self.speed_up_every = speed_up_every
        self.c = c
        self.lr = lr


    def optimize(self, fn,  initial_vec, steps, equality_constraints=[],
                 inequality_constraints=[]):

        print(initial_vec)

        def _constraints_satisfied(vec):
            return all([constraint(vec) == 0 for constraint in equality_constraints]) and \
                   all([constraint(vec) <= 0 for constraint in inequality_constraints])


        r_k = DifferentiableConstant(1)

        zero = DifferentiableConstant(0)

        equality_constraints_fn = zero

        for constraint in equality_constraints:
            equality_constraints_fn = DifferentiableAdd(equality_constraints_fn, 
                                                         DifferentiableSquare( constraint) ) 

        inequality_constraints_fn = zero
        
        for constraint in inequality_constraints:
            sq_max = DifferentiableSquare(DifferentiableMax(constraint, zero))
            inequality_constraints_fn = DifferentiableAdd(inequality_constraints_fn, sq_max)
                                                           

        equality_constraints_fn = DifferentiableMult(r_k, equality_constraints_fn)

        inequality_constraints_fn = DifferentiableMult(r_k, inequality_constraints_fn)

        constraints_fn = DifferentiableAdd(inequality_constraints_fn, equality_constraints_fn)
    
        penalty_fn = DifferentiableAdd(fn, constraints_fn)

        curr_vec = initial_vec.copy()

        for step in range(steps):
            penalty_gradient = penalty_fn.gradient(curr_vec)
            print(r_k.value)
            print('vec_before: ',curr_vec)
            curr_vec -= self.lr * penalty_gradient
            
            
            print('grad: ', penalty_gradient)
            print('vec: ', curr_vec)
            if _constraints_satisfied(curr_vec):
                print('constraints satisfied')
                return curr_vec
            else:
                print('constraints violated')
            

            print('-----------------------------------------------------')

            if (step + 1)  % self.speed_up_every == 0:
                r_k.value = r_k.value * self.c
                curr_vec = initial_vec
                print('updating', curr_vec)


        return curr_vec

            
class CustomFn(DifferentiableFn):

    def __call__(self, vec):
        return (1/3) * (1 + vec[0])**3  + vec[1]

    def gradient(self, vec):
        return np.array([ (1 + vec[0])**2, 1 ]) 

class InequalityConstraint1(DifferentiableFn):
    
    def __call__(self, vec):
        return 1-vec[0]

    def gradient(self, vec):
        return np.array([-1, 0])

class InequalityConstraint2(DifferentiableFn):
    
    def __call__(self, vec):
        return -vec[1]


    def gradient(self, vec):
        return np.array([0, -1])

def main():
    optimizer = PentaltyOptimizer(lr=0.1, speed_up_every=2)

    min_val = optimizer.optimize(CustomFn(), np.zeros(2), 10,
                                 inequality_constraints=[InequalityConstraint1(), InequalityConstraint2()])

    print(min_val)


main()




