'''
The sum we are looking for is the sum of the multiples of 3 below 1000 and multiples of 5 below 1000, 
minus the sum of the multiples of 15 below 1000 by the inclusion-exclusion principle. 
Then, we have 3 + 6 + ... + 999 = 333(3+999)/2
5 + 10 + ... + 995 = 199(5+995)/2
15 + 30 + ... + 990 = 66(15+990)/2
'''
print(int((333*1002/2)+(199*1000/2)-(66*1005/2)))