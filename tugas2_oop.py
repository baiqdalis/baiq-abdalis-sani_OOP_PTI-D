class Motor:
    # Class variables (dibagikan oleh semua instance)
    jumlah_motor = 0  # Counter untuk jumlah motor yang dibuat
    merk_populer = ["Honda", "Yamaha", "Suzuki"]  # List merk populer (statis)
    
    def __init__(self, merk, warna, cc, surat, mesin, tahun, harga=0):
        """
        Constructor untuk kelas Motor.
        - merk: str, merek sepeda motor (misal: 'Honda')
        - warna: str, warna sepeda motor (misal: 'Merah')
        - cc: int, kapasitas mesin dalam cc (misal: 150)
        - surat: str, status surat kendaraan (misal: 'Lengkap')
        - mesin: str, tipe mesin (misal: '4-Tak')
        - tahun: int, tahun pembuatan (misal: 2020)
        - harga: int, harga motor (misal: 20000000) - Instance variable baru
        """
        # Instance variables (unik per objek)
        self.merk = merk
        self.warna = warna
        self.cc = cc
        self.surat = surat
        self.mesin = mesin
        self.tahun = tahun
        self.harga = harga  # Instance variable baru
        
        # Increment class variable setiap kali instance dibuat
        Motor.jumlah_motor += 1
    
    def __str__(self):
        """Method untuk mencetak informasi motor secara rapi."""
        return f"Motor {self.merk} ({self.tahun}) - Warna: {self.warna}, CC: {self.cc}, Mesin: {self.mesin}, Surat: {self.surat}, Harga: Rp{self.harga:,}"

# Contoh penggunaan:
if __name__ == "__main__":
    # Akses class variables sebelum membuat instance
    print(f"Merk populer (class variable): {Motor.merk_populer}")
    print(f"Jumlah motor awal (class variable): {Motor.jumlah_motor}")
    
    # Membuat objek motor
    motor1 = Motor("Honda", "Merah", 150, "Lengkap", "4-Tak", 2020, 20000000)
    motor2 = Motor("Yamaha", "Biru", 125, "Lengkap", "4-Tak", 2021, 18000000)
    
    # Mencetak informasi
    print(motor1)
    print(motor2)
    
    # Akses atribut individual (instance variables)
    print(f"Merek motor1: {motor1.merk}")
    print(f"CC motor1: {motor1.cc}")
    print(f"Harga motor2: Rp{motor2.harga:,}")
    
    # Akses class variables via kelas atau instance
    print(f"Jumlah motor total (via kelas): {Motor.jumlah_motor}")
    print(f"Jumlah motor total (via instance): {motor1.jumlah_motor}")  # Sama saja, karena shared
    print(f"Merk populer (via instance): {motor2.merk_populer}")  # Sama saja