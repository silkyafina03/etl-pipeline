import unittest
import pandas as pd
import os
from utils.load import load_product_data


class TestLoadFunction(unittest.TestCase):

    def setUp(self):
        self.sample_df = pd.DataFrame({
            "title": ["T-Shirt A"],
            "price": [160000],
            "rating": [4.8],
            "colors": [3],
            "size": ["M"],
            "gender": ["Men"]
        })
        self.output_path = "test_products.csv"

    def test_file_is_created(self):
        load_product_data(self.sample_df, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_csv_contents_match(self):
        load_product_data(self.sample_df, self.output_path)
        loaded_df = pd.read_csv(self.output_path)
        pd.testing.assert_frame_equal(self.sample_df, loaded_df)

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
       

if __name__ == '__main__':
    unittest.main()