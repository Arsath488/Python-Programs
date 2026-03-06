def average(array):
    
    distinct_elements = set(array)
    
 
    result = sum(distinct_elements) / len(distinct_elements)
    
   
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)