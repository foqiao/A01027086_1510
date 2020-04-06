import time

product = 1
startTime = time.time()
print(startTime)
for i in range(1, 100000):
    product = product * i
endTime = time.time()
print('The result is %s digits long.' % (len(str(product))))
print('Took %s seconds to calculate.' % (endTime - startTime))



