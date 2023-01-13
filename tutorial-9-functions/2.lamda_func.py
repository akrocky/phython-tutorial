# products =[
#     ("Product-1",15),
#     ("Product-2",25),
#     ("Product-3",5),
#     ("Product-4",45),
#     ("Product-5",20),
#   ]
# products.sort(key=lambda product: product[1])
# print(products)
# labda  +filter

my_list = [1, 5, 4, 6, 7, 11, 3, 12, 34]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)
# for num in new_list:
#    print(num)
# even_nums = list(new_list)
# print(even_nums)
