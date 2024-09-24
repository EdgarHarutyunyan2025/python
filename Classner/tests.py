class MyList:
    def __init__(self,list1) :
        self.list1=list1

    def __add__(self,lis):
        if isinstance(lis,list):
            return self.list1+lis
        if isinstance(lis,str):
            st_lis=list(self.list1)
            st_lis.append(lis)
            return st_lis
        if isinstance(lis,int):
            int_lis=list(self.list1)
            int_lis.append(lis)
            return int_lis
        if isinstance(lis,MyList):
            return self.list1 + lis.list1
    
    def binery_search(self,lis,num):
        if type(lis)!=list:
            print('TypeError: first argument must be a list')
            return 0
        if type(num)!=int:
            print('TypeError: second argument must be a number')
            return 0
        low=0
        high=len(lis)-1
        while low<=high:
            mid=(low+high)//2
            guess=lis[mid]
            if guess==num:
                print(mid)
                return mid
            if guess>num:
                high=mid-1
            else:
                low=mid+1

    def selectionSort(self,arr):
            if type(arr)!=list:
                print('TypeError: second argument must be a number')
                return 0
            
            def smallest(arr):
                el=arr[0]
                el_index=0
                for i in range(1,len(arr)):
                    if arr[i]<el:
                        el=arr[i]
                        el_index=i

                return el_index

            def  selection_sort(arr):
                sort_list=[]
                for i in range(len(arr)):
                    smalles=smallest(arr)
                    sort_list.append(arr.pop(smalles))
                return sort_list
            
            return selection_sort(arr)
        
    def bubble_sort(self,lis):
        if type(lis)!=list:
                print('TypeError: second argument must be a number')
                return 0
        for i in range(len(lis)-1,0,-1):
            flag=False
            for j in range(i):
                if lis[j]>lis[j+1]:
                    flag=True
                    lis[j],lis[j+1]=lis[j+1],lis[j]
        if not flag:
            return lis




list11=[2,7,9,4,5,3,1]
list22=[88,94,98,100,180,196]
myclasslist=MyList(list11)
myclasslist2=MyList(list22)
#print(myclasslist+myclasslist2)
#print(myclasslist.selectionSort(list11))
#myclasslist.binery_search(list11,77)
myclasslist.bubble_sort(list11)
print(list11)



     
