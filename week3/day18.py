class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        list = []
        nums.sort()
        primaryI = set()
        for i in range(0, len(nums)-2):
            secondJK = set()
            target = 0 - nums[i]
            if(not nums[i] in primaryI):
                j = i + 1
                k = len(nums)-1
                while(j < k):
                    sum = nums[j] + nums[k]
                    if(sum<target):
                        j += 1
                    elif(sum > target):
                        k -= 1
                    elif(not nums[j] in secondJK and sum == target):
                        secondJK.add(nums[j])
                        secondJK.add(nums[k])
                        arr = [0] * 3
                        arr[0] = nums[i]
                        arr[1] = nums[j]
                        arr[2] = nums[k]
                        list.append(arr)
                        j+=1
                        k-=1
                    else:
                        j+=1
                primaryI.add(nums[i])
        return list
                    

        
