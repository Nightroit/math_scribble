n = 100

prime = [True for i in range(n+1)]
for i in range(n+1): 
    prime[i] = True

for i in range(2, n):
    for j in range(i*i, n+1, i): 
        prime[j] = False

for i in range(n): 
    if prime[i] == True: 
        print(i)


#Obj: How to compute primes between large numbers. Between 1m and 1m + 1000