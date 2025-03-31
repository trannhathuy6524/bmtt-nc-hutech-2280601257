def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

#Nhập tuple từ bàn phím
input_tuple = eval(input("Nhập vào một tuple, cách nhau bởi dấu phẩy: "))
first, last = truy_cap_phan_tu(input_tuple)

#In ra phần tử đầu tiên và cuối cùng của tuple
print("Phần tử đầu tiên trong tuple là: ", first)
print("Phần tử cuối cùng trong tuple là: ", last)   