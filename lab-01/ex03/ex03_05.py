def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

#Nhập danh sách số từ bàn phím
input_string = input("Nhập vào danh sách các từ, cách nhau bởi dấu cách: ")
word_list = input_string.split()

#Sử dụng hàm để đếm số lần xuất hiện của từng phần tử
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của từng phần tử trong danh sách là: ", so_lan_xuat_hien)