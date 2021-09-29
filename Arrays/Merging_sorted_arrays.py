from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        for i in range(n2):
            nums1.pop(len(nums1)-1)
            
        for i in range(n2):
            nums1.append(nums2[i])
        
        return nums1.sort()

