from datetime import datetime
import pandas as pd

def clean_price(p):
    try:
        price_usd = float(str(p).replace('$', '').replace(',', '').strip())
        return price_usd * 16000
    except:
        return None

def clean_rating(r):
    try:
        return float(r)
    except:
        return None

def clean_colors(c):
    try:
        c = str(c).strip()
        return int(c)
    except:
        return None  # kalau gak bisa dikonversi ke angka, buang

def clean_field(val):
    if isinstance(val, str) and val.strip().lower() == 'undefined':
        return 'Unknown'
    return val

def transform_product_data(df):
    df = df.drop_duplicates().copy()

    # Bersihkan nilai
    df['price'] = df['price'].apply(clean_price)
    df['rating'] = df['rating'].apply(clean_rating)
    df['colors'] = df['colors'].apply(clean_colors)
    df['size'] = df['size'].apply(clean_field)
    df['gender'] = df['gender'].apply(clean_field)

    # Hapus hanya jika price, rating, dan colors tidak valid
    df.dropna(subset=['price', 'rating', 'colors'], inplace=True)

    # Pastikan colors tipe int, size dan gender string
    df['colors'] = df['colors'].astype(int)
    df['size'] = df['size'].astype(str)
    df['gender'] = df['gender'].astype(str)

# Tambahkan kolom timestamp
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return df






