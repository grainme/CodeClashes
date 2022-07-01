'''Input:
N = 6
arr[] = 7 10 4 3 20 15
---> sorted(arr) = 3 4 7 10 15 20
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.'''


N = int(input())
arr = (map(int,input().split()))
k = int(input())
print(f"{k} smallest element in the given array is {sorted(arr)[k-1]}")
