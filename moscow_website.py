j = r"""
 __  __
|  \/  | ___  ___  ___ _____      __
| |\/| |/ _ \/ __|/ __/ _ \ \ /\ / /
| |  | | (_) \__ \ (_| (_) \ V  V /
|_|  |_|\___/|___/\___\___/ \_/\_/

"""
print("\033[0;32m",j)
print("script by Moscow\n")

try:
    from googlesearch import *
    print("bo darchon zhamra 99 banwsa\n\n")   
    m = 0
    while m < 10:
        try:
            m += 1
            x = input("\033[0;31m Lyra dorkea banwsa:   ")
            y = int  (input("Chan websitet dawya bot bahynea ==>  "))

            if (x == '99'):
                break
            
            elif (y == 99):
                break
            
            for t in search(str(x),stop=y):
                print(t)
                print("\n\n")
            print("============================  kotye  ============================\n")

                
        except ValueError:
            print("\n<==============================  halya  ==============================>\n")
            
except ModuleNotFoundError:
    import os
    os.system("pip install google")
