def findPath(num):
  arr = [[1]]
  num = num + 1
  for i in range(1, num):
    arr1 = []
    for k in range(0, i+1):
      if k < 1:
        num1 = 0
      else:
        num1 = arr[i - 1][k - 1]
      if k > i - 1:
        num2 = 0
      else:
        num2 = arr[i - 1][k]
      arr1.append(num1 + num2)
    arr.append(arr1)
  
  for i in range(0, num - 1):
    arr1 = []
    for k in range(0, num-i-1):
      num1 = arr[num + i - 1][k]
      num2 = arr[num + i - 1][k + 1]
      arr1.append(num1 + num2)

    arr.append(arr1)
  return arr[-1][0]

print(findPath(20))