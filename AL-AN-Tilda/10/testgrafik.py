from molgrafik import *
ruta1 = Ruta(atom = "C")
ruta2 = Ruta(num = 3)
ruta3 = Ruta(atom = "O", num = 2)
ruta4 = Ruta(atom = "H")
ruta1.next = ruta2
ruta2.down = ruta3
ruta3.next = ruta4
grafik = Molgrafik()
grafik.show(ruta1)