arr=[20,10,30,40,50]
l=len(arr)
for i in range(1,l-1):
    if arr[i-1]>arr[i]:
        print(arr[i-1])
    elif arr[i-1]<arr[i] and arr[i]>arr[i+1]:
        print(arr[i])
    if arr[i]==arr[l-2]:
        if arr[i+1]>arr[i]:
            print(arr[i+1])