import unittest
import math
from integrator import MCIntegrator

class TestIntegrator(unittest.TestCase):
  def setUp(self):
    self.integrator_1d = MCIntegrator(1)
    self.integrator_2d = MCIntegrator(2)

  def test_first_quadrant(self):
    bounds = self.integrator_1d.first_quadrant()
    self.assertEqual(len(bounds), 1)
    self.assertEqual(bounds[0][0], 0)
    self.assertEqual(bounds[0][1], 1)
    #TODO: test 2d

  def test_bounds_size(self):
    bounds = self.integrator_1d.first_quadrant()
    self.assertEqual(self.integrator_1d.bounds_size(bounds), 1)
    #TODO: test 2d and other bounds

  def test_sample_input(self):
    bounds = self.integrator_1d.first_quadrant()
    sample_input = self.integrator_1d.sample_input(bounds)
    self.assertLess(sample_input[0], 1)
    self.assertGreater(sample_input[0], 0)
    #TODO: test 2d and other bounds

  def test_estimate_pi(self):
    def circle(x):
      x = x[0]
      return math.sqrt(1 - x * x)
    target = math.pi / 4
    estimate = self.integrator_1d.integrate(circle, 100)
    self.assertAlmostEqual(estimate, target, 1)
    #TODO: test 2d

