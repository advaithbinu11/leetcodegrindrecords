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
                    
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
            left = 0
            right = len(matrix) - 1
            while (left<right):
                mid = (left + right) // 2
                if(matrix[mid][0] < target):
                    left = mid + 1
                elif(matrix[mid][0] > target):
                    right = mid
                else:
                    return True
            mid = (left + right) // 2
            currRow = mid if matrix[mid][0] <= target else mid - 1
            left = 0
            right = len(matrix[currRow])
            print(currRow)
            while (left<right):
                mid = (left + right) // 2
                if(matrix[currRow][mid] < target):
                    left = mid + 1
                elif(matrix[currRow][mid] > target):
                    right = mid
                else:
                    return True
            return False
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 1
        right = len(nums) - 1
        arr = [-1] * 2
        if(len(nums) == 0):
            return arr
        mid = (left + right) // 2
        while(left <= right):
            if(nums[mid] == target and nums[mid-1] != target):
                arr[0] = mid
                break
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        if(nums[0] == target):
            arr[0] = 0
        left = 0
        right = len(nums) - 2
        mid = (left + right) // 2
        while(left <= right):
            if(nums[mid] < target):
                left = mid + 1
            elif(nums[mid] == target and nums[mid+1] == target):
                left = mid + 1
            else:
                right = mid - 1
            if(nums[mid] == target and nums[mid+1] != target):
                arr[1] = mid
                break
            mid = (left + right) // 2
        if(nums[len(nums) - 1] == target):
            arr[1] = len(nums) - 1
        return arr
    
        
