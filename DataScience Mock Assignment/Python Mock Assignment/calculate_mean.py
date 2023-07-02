def calculate_mean(ls):
    tot_sum=sum(ls)
    #t=0
    #for i in ls:
 #    t+=i
    n=len(ls)
    mean=tot_sum/n
    return mean
ls=[1,2,3,4,5,6,7,8,9,10]
mean=calculate_mean(ls)
print(f"Mean of {ls} is {mean}") # Mean of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is 5.5
