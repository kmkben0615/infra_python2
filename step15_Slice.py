#Step15_slice.py

nums = [10,20,30,40,50]
       #0  1  2  3  4
print(nums[1:])#1 인데스부터 끝까지
print(nums[2:])
print(nums[3:])

print("----------------")
print(nums[:3])#3번쨰 인덱스 미만
print(nums[:2])#
print(nums[:1])

print("----------------")
print(nums[1:4])#인덱스1 이상 4 미만 즉 30,40


print("----------------")
print(nums[::1])#1씩 증가
print(nums[::2])#2씩 증가
print(nums[::3])#3씩 증가
