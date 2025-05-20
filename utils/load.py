import pandas as pd

def load_product_data(df: pd.DataFrame, output_path: str = "products.csv") -> None:
    """Simpan DataFrame ke file CSV di root folder proyek"""
    df.to_csv(output_path, index=False)