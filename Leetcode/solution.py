N = [n > 0 for n in nums]
negl = []
for a in N:
    if (-1)*a in nums:
        negl.append(a)
    if len(negl) != 0:
        ret = max(negl)
        return ret
    else:
        return -1