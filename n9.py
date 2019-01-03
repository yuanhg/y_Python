from datetime import datetime
def divi9():
    begin=datetime.now()
    for n in range(123456789,987654321):
        if   str(n).count("0")>0:
            continue
        elif str(n).count("1")>1:
            continue
        elif str(n).count("2")>1:
            continue
        elif str(n).count("3")>1:
            continue
        elif str(n).count("4")>1:
            continue
        elif str(n).count("5")>1:
            continue
        elif str(n).count("6")>1:
            continue
        elif str(n).count("7")>1:
            continue
        elif str(n).count("8")>1:
            continue
        elif str(n).count("9")>1:
            continue

        if n%9 != 0:
            continue
        elif n//10%8 !=0:
            continue
        elif n//100%7 !=0:
            continue
        elif  n//1000%6 !=0:
            continue
        elif n//10000%5 !=0:
            continue
        elif n//100000%4 != 0:
            continue
        elif n//1000000%3 != 0:
            continue
        elif n//10000000%2 != 0:
            continue
        else:
            print("time lasting:",datetime.now()-begin)
            print(n)

    print("the finish time last is :",datetime.now()-begin)

if __name__ == "__main__" :
    divi9()
