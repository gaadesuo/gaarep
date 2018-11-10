# -*- coding: utf-8 -*-
__author__ = "gaa"
__date__ = '2018/11/09 09:14'


def print_picnic(items_dict, left_width, right_width):
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for k, v in items_dict.items():
        print(k.ljust(left_width, ".") + str(v).rjust(right_width))


picnic_items = {"sandwiches": 4, "apples": 12, "cups": 4, "cookise": 8000}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)