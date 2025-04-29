skore = []
for i in range(10):
    cislo = int(input("zadejte skóre"))
    skore.append(cislo)
print(skore)

prumer=sum(skore)/10
print(prumer)
print(max(skore))
print(min(skore))
for i in skore:
    print(i)
if prumer >250:
    print("výborný výkon")
else:
    print("příště to můžete zkusit lépe")
