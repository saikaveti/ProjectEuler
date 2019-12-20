import sys

max = int(sys.argv[1])

head = 2
second = 1

sum = 0

while head < max:
  if head % 2 == 0:
    sum += head
  
  new_head = head+second
  second = head
  head = new_head

print(sum)
