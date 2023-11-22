from typing import List


class DiagonaTraverse:
    """
    Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images
     (click the link).
     link: https://leetcode.com/problems/diagonal-traverse-ii/description/
    """
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        res_d = []
        len_list = [len(l) for l in nums]
        num_cols = num_rows = max(len(nums), max(len_list))
        if len(nums) == 1:
            return nums[0]
        num_diags = num_rows + num_cols - 1
        i = j = 0
        i_diag = 1
        i_d = num_rows - 1
        j_d = num_cols - 1
        while i_diag <= num_diags // 2:

            # ascendant
            for el in range(i_diag):
                try:
                    res.append(nums[i][j])
                    j += 1
                    i -= 1
                except:
                    j += 1
                    i -= 1
                try:
                    res_d.append(nums[i_d][j_d])
                    j_d -= 1
                    i_d += 1
                except:
                    j_d -= 1
                    i_d += 1

            i_diag += 1
            j = 0
            i = i_diag - 1

            i_d = num_rows - i_diag
            j_d = num_cols - 1
        for el in range(i_diag):
            try:
                res.append(nums[i][j])
                j += 1
                i -= 1
            except:
                # print("up (i, j) = ", (i, j))
                j += 1
                i -= 1
        return res + res_d[::-1]


if __name__ == '__main__':
    dt = DiagonaTraverse()
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(dt.findDiagonalOrder(nums))
