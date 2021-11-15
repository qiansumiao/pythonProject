#判断是否存在重复元素
nums = [1,1,1,3,3,4,3,2,4,2]

class Solusion:
    def duplicate(self,nums):
        s = set(nums)
        List = list(s)
        if len(nums) == len(List):
            return False
        else:
            return True

s = Solusion()
print(s.duplicate(nums))