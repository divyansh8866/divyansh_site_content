---
weight: 1
title: "Leetcode - Finding piviot index"       # <<< Change here
date: 2022-10-21T16:33:23+00:00
lastmod: 2022-10-21T16:33:23+00:00
draft: false                
author: "Divyansh"
authorLink: "https://divyanshpatel.com"
description: "Change Me"                    # <<< Change here
images: []
resources:
- name: "Leetcode"
  src: "leetcode.png"

tags: ["python", "leetcode"]     # <<< Change here
categories: ["Leetcode"]               # <<< Change here

lightgallery: true

toc:
  auto: false
---

![leetcode](leetcode.jpeg)

# Finding piviot index
`Python ` `leetcode` `data structure` `algorithems`

---

> Developer : __Divyansh Patel__

## Question

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

## Solution
### Method 1
solved using consecept of slicing the list. This method is inefficient for large list and large numbers. Go to second method.
``` python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if i==len(nums):
                if sum(nums[:i])==0 :
                    return i 
                else :
                    continue
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1
```
### Method 2
sloved using the summing and dividing equaly.
``` python 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        targeted_sum = 0
        for i,v in enumerate(nums):
            targeted_sum = (total_sum -v)/2
            # print(f"right sum should be {i} : {targeted_sum} ")
            if (targeted_sum-int(targeted_sum))==0:
                if sum(nums[:i])==targeted_sum:
                    # print(f"Is Piviot index {i}")
                    return i
                else :
                    continue
        return -1
```

