def tao_tuple_tu_list(lst):
    return tuple(lst)

#Nhập danh sách số từ bàn phím
input_list = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple: ", my_tuple)
#Nhập danh sách số từ bàn phím