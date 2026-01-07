from auth import current_user, is_logged_in
from data import products

def show_products():
  if not products:
    print('Produk Belum Tersedia')
    return
  
  print('\nDaftar Produk')
  for product in products:
    print(f'- {product['name']} | Harga: {product['price']} | Stok: {product['stock']}')

def add_product(name, price, stock):
  if not is_logged_in():
    print('Login Terlebih Dahulu')
    return
  
  if current_user['role'] != 'penjual':
    print('Anda bukan Penjual tidak bisa menambahkan barang')
    return
  
  new_id = len(products) + 1
  
  product = {
    "id": new_id,
    "name": name,
    "price": price,
    "stok": stock
  }
  
  products.append(product)
  print('Produk Berhasil Ditambahkan')  