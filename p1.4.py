def old_list(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

k = [" krish, om, sheryesh, palak",]
print("LIST :", k)
s1 = 3
s2 = 0
new_list = old_list (k, s1, s2)
print("NEW_LIST : " , new_list)
