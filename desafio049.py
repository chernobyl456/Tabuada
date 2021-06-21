titulo = str("Tabuada 2.0")
print("\033[1;32m{:=^40}\033[m".format(titulo))
num = int(input('Digite um número: '))
for x in range(0, 11):
    print(f'\033[0;36m{x}x{num} = {num * x}\033[m')
