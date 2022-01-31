print('\033[32;1m  Veja quanto vale seu Real em Dólar')
rs = float(input('  Quanto reais você tem?\n  — ').strip().replace(" ", ""))
uss = rs / 3.27 #considerando que USs 1.00 == Rs 3.27

print('  Você pode comprar {:.2f} Dólares com seus {:.2f} Reais'.format(uss, rs))