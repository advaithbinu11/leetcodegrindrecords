class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        pivot = 0
        while(left < right and right > 1):
            print(str(left)+" "+str(right))
            mid = (left + right) // 2
            if (nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]):
                pivot=mid
                break
            elif(nums[mid]<nums[right]):
                right = mid
            else:
                left = mid + 1
        if(pivot == 0 and nums[0] >nums[len(nums)-1]):
            pivot = len(nums) - 1
        print(pivot)
        if(nums[pivot] <= target and target <= nums[len(nums)-1]):
            left = pivot
            right = len(nums) - 1
        elif(target >= nums[0]):
            left = 0
            right = pivot-1
        else:
            return -1
        while(left <= right):
            mid = (left + right) // 2
            if (nums[mid]==target):
                return mid
            elif(target < nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
