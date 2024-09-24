def sort_list(lis,lis2):
    if len(lis2)<1:
        return []

    return [lis[i]*lis2[0] for i in range(len(lis)) ]+sort_list(lis,lis2[1:])


mlis=[2,4,6,8]
mlis2=mlis
new_list=sort_list(mlis,mlis2)
print(new_list)