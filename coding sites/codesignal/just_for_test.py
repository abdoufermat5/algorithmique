# from collections import defaultdict
# def mostBalancedPartition(parent, files_size):
#     # get directories with their files
#     directories_with_f = {}
#     for i in range(len(parent)):
#         test = directories_with_f.get(parent[i]+1, -1)
#         if test == -1:
#             directories_with_f[parent[i]+1] = files_size[i]
#         else:
#             directories_with_f[parent[i]+2] = files_size[i]
#     return dict(directories_with_f)
# d = mostBalancedPartition([-1, 0, 0, 1, 1, 2], [1, 2, 2, 1, 1, 1])
# print(d)


def binaryPatternMatching(pattern, s):
    n = len(pattern)
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    transformed_s = ''.join([str(int(c in vowels)) for c in s])
    res = 0
    for i in range(len(transformed_s)):
        if n+i <= len(transformed_s):
            if transformed_s[i:n+i] == pattern:
                res += 1
        else:
            break
    return res

s = 'codesignal'
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
transformed_s = ''.join([str(int(c not in vowels)) for c in s])
print(transformed_s)