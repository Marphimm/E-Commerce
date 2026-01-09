from auth import current_user, require_login
from cart import cart, is_cart_empty
from data import products

transactions = []

def checkout():
  if not require_login():
    return
  
  if is_cart_empty():
    print('Keranjang Kosong')
    return
  
  total_price = 0
  
  for item in cart:
    for product in products:
      if product['id'] == item['product_id']:
        if product['stock'] < item['qty']:
          print(f"Stok {product['stock']} Tidak Cukup")
          return
        
        product['stock'] -= product['qty']
        subtotal = item['price'] * item['qty']
        
        total_price += subtotal
  
  transaction = {
    'user': current_user['username'],
    'items': cart.copy(),
    'total': total_price
  }
  
  transactions.append(transaction)
  cart.clear()
  print('Checkout Berhasil')
  print(f'Total Pembayaran: {total_price}')
  