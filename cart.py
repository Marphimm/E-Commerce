from auth import current_user, require_login
from data import products

cart = []

def added_to_cart(product_id, qty):
  if not require_login():
    return
  
  for product in products:
    if products['id'] == product_id:
      if product['stock'] < qty:
        print('Stok Produk Tidak Cukup')
        return
      
      item = {
        'produk_id': product['id'],
        'nama': product['name'],
        'harga': product['price'],
        'stok': qty
      }
      
      cart.append(item)
      print('Produk Berhasil Ditambahkan Ke Keranjang')
      return
    
  print('Produk Tidak Ditemuka')

def show_cart():
  if not require_login():
    return
  
  if not cart:
    print('Keranjang Masih Kosong')
    return
  
  print('\nIsi Keranjang')
  
  total = 0
  
  for item in cart:
    subtotal = item['harga'] * item['stok']
    total += subtotal
    print(f"- {item['nama']} | {item['stok']} | Subtotal: {subtotal}")
  
  print(f'Total; {total}')

def clear_cart():
  if not require_login():
    return
  
  cart.clear()
  print('Keranjang Berhasil Dikosongkan')
  
def is_cart_empty():
  return len(cart) == 0