from statistics import mean
import math

def k_means(k_list,elements,no_of_elements,value_of_k):
	i=j=0
	diff=[]
	copy_list=[]
	count=0
	while True:
		copy_list=k_list[0].copy()
		count+=1
		for i in range(no_of_elements):
			diff=[]
			for j in range(value_of_k):
				diff.append(abs(k_list[0][j]-elements[i]))
			indx=diff.index(min(diff))
			k_list[indx+1].append(elements[i])
		print(count,"iteration:")
		for i in range(1,(value_of_k+1),1):
			print("k",(i),":",k_list[i],"=",k_list[0][i-1])
		for i in range(value_of_k):
			k_list[0][i]=mean(k_list[i+1])
		if copy_list == k_list[0] :
			print("Since the clusters consists same elements, the final clusters are:")
			for i in range(1,(value_of_k+1),1):
				print("k",(i),":",k_list[i],"=",k_list[0][i-1])
			break
		for i in range(value_of_k):
			k_list[i+1]=[]
#-------------------------------------------------------------------#			

no_of_elements=int(input("Enter total number of elements:"))
value_of_k=int(input("Enter value of K:"))
elements=[]
print("Enter the elements:")
for i in range(no_of_elements):
	elements.append(int(input()))
k_list = [[] * no_of_elements for p in range(no_of_elements)]
for j in range(value_of_k):
	k_list[0].append(elements[j])
print("elements:",elements)
print("random k values:",k_list[0])	
k_means(k_list,elements,no_of_elements,value_of_k)	
