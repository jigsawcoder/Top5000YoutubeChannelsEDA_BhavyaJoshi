def chopstick(arr,d):
    counter = 0
    for x in arr:
        for y in arr:
            diff = int(abs(arr[x] - arr[y]))
            while (diff <= d):
                counter += 1
    return counter
                


n = input("Enter the number of chopstick: \n")
d = input("Enter the max diff: \n")
n = int(n)
d = int(d)

arr = []*n

arr = input("Enter the lengths: \n")

print(arr)

pairs = chopstick(arr,d)

print(pairs)
