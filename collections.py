nums = [0,0,98]
firstset=set(nums)
zeroset = {0}
if firstset - zeroset == set():
    print("y") 
else:
    print("n")
    for i in range(len(nums)):
        print(nums[i])