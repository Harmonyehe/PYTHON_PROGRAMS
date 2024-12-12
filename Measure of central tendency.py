#mean

data=[12,18,14,20,16]
mean=sum(data)/len(data)
print(f"Mean: {mean}")

sorted_D=sorted(data)

n=len(sorted_D)

median=(sorted_D[n//2]+sorted_D[(n-1)//2])/2
print(f"Median: {median}")

from statistics import mode
mode_val=mode(data)
print(f"Mode: {mode_val}")
