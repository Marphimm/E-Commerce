from auth import current_user, is_logged_in
from data import products

def view_cart():
  if not is_logged_in:
    print('Login Terlebih Dahulu')
    return
  
  cart = current_user.get("cart", [])
  
  if not cart:
    print('Cart Anda Masih Kosong')
    return
  
  print('\nISI CART')
  total = 0
  for item in cart:
    subtotal = item['price'] = item['qty']
    
    
    