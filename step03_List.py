#list type에 대해서 알아보자
nums=[1,2,3]
names=["k","l","j"]
#nums에 4 추가
nums.append(4)
#lens()힘수를 이용해서 list의 길이를 얻어낼수 있다.
nums_len = len(nums)
print(nums)
#인덱스를 이용해 삭제
del names[0]
#값에 의한 삭제
names.remove("j")
#맨마지막 index를 삭제하면서 값을 가져오기
#nums.pop()
result = nums.pop()
print(nums)
print(names)