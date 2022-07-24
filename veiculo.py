roda = int (input("Quantas rodas o veículo possui? "))
peso = float (input("Qual o peso do veículo? "))
pessoa = int (input("Quantas pesoas cabem no veículo? "))

if roda<=3:
    print ("Sua categoria é A!")
elif (roda==4) and (pessoa<=8) and (peso>=3500):
    print ("Sua categoria é B!")
elif (roda > 4) and (peso>=3500.01 and peso<6000):
    print ("Sua categoria é C!")
elif (roda>=4) and (pessoa>8):
    print ("Sua categoria é D!")
else:
    print ("Sua categoria é E!")