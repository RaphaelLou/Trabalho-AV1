n = int(input('A sequência de Fibonacci de: '))
p, s = 0, 1
while p < n:
    yield p
    print('- {}'.format(p), end ='')
    p, s = s, p+s
print('FIM')