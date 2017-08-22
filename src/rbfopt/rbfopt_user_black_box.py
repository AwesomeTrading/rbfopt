"""Black-box function from user data.

This module contains the definition of a black box function
constructed from user data that can be optimized by RBFOpt.

Licensed under Revised BSD license, see LICENSE.
(C) Copyright International Business Machines Corporation 2017.

"""
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from . import rbfopt_black_box as bb
import numpy as np


class RbfoptUserBlackBox(bb.RbfoptBlackBox):
    """A black-box function from user data that can be optimized.

    A class that implements the necessary methods to describe the
    black-box function to be minimized, and gets all the required data
    from the user.

    Parameters
    ----------
    dimension : int
        Dimension of the problem.
        
    var_lower : 1D numpy.ndarray[float]
        Lower bounds of the decision variables.

    var_upper : 1D numpy.ndarray[float]
        Upper bounds of the decision variables.

    integer_vars : 1D numpy.ndarray[int]
        A list of indices of the variables that must assume integer
        values. Can be empty.

    obj_funct : Callable[1D numpy.ndarray[float]]
        The function to optimize. Must take a numpy array as argument,
        and return a float.

    obj_funct_fast : Callable[1D numpy.ndarray[float]] or None
        The noisy but fast version of the function to optimize. If
        given, it must take a numpy array as argument, and return a
        float. If it is None, we assume that there is no fast version
        of the objective function.
        

    See also
    --------
    :class:`rbfopt_black_box.BlackBox`

    """

    def __init__(self, dimension, var_lower, var_upper, integer_vars,
                 obj_funct, obj_funct_fast=None):
        """Constructor.
        """
        assert(len(var_lower) == dimension)
        assert(len(var_upper) == dimension)
        assert(len(integer_vars) <= dimension)

        self.dimension = dimension
        self.var_lower = np.array(var_lower)
        self.var_upper = np.array(var_upper)
        self.integer_vars = np.array(integer_vars)
        self.obj_funct = obj_funct
        self.obj_funct_fast = obj_funct_fast
    # -- end function

    def get_dimension(self):
        """Return the dimension of the problem.

        Returns
        -------
        int
            The dimension of the problem.
        """
        return self.dimension
    # -- end function
    
    def get_var_lower(self):        
        """Return the array of lower bounds on the variables.

        Returns
        -------
        List[float]
            Lower bounds of the decision variables.
        """
        return self.var_lower
    # -- end function
        
    def get_var_upper(self):
        """Return the array of upper bounds on the variables.

        Returns
        -------
        List[float]
            Upper bounds of the decision variables.
        """
        return self.var_upper
    # -- end function

    def get_integer_vars(self):
        """Return the list of integer variables.
        
        Returns
        -------
        List[int]
            A list of indices of the variables that must assume
            integer values. Can be empty.
        """
        return self.integer_vars
    # -- end function
    
    def evaluate(self, x):
        """Evaluate the black-box function.
        
        Parameters
        ----------
        x : List[float]
            Value of the decision variables.

        Returns
        -------
        float
            Value of the function at x.

        """
        assert(len(x) == self.dimension)
        return self.obj_funct(x)
    # -- end function
    
    def evaluate_fast(self, x):
        """Evaluate a fast approximation of the black-box function.

        Returns an approximation of the value of evaluate(), hopefully
        much more quickly. If has_evaluate_fast() returns False, this
        function will never be queried and therefore it does not have
        to return any value.

        Parameters
        ----------
        x : List[float]
            Value of the decision variables.

        Returns
        -------
        float
            Approximate value of the function at x.

        """
        assert(len(x) == self.dimension)
        if (self.obj_funct_fast is None):
            raise NotImplementedError('evaluate_fast not available')
        else:
            return self.obj_funct_fast(x)
        
    # -- end function

    def has_evaluate_fast(self):
        """Indicate whether evaluate_fast is available.

        Indicate if a fast but potentially noisy version of evaluate
        is available through the function evaluate_fast. If True, such
        function will be used to try to accelerate convergence of the
        optimization algorithm. If False, the function evaluate_fast
        will never be queried.

        Returns
        -------
        bool
            Is evaluate_fast available?
        """
        return (self.obj_funct_fast is not None)
    # -- end function

# -- end class