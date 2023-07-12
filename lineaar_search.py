def linear_search(array,number_occured):
    count=0
    for i in range(len(array)):
        if(array[i]==number_occured):
            count+=1
    return count
array=list(map(int,input().split()))
number_occured=int(input())
print(linear_search(array,number_occured))    