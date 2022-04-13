import unittest

from knapsack import greedy_knapsack as kp


class TestClass(unittest.TestCase):
    

    def test_sorted(self):
        
        profit = [10, 20, 30, 40, 50, 60]
        weight = [2, 4, 6, 8, 10, 12]
        max_weight = 100
        self.assertEqual(kp.calc_profit(profit, weight, max_weight), 210)

    def test_negative_max_weight(self):
        
        
        
        
        self.assertRaisesRegex(ValueError, "max_weight must greater than zero.")

    def test_negative_profit_value(self):
        
        
        
        
        self.assertRaisesRegex(ValueError, "Weight can not be negative.")

    def test_negative_weight_value(self):
        
        
        
        
        self.assertRaisesRegex(ValueError, "Profit can not be negative.")

    def test_null_max_weight(self):
        
        
        
        
        self.assertRaisesRegex(ValueError, "max_weight must greater than zero.")

    def test_unequal_list_length(self):
        
        
        
        
        self.assertRaisesRegex(
            IndexError, "The length of profit and weight must be same."
        )


if __name__ == "__main__":
    unittest.main()
