import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Variabel input (antecedent)
barangTerjual = ctrl.Antecedent(np.arange(0, 101), 'barangTerjual')
permintaan = ctrl.Antecedent(np.arange(0, 301), 'permintaan')
hargaPerItem = ctrl.Antecedent(np.arange(0, 11), 'hargaPerItem')
profit = ctrl.Antecedent(np.arange(0, 5), 'profit')

# Variabel output (consequent)
stokMakanan = ctrl.Consequent(np.arange(0, 11), 'stokMakanan')

# Fungsi Keanggotaan Barang Terjual
barangTerjual ['rendah'] = fuzz.trimf(barangTerjual.universe, [0, 0, 40])
barangTerjual ['sedang'] = fuzz.trimf(barangTerjual.universe, [30, 50, 70])
barangTerjual ['tinggi'] = fuzz.trimf(barangTerjual.universe, [60, 100, 100])

# Fungsi Keanggotaan Permintaan
permintaan ['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan ['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan ['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

# Fungsi Keanggotaan Harga Per Item
hargaPerItem ['murah'] = fuzz.trimf(hargaPerItem.universe, [0, 0, 4])
hargaPerItem ['sedang'] = fuzz.trimf(hargaPerItem.universe, [3, 5, 8])
hargaPerItem ['mahal'] = fuzz.trimf(hargaPerItem.universe, [6, 10, 10])

# Fungsi Keanggotaan Profit
profit ['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1])
profit ['sedang'] = fuzz.trimf(profit.universe, [1, 2, 2.5])
profit ['banyak'] = fuzz.trimf(profit.universe, [1.5, 2.5, 4])

# Fungsi Keanggotaan Stok Makanan
stokMakanan ['sedang'] = fuzz.trimf(stokMakanan.universe, [1, 5, 9])
stokMakanan ['banyak'] = fuzz.trimf(stokMakanan.universe, [6, 10, 10])

# Aturan Fuzzy
rule1 = ctrl.Rule(
    barangTerjual['tinggi'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['banyak'],
    stokMakanan['banyak']
)

rule2 = ctrl.Rule(
    barangTerjual['tinggi'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['sedang'],
    stokMakanan['sedang']
)

rule3 = ctrl.Rule(
    barangTerjual['tinggi'] & permintaan['sedang'] & hargaPerItem['murah'] & profit['sedang'],
    stokMakanan['sedang']
)

rule4 = ctrl.Rule(
    barangTerjual['sedang'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['sedang'],
    stokMakanan['sedang']
)

rule5 = ctrl.Rule(
    barangTerjual['sedang'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['banyak'],
    stokMakanan['banyak']
)

rule6 = ctrl.Rule(
    barangTerjual['rendah'] & permintaan['rendah'] & hargaPerItem['sedang'] & profit['sedang'],
    stokMakanan['sedang']
)

# Sistem Fuzzy
sistem_ctrl = ctrl.ControlSystem([ rule1, rule2, rule3, rule4, rule5, rule6])
sistem = ctrl.ControlSystemSimulation(sistem_ctrl)

# Sistem Input
sistem.input['barangTerjual'] = 80
sistem.input['permintaan'] = 255
sistem.input['hargaPerItem'] = 2.5
sistem.input['profit'] = 3.5

# Proses
sistem.compute()

# Output
print(f"Stok Makanan: {sistem.output['stokMakanan']:.2f}")

# Visualisasi
barangTerjual.view()
permintaan.view()
hargaPerItem.view()
profit.view()
stokMakanan.view()

stokMakanan.view(sim=sistem)

# Tampilkan semua jendela grafik (non-blocking)
plt.show(block=False)

# Tahan jendela terminal agar tidak langsung tertutup
input("\nTekan Enter pada terminal untuk keluar dan menutup semua grafik...")
plt.close('all')
