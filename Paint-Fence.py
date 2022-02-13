'''
Given a fence with n posts and k colors, 
find out the number of ways of painting the fence 
such that at most 2 adjacent posts have the same color. 
'''

def paintFence(posts, colors):
    if colors == 0 or posts == 0:
        return 0

    if n == 1:
        return colors
    
    same = colors
    diff = colors * (colors - 1)

    for _ in range(3, n + 1):
        same, diff = diff, (same + diff) * (colors - 1)

    return same + diff