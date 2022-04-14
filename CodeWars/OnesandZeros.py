def binary_array_to_number(arr):
    value=0
    arr.reverse()
    for i in range(len(arr)):
        
        value+=arr[i]*(2**i)
    
    return value
  
print(binary_array_to_number([0,0,1,0]))