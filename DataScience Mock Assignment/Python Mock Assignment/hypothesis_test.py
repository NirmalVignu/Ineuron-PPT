from scipy import stats

def perform_hypothesis_test(sample1, sample2):
    t_statistic, p_value = stats.ttest_ind(sample1, sample2)
    return p_value

sample1 = [2,4,6,8,10]
sample2 = [1,3,5,7,9]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value) #P-value: 0.6305360755569764

