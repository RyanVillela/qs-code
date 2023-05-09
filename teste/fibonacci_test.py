import unittest
from math_samples import MathSamples

class FibonacciTest(unittest.TestCase):

    def teste_01(self):
        """"Testando caso para entrada = 0"""
        self.assertEqual(
            MathSamples.fibomacci(0), 0

        )
    def teste_02(self):
        """"Testando caso para entrada = 2"""
        self.assertEqual(
            MathSamples.fibomacci(1), 1

        )

    def teste_03(self):
        """"Testando caso para entrada = 2"""
        self.assertEqual(
            MathSamples.fibomacci(2), 1

        )

    def teste_04(self):
        """"Testando caso para entrada = 3"""
        self.assertEqual(
            MathSamples.fibomacci(3), 
            2

        )

    def teste_05(self):
        """"Testando caso para entrada = 4"""
        self.assertEqual(
            MathSamples.fibomacci(4), 
            3

        )

    def teste_06(self):
        """"Testando caso para entrada = 5"""
        self.assertEqual(
            MathSamples.fibomacci(5), 
            5

        )

    def teste_07(self):
        """"Testando caso para entrada = 6"""
        self.assertEqual(
            MathSamples.fibomacci(6), 
            8

        )

        
