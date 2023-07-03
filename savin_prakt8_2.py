print("Введите натуральное число не более 100 000")
n=int(input())
print("Введите через пробел",n,"натуральных чисел, величиной не более 1000 000 000")

m=input().split()

m_new=[]
m_new.append(m[-1])

i=0
for i in range(n-1):
    m_new.append(m[i])


print(m_new)
