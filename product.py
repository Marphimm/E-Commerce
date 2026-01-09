from auth import current_user, require_login
from data import products

def show_products():
  if not products:
    print('Produk Belum Tersedia')
    return
  
  print('\nDaftar Produk')
  for product in products:
    print(f"- {product['name']} | Harga: {product['price']} | Stok: {product['stock']}")

def add_product(name, price, stock):
  if not require_login():
    return
  
  if current_user['role'] != 'penjual':
    print('Selain Penjual Tidak Bisa Menambahkan Barang')
    return
  
  new_id = len(products) + 1
  
  product = {
    "id": new_id,
    "name": name,
    "price": price,
    "stock": stock
  }
  
  products.append(product)
  print('Produk Berhasil Ditambahkan')  