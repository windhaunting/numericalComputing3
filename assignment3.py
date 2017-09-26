import numpy as np

####################################################
# Problem 1: Data filtering
####################################################
housing_data = np.loadtxt("boston.csv",delimiter=',')
        
## Add code here ##
#question 1:
#get total entry 
totalNum = housing_data.size
totalNan = np.sum(np.isnan(housing_data)) #np.count_nonzero(np.isnan(housing_data))
print ("percentage: ", totalNan, totalNum, totalNan/totalNum)



####################################################
# Problem 2: Data exploration
####################################################
iris_data = np.loadtxt("iris.csv",delimiter=',',skiprows=1)
    
## Add code here ##
