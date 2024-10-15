import matplotlib.pyplot as plt

a = int(input("Enter a positive integer: "))
values = [a,]
steps = [0,]

while (a!=1):
    steps.append(steps[-1]+1)
    if a%2==0:
        a/=2
    else:
        a = 3*a+1
    values.append(a)


plt.plot(steps,values)
plt.show()

