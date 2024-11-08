população_a = 80000
população_b = 200000
taxa_a = 0.03
taxa_b = 0.015
anos = 0
while  população_a < população_b :
    população_a += população_a * taxa_a
    população_b += população_b * taxa_b
    anos += 1
print(f"a quantidade de anos para que a população de a alcance a população de b é de {anos} anos")

