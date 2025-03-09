#x = int(input())
#y = int(input())
#z = int(input())
#n = int(input())
x=y=z=1
n=2

newlist = [[[[k,j,i] for i in range(0,x+1) if i+j+k!=n] for j in range(0,y+1)] for k in range(0,z+1)]

newlist2 = [[i for i in range(0,3)],[j for j in range(0,3)],[k for k in range(0,3)]]

newlist3 = [[[j,k] for k in range(0,3)] for j in range(0,3)]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

odd_numbers = [
    element for row in matrix for element in row if element % 2 != 0]

print(odd_numbers)

print(newlist3)

nums = [n**2 for n in range(1000000)]

nums_gen = (n**2 for n in range(1000000))

# Hackerrank Basic Data Types


