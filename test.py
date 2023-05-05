"""from random import randint
def tri_double(T):
    for i in range(len(T)//2):
        maxi = len(T) - i - 1
        max_i = len(T) - i - 1
        mini = i
        
        for j in range(i+1,len(T)-i):
            if T[mini] > T[j]:
                mini = j
            if T[maxi] < T[j]:
                maxi = j
        #minimum
        temp = T[i]
        T[i] = T[mini]
        T[mini] = temp
        #maximum
        temp = T[maxi]
        T[maxi] = T[max_i]
        T[max_i] = temp
        

T = [randint(0,100)for i in range(20)]
print(T)
tri_double(T)
print(T)"""

T = [1,2,3,4,5]
i = 0
while i < 10:
    if i < len(T):
        print(T[i])
    else:
        print(T[i-len(T)], "au dessus")
    i = i+ 1