from auth import register, login, logout, current_user
from product import show_products, add_product
from cart import add_to_cart, show_cart
from transaction import checkout

def clear_line():
    print("-" * 40)

def header():
    clear_line()
    print("   E-COMMERCE SEDERHANA PYTHON")
    print("   Project UAS Semester 1")
    clear_line()

def show_status():
    if current_user:
        print(f"Login sebagai: {current_user['username']} ({current_user['role']})")
    else:
        print("Status: Belum Login")
    clear_line()

def main_menu():
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Lihat Produk")
    print("5. Menu Keranjang")
    print("6. Checkout")
    print("0. Keluar")

def seller_menu():
    print("7. Tambah Produk (Penjual)")

def cart_menu():
    clear_line()
    print("MENU KERANJANG")
    print("1. Lihat Keranjang")
    print("2. Tambah Produk ke Keranjang")
    print("0. Kembali")

def handle_cart():
    while True:
        cart_menu()
        choice = input("Pilih menu keranjang: ")

        if choice == "1":
            show_cart()

        elif choice == "2":
            product_id = int(input("ID Produk: "))
            qty = int(input("Jumlah: "))
            add_to_cart(product_id, qty)

        elif choice == "0":
            break

        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        header()
        show_status()
        main_menu()

        if current_user and current_user["role"] == "penjual":
            seller_menu()

        choice = input("Pilih menu: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (penjual/pembeli): ")
            register(username, password, role)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            login(username, password)

        elif choice == "3":
            logout()

        elif choice == "4":
            show_products()

        elif choice == "5":
            handle_cart()

        elif choice == "6":
            checkout()

        elif choice == "7":
            if current_user and current_user["role"] == "penjual":
                name = input("Nama Produk: ")
                price = int(input("Harga: "))
                stock = int(input("Stok: "))
                add_product(name, price, stock)
            else:
                print("Akses ditolak.")

        elif choice == "0":
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("Menu tidak tersedia.")

if __name__ == "__main__":
    main()