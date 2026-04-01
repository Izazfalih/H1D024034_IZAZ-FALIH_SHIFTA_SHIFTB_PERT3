import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# INPUT (Antecedent)
informasi = ctrl.Antecedent(np.arange(0, 101), 'informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101), 'persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101), 'sarpras')
# OUTPUT (Consequent)
kepuasan = ctrl.Consequent(np.arange(0, 401), 'kepuasan')

# FUZZY SET INPUT
# INFORMASI
informasi['tidak memuaskan'] = fuzz.trimf(informasi.universe, [0, 60, 75])
informasi['cukup memuaskan'] = fuzz.trimf(informasi.universe, [60, 75, 90])
informasi['memuaskan'] = fuzz.trimf(informasi.universe, [75, 90, 100])

# PERSYARATAN
persyaratan['tidak memuaskan'] = fuzz.trimf(persyaratan.universe, [0, 60, 75])
persyaratan['cukup memuaskan'] = fuzz.trimf(persyaratan.universe, [60, 75, 90])
persyaratan['memuaskan'] = fuzz.trimf(persyaratan.universe, [75, 90, 100])

# PETUGAS
petugas['tidak memuaskan'] = fuzz.trimf(petugas.universe, [0, 60, 75])
petugas['cukup memuaskan'] = fuzz.trimf(petugas.universe, [60, 75, 90])
petugas['memuaskan'] = fuzz.trimf(petugas.universe, [75, 90, 100])

# SARPRAS
sarpras['tidak memuaskan'] = fuzz.trimf(sarpras.universe, [0, 60, 75])
sarpras['cukup memuaskan'] = fuzz.trimf(sarpras.universe, [60, 75, 90])
sarpras['memuaskan'] = fuzz.trimf(sarpras.universe, [75, 90, 100])

# FUZZY SET OUTPUT
kepuasan['tidak memuaskan'] = fuzz.trimf(kepuasan.universe, [0, 50, 75])
kepuasan['kurang memuaskan'] = fuzz.trimf(kepuasan.universe, [50, 75, 100])
kepuasan['cukup memuaskan'] = fuzz.trapmf(kepuasan.universe, [100, 150, 250, 275])
kepuasan['memuaskan'] = fuzz.trapmf(kepuasan.universe, [250, 275, 325, 350])
kepuasan['sangat memuaskan'] = fuzz.trimf(kepuasan.universe, [325, 350, 400])

# RULE (contoh representatif)
rule1 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['tidak memuaskan'])

rule2 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['tidak memuaskan'])

rule3 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['tidak memuaskan'])

rule4 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['tidak memuaskan'])

rule5 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['tidak memuaskan'])

rule6 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['cukup memuaskan'])

rule7 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['tidak memuaskan'])

rule8 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])

rule9 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['cukup memuaskan'])

rule10 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])

rule11 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])

rule12 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])

rule13 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])

# SISTEM
sistem_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13])
sistem = ctrl.ControlSystemSimulation(sistem_ctrl)

# INPUT DATA SOAL
sistem.input['informasi'] = 80
sistem.input['persyaratan'] = 60
sistem.input['petugas'] = 50
sistem.input['sarpras'] = 90

# PROSES
sistem.compute()

# OUTPUT
# print("Nilai Kepuasan:", sistem.output['kepuasan'])

# Visualisasi
informasi.view()
persyaratan.view()
petugas.view()
sarpras.view()

kepuasan.view(sim=sistem)

# Tampilkan semua jendela grafik (non-blocking)
plt.show(block=False)

# Tahan jendela terminal agar tidak langsung tertutup
input("\nTekan Enter pada terminal untuk keluar dan menutup semua grafik...")
plt.close('all')