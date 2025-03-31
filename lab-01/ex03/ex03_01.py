def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập vào một dãy số, cách nhau bởi dấu cách: ")
numbers = [int(x.strip()) for x in input_list.replace(' ', '').split(',')]

tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong dãy là: ", tong_chan)