#Secuencia de Fibonacci
#Forma recursiva
# fn = fn-1 + fn-2
def fib_r(n):
	if n < 2:
		return n
	return fib_r(n-1) + fib_r(n-2)
for x in range(int(input())):
	print(fib_r(x))
