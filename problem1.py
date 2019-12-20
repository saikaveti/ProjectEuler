import sys

max = int(sys.argv[1])
total = 0;

for i in range(0, max):
  if i % 3 == 0 or i % 5 == 0:
    total += i;

print(total)
