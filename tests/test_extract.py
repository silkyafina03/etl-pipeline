import unittest
import pandas as pd
from utils.extract import extract_data_from_url

class TestExtractFunction(unittest.TestCase):

    def setUp(self):
    
        self.test_url = "https://fashion-studio.dicoding.dev/"  

    def test_extract_returns_dataframe(self):
        """Test fungsi extract mengembalikan DataFrame"""
        df = extract_data_from_url(self.test_url)
        self.assertIsInstance(df, pd.DataFrame)

    def test_dataframe_is_not_empty(self):
        """Pastikan DataFrame tidak kosong"""
        df = extract_data_from_url(self.test_url)
        self.assertFalse(df.empty, "DataFrame kosong, kemungkinan scraping gagal.")

    def test_dataframe_columns(self):
        """Pastikan kolom sesuai dengan yang diharapkan"""
        df = extract_data_from_url(self.test_url)
        expected_columns = {"title", "price", "rating", "colors", "size", "gender"}
        self.assertTrue(expected_columns.issubset(set(df.columns)), f"Kolom tidak lengkap: {df.columns}")

    def test_no_missing_values(self):
        """Cek apakah ada missing values"""
        df = extract_data_from_url(self.test_url)
        self.assertFalse(df.isnull().any().any(), "Ada missing values dalam DataFrame.")

if __name__ == '__main__':
    unittest.main()
