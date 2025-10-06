list_1 = list(map(str, input().split()))
list_2 = list(map(str, input().split()))


#

all_elements  = list_1+list_2
print(all_elements)

unique_elements = set(all_elements)
print(unique_elements)