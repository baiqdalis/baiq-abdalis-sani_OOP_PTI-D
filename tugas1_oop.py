class Motor:
    def __init__(self, merk, warna, cc, surat, mesin, tahun):
        """
        Constructor untuk kelas Motor.
        - merk: str, merek sepeda motor (misal: 'Honda')
        - warna: str, warna sepeda motor (misal: 'Merah')
        - cc: int, kapasitas mesin dalam cc (misal: 150)
        - surat: str, status surat kendaraan (misal: 'Lengkap')
        - mesin: str, tipe mesin (misal: '4-Tak')
        - tahun: int, tahun pembuatan (misal: 2020)
        """
        self.merk = merk
        self.warna = warna
        self.cc = cc
        self.surat = surat
        self.mesin = mesin
        self.tahun = tahun
    
    def __str__(self):
        """Method untuk mencetak informasi motor secara rapi."""
        return f"Motor {self.merk} ({self.tahun}) - Warna: {self.warna}, CC: {self.cc}, Mesin: {self.mesin}, Surat: {self.surat}"

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat objek motor
    motor1 = Motor("Honda", "Merah", 150, "Lengkap", "4-Tak", 2020)
    
    # Mencetak informasi
    print(motor1)
    # Output: Motor Honda (2020) - Warna: Merah, CC: 150, Mesin: 4-Tak, Surat: Lengkap
    
    # Akses atribut individual
    print(f"Merek: {motor1.merk}")
    print(f"CC: {motor1.cc}")