# date:2019/11/27
# author:pomelo


f = open('IOprac.txt', 'r')
print(f.read())
f.close()

try:
    f = open('IOprac.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
with open('IOprac.txt', 'r') as f:
    print(f.read())
with open('IOprac.txt', 'a') as f:
    f.write('\nHello,pomelo!')
with open('IOprac.txt', 'r') as f:
    print(f.read())



