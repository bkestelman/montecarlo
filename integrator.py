import math
import random

class MCIntegrator():
  """
  @param dim: dimensionality of the functions this Integrator will integrate
  """
  def __init__(self, dim=1):
    #TODO: should bounds also be given here or specified with each call to integrate?
    self.dim = dim

  """
  Compute the integral of a function using Monte Carlo
  @param f: function to integrate. Should accept a dim-dimensional input.
  @param N: number of samples to use
  @param bounds: bounds of integration. Must be a hyperrectangle described as
    a list of dim 2-tuples (a, b) where each a is the left bound and b is the 
    right bound for a particular dimension.
  """
  def integrate(self, f, N, bounds=None):
    if bounds is None:
      bounds = self.first_quadrant()
    if len(bounds) != self.dim:
      raise ValueError(f'Integration bounds length ({len(bounds)}) must match Integrator dimension ({self.dim})')
    #TODO: add checks for 2-tuple structure?

    result = 0
    
    for i in range(N):
      sample_input = self.sample_input(bounds) 
      output = f(sample_input)
      result += output

    bounds_size = self.bounds_size(bounds)
    return result * bounds_size / N

      
  """Bounds for a hypercube in the first quadrant"""
  def first_quadrant(self):
    return [(0, 1)] * self.dim

  def bounds_size(self, bounds):
    return math.prod([(b - a) for a, b in bounds])

  def sample_input(self, bounds):
    return [random.uniform(a, b) for a, b in bounds] #TODO: might be possible to vectorize this

