'''
Given an integer array of unique elements,
return all subsets
'''

def dfs(nums, index, path, res):
    print(path)
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], res)

def subsets(nums):
    res = []
    dfs(nums, 0, [], res)
    return res

print(subsets([1,2,3]))