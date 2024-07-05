import os
from colorama import Fore, Style
from tabulate import tabulate

# Fungsi untuk membersihkan layar konsol
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk menampilkan menu dengan warna
def tampilkan_menu():
    print(f"{Fore.BLUE}=== Menu Alfamart ==={Style.RESET_ALL}")
    print("1. Login")
    print("2. Change Password")
    print("3. Cek Transaksi")
    print("4. Claim Voucher")
    print("5. Cek Keranjang")
    print("6. Cek Lokasi Toko")
    print("7. Keluar")
    print("=====================")

    pilihan = input(f"{Fore.YELLOW}Masukkan nomor menu yang ingin diakses (1-7): {Style.RESET_ALL}")
    return pilihan

# Fungsi untuk proses login
def login():
    username = input(f"{Fore.YELLOW}Masukkan username: {Style.RESET_ALL}")
    password = input(f"{Fore.YELLOW}Masukkan password: {Style.RESET_ALL}")

    # Contoh sederhana, validasi login
    if username == "admin" and password == "admin123":
        print(f"{Fore.GREEN}Login berhasil!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Login gagal. Username atau password salah.{Style.RESET_ALL}")

# Fungsi untuk mengubah password
def change_password():
    username = input(f"{Fore.YELLOW}Masukkan username: {Style.RESET_ALL}")
    old_password = input(f"{Fore.YELLOW}Masukkan password lama: {Style.RESET_ALL}")
    new_password = input(f"{Fore.YELLOW}Masukkan password baru: {Style.RESET_ALL}")

    # Contoh sederhana, validasi ubah password
    if username == "admin" and old_password == "admin123":
        print(f"{Fore.GREEN}Password berhasil diubah.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Gagal mengubah password. Username atau password lama salah.{Style.RESET_ALL}")

# Fungsi untuk cek transaksi
def cek_transaksi():
    transaksi = [
        {"Tanggal": "2024-07-04", "Nomor Transaksi": "12345", "Total Belanja": "Rp. 50,000"},
        {"Tanggal": "2024-07-03", "Nomor Transaksi": "67890", "Total Belanja": "Rp. 25,000"}
    ]
    headers = transaksi[0].keys()  # Ambil keys dari dictionary pertama sebagai headers
    data = [list(trans.values()) for trans in transaksi]  # Ambil values dari setiap dictionary sebagai data

    print(f"{Fore.YELLOW}Riwayat Transaksi:{Style.RESET_ALL}")
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

# Fungsi utama program
def main():
    while True:
        clear_screen()
        pilihan = tampilkan_menu()

        if pilihan == '1':
            login()
        elif pilihan == '2':
            change_password()
        elif pilihan == '3':
            cek_transaksi()
        elif pilihan == '4':
            print(f"{Fore.YELLOW}Mengklaim voucher...{Style.RESET_ALL}")
        elif pilihan == '5':
            print(f"{Fore.YELLOW}Mengecek keranjang belanja...{Style.RESET_ALL}")
        elif pilihan == '6':
            print(f"{Fore.YELLOW}Mengecek lokasi toko...{Style.RESET_ALL}")
        elif pilihan == '7':
            print(f"{Fore.BLUE}Terima kasih telah menggunakan layanan Alfamart.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid. Silakan masukkan nomor yang sesuai.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
