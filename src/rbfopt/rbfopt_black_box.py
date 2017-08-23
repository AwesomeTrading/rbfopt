"""Black-box function.

This module contains the definition of the black box function that is
optimized by RBFOpt, when using the default command line
interface. This is an abstract class: all methods *must* be
reimplemented by the user.

Licensed under Revised BSD license, see LICENSE.
(C) Copyright Singapore University of Technology and Design 2014.
(C) Copyright International Business Machines Corporation 2016.
Research partially supported by SUTD-MIT International Design Center.

"""

from abc import ABCMeta, abstractmethod

class RbfoptBlackBox:
    """Abstract class for a black-box function that can be optimized. 
    
    A class that declares (but does not implement) the necessary
    methods to describe a black-box function. The user can implement a
    derived class and use it to compute the function that must be
    optimized.

    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_dimension(self):
        """Return the dimension of the problem.

        Returns
        -------
        int
            The dimension of the problem.
        """
        pass
    # -- end function

    @abstractmethod
    def get_var_lower(self):        
        """Return the array of lower bounds on the variables.

        Returns
        -------
        1D numpy.ndarray[float]
            Lower bounds of the decision variables.
        """
        pass
    # -- end function
    
    @abstractmethod
    def get_var_upper(self):
        """Return the array of upper bounds on the variables.

        Returns
        -------
        1D numpy.ndarray[float]
            Upper bounds of the decision variables.
        """
        pass
    # -- end function

    def get_integer_vars(self):
        """Return the list of integer variables.
        
        Returns
        -------
        1D numpy.ndarray[int]
            A list of indices of the variables that must assume
            integer values. Can be empty.
        """
        pass
    # -- end function

    @abstractmethod
    def evaluate(self, x):

        """Evaluate the black-box function.
        
        Parameters
        ----------
        x : 1D numpy.ndarray[float]
            Value of the decision variables.

        Returns
        -------
        float
            Value of the function at x.

        """
        pass
    # -- end function

    @abstractmethod
    def evaluate_noisy(self, x):
        """Evaluate a fast approximation of the black-box function.

        Returns an approximation of the value of evaluate(), hopefully
        much more quickly, and provides error bounds on the
        evaluation. If has_evaluate_noisy() returns False, this
        function will never be queried and therefore it does not have
        to return any value.

        Parameters
        ----------
        x : 1D numpy.ndarray[float]
            Value of the decision variables.

        Returns
        -------
        1D numpy.ndarray[float]
            A numpy array with three floats (value, lower, upper)
            containing the approximate value of the function at x, the
            lower error bound, and the upper error bound, such that
            the true function value is contained between value + lower
            and value + upper. Hence, lower should be <= 0 while upper
            should be >= 0.

        """
        pass
    # -- end function

    @abstractmethod
    def has_evaluate_noisy(self):
        """Indicate whether evaluate_noisy is available.

        Indicate if a fast but potentially noisy version of evaluate
        is available through the function evaluate_noisy. If True, such
        function will be used to try to accelerate convergence of the
        optimization algorithm. If False, the function evaluate_noisy
        will never be queried.

        Returns
        -------
        bool
            Is evaluate_noisy available?
        """
        pass
    # -- end function

# -- end class
