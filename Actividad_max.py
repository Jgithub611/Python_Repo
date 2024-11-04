#Dados n enteros en una matriz unidimensional sucesiva, escriba un algoritmo que encuentre cuándo se maximiza la suma de los valores sucesivos de la matriz
def maximum_subarray(S):
    max_end = 0
    max_sum = float('-inf')
    for num in S:
        max_end = max(num, max_end + num)
        max_sum = max(max_sum, max_end)
    return max_sum
S=[-2,1,-2,4,-1,2,1,-5,4]
M=maximum_subarray(S)
print(M)