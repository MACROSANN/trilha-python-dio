salario = int(input()) 

if salario <= int(600):
    reajuste = 0.17
    reajustado = reajuste * 100
    ganho = salario * reajuste
    novo = salario + ganho
    print(f"Novo salario: {novo:.2f}")
    print(f"reajuste ganho: {ganho:.2f}")
    print(f"Em percentual: {reajustado:.2f} %")
  
elif salario <= int(900):
    reajuste = 0.13
    reajustado = reajuste * 100
    ganho = salario * reajuste
    novo = salario + ganho
    print(f"Novo salario: {novo:.2f} Reajuste ganho: {ganho:.2f} Em percentual: {reajustado:.2f} %")
  
elif salario <= int(1500):
    reajuste = 0.12
    reajustado = reajuste * 100
    ganho = salario * reajuste
    novo = salario + ganho
    print(f"Novo salario: {novo:.2f} Reajuste ganho: {ganho:.2f} Em percentual: {reajustado:.2f} %")
  
elif salario <= int(2000):
    reajuste = 0.10
    reajustado = reajuste * 100
    ganho = salario * reajuste
    novo = salario + ganho
    print(f"Novo salario: {novo:.2f} Reajuste ganho: {ganho:.2f} Em percentual: {reajustado:.2f} %")
  
else: 
    reajuste = 0.05
    reajustado = reajuste * 100
    ganho = salario * reajuste
    novo = salario + ganho
    print(f"Novo salario: {novo:.2f} Reajuste ganho: {ganho:.2f} Em percentual: {reajustado:.2f} %")
