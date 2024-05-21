def main(a):       #parameters default
    print(a,"hello world")

main(12)   #arguments   default
main(a = 13)   #keywords using 


def oddeven(a):
    if a%2 == 0:
        # print("even")
        return ("even")    # function se kisi value ko return karne ke liye jahan se value call hua hai
    else:
        # print("odd")
        return ("odd")

print(oddeven(13))        