N = 5
for i in range(N):
	for j in range(N - i):
		print('-', end='')
	print('/', end='')
	for j in range(i * 2):
		print(',', end='')
	print('\\', end='')
	for j in range(N - i):
		print('-',end='')
	print()
for i in range(N - 1, -1, -1):
	for j in range(N - i):
		print('-', end='')
	print('\\', end='')
	for j in range(i * 2):
		print(',', end='')
	print('/', end='')
	for j in range(N - i):
		print('-',end='')
	print()
