#lst = "red,orange,yellow,green,blue,purple,pink,brown,black,white,gray,violet,indigo,maroon,navy"
lst = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20"
#lst = "dog,cat,elephant,giraffe,lion,tiger,zebra,monkey,penguin,kangaroo,koala,panda,bear,wolf,fox"

lst = lst.split(",")

print(lst)

lst_middle = len(lst) // 2

print(lst[1::3])
print(lst[5::-1])
print(lst[lst_middle::2])