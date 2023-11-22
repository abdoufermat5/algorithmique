class ZigZagConvert:
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)
    Link: https://leetcode.com/problems/zigzag-conversion/
    """
    def convert(self, s: str, numRows: int) -> str:
        v = [""] * numRows
        i = 0
        chosen_row = numRows - 2
        while i < len(s):
            # remplir la colonne
            for j in range(numRows):
                if i < len(s):
                    v[j] += s[i]
                    i += 1
                else:
                    break
            # remplir la diagonale
            for j in range(chosen_row, 0, -1):
                if i < len(s):
                    v[j] += s[i]
                    i += 1
                else:
                    break
        return "".join(v)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    sol = ZigZagConvert()
    res = sol.convert(s, 4)
    print(res)
