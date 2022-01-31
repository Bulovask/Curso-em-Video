print('\033[32m Conversor de METROS para CENTIMETROS e MILÍMETROS.')
m = float(input('  Por favor, digite um valor em metros:\n  => '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000

print('  {:.3f}km = {:.3f}hm {:.3f}dam = {:.3f}m = {:.3f}dm = {:.3f}cm = {:.3f}mm'.format(km, hm, dam, m, dm, cm, mm))