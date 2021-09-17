times = ('Corinthians',"Palmeiras","Santos","Gremio","Cruzeiro","Flamengo","Vasco da gama","Chapecoense",
"Atletico mineiro","Botafogo","Atletico paranaense","Bahia","São Paulo","Fluminense","Sport Recife","Vitória",
"Curitiba","Avai","Ponte preta","Atletico goianiense")
print("-=" * 30)
print(f'Lista de times {times}')
print("-=" * 30)
print(f"Os 5 primeiros times são {times[0:5]}")
print("-=" * 30)
print(f"Os 4 ultimos colocados são {times[-4:]}")
print("-=" * 30)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 30)
print(f'A chapecoense está em {times.index("Chapecoense")}° lugar')