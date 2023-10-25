coleta = {'Aedes aegypt': 32, 
          'Aedes albopictus': 22,
          'Anopheles darlingi': 14}

print(coleta['Aedes aegypt'])

coleta['Rhodnius montenegrensis'] = 11

print(coleta)

print()
# del(coleta)

print(coleta.items())

print()

print(coleta.keys())

print()

print(coleta.values())


coleta2 = {'Anopheles gambiae': 13,
           'Anopheles deaneorum': 14}

coleta.update(coleta2)

print()

print(coleta)

print()

for especie, num_especimes in coleta.items():
    print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')