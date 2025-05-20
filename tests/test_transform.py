import unittest
import pandas as pd
from utils.transform import transform_product_data

class TestTransformData(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'title': ['T-shirt', 'Hoodie', 'Pants', 'Unknown Product'],
            'price': ['$10.00', '$20.50', '$30.75', '$invalid'],
            'rating': ['4.5', '3.9', 'invalid', '4.0'],
            'colors': ['3', '4', 'undefined', '5'],
            'size': ['M', 'L', 'undefined', 'XL'],
            'gender': ['Men', 'Women', 'undefined', 'Unisex']
        }
        self.df_raw = pd.DataFrame(self.sample_data)

    def test_transform_output(self):
        df_transformed = transform_product_data(self.df_raw)

        # Pastikan kolom yang dibersihkan ada
        self.assertIn('price', df_transformed.columns)
        self.assertIn('rating', df_transformed.columns)
        self.assertIn('colors', df_transformed.columns)
        self.assertIn('size', df_transformed.columns)
        self.assertIn('gender', df_transformed.columns)
        
        # Pastikan kolom timestamp ditambahkan
        self.assertIn('timestamp', df_transformed.columns)

        # Pastikan tidak ada nilai null
        self.assertFalse(df_transformed.isnull().values.any())

        # Pastikan price, rating, colors bertipe sesuai
        self.assertTrue(pd.api.types.is_float_dtype(df_transformed['price']))
        self.assertTrue(pd.api.types.is_float_dtype(df_transformed['rating']))
        self.assertTrue(pd.api.types.is_integer_dtype(df_transformed['colors']))
        self.assertTrue(pd.api.types.is_object_dtype(df_transformed['size']))
        self.assertTrue(pd.api.types.is_object_dtype(df_transformed['gender']))

        # Cek bahwa timestamp tidak kosong
        self.assertTrue(df_transformed['timestamp'].notnull().all())
        

if __name__ == '__main__':
    unittest.main()
