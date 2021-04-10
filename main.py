from tri.tri_insertion import tri_insertion

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tab1 = [6, 2, 0, 5, 4, 1, 3]
    tab2 = [6, 2, 0, 5, 4, 1, 3]
    print("non sorted tab: ", tab1)
    tab_sorted_desc = tri_insertion(tab1, "-")
    print("sorted tab descending order: ", tab_sorted_desc)
    tab_sorted_asc = tri_insertion(tab2)
    print("sorted tab ascending order: ", tab_sorted_asc)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
