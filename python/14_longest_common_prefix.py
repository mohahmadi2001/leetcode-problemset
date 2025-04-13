def longest_common_prefix(strs:[str]):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

def longest_common_prefix_1(strs:[str]):
    res = ""
    for chars in zip(*strs):
        if all(c == chars[0] for c in chars):
            res += chars[0]
        else:
            break
    return res


def longest_common_prefix_2(strs:[str]):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix