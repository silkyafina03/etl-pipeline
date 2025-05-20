import pandas as pd
from utils.extract import extract_data_from_url
from utils.transform import transform_product_data
from utils.load import load_product_data

def main():
    url = "https://fashion-studio.dicoding.dev/"
    df_raw = extract_data_from_url(url)

    print("Hasil scraping:")
    print(df_raw.head())
    print("Jumlah data hasil scrape:", len(df_raw))

    if not df_raw.empty:
        df_clean = transform_product_data(df_raw)

        print("Hasil transformasi:")
        print(df_clean.head())
        print("Jumlah data setelah transform:", len(df_clean))

        if not df_clean.empty:
            load_product_data(df_clean, "products.csv")
            print("Produk berhasil disimpan ke products.csv")
        else:
            print("Data kosong setelah transformasi.")
    else:
        print("Tidak ada data yang ditemukan.")


if __name__ == "__main__":
    main()
