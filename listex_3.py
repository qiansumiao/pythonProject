#旋转数组
nums = [1,2,3,4,5,6,7]
k =3

result = nums[-k:] + nums[:k]

print(result)