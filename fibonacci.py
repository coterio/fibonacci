from time import sleep
import os
prossegue = "s"
while(prossegue == "s"):
    error = "n"
    while(error == "n"):
        try:
            os.system("clear")
            terms = input("Deseja ver quantos termos de Fibonacci?\n")
            terms = int(terms)
            break
        except ValueError:
            print("\nDigite um número válido!")
            sleep(2)
            continue
    print(f"\n{terms} termos de Fibonacci:\n\n1\n1")
    num1, num2 = 1, 1
    i = 2
    velo = 1
    while(i != terms):
        resu = num1 + num2
        print(f"{resu}")
        num1 = num2
        num2 = resu
        i += 1
        sleep(velo)
        velo *= 0.9
    print("\n\nchega fi cabo a graca")
    prossegue = input("Deseja ver mais?(s/n)")
