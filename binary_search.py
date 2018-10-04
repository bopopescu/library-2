

def binary_search(data, target, low, high):
    try:
        if(low > high):
            return False
        else:
            mid = int((low + high)/2)
            if(target == data[mid]):
                return True
            elif(target <= data[mid]):
                return binary_search(data, target, low, mid-1)
            else:
                return binary_search(data, target, mid + 1, high)

    except Exception as e:
        return False

d = (1,2,3,4,5,6,7,8,9,10)
res = binary_search(d, 0, 1,10)
print(res)