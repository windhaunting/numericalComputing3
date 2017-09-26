import numpy as np

####################################################
# Problem 1: Data filtering
####################################################
housing_data = np.loadtxt("boston.csv",delimiter=',')
        
## Add code here ##
#may not use any for or while loops in your code
#question 1:
totalNum = housing_data.size        #get total entry 
totalNan = np.sum(np.isnan(housing_data)) #np.count_nonzero(np.isnan(housing_data))        ; get total Nan
percentage = totalNan/totalNum
print ("percentage of Nan entry in all entry: ", percentage)

#question 2
nanRowsNum = np.sum(np.isnan(housing_data).any(axis=1))           #check each row contains any one Nan
print ("number of rows with Nan: ", nanRowsNum)


#question 3
nanNumColumns = sum(np.isnan(housing_data))                   #check how many Nan in each column
print ("number of Nan in each column: ", nanNumColumns)

#question 4                                                  #the average value of each column, ignoring all rows containing at least one NaN value?        
newArray = housing_data[~np.isnan(housing_data).any(axis=1)] 
averageColumn1 = sum(newArray)/newArray.shape[0]                                        
print ("avearge of each column ignoring all Rows with at least One Nan: ", averageColumn1)

#question 5
sumColumns2 = np.nansum(housing_data, axis=0)/(housing_data.shape[0]-nanNumColumns)    
print ("avearge of each column ignoring Nan values only: ", sumColumns2)


####################################################
# Problem 2: Data exploration
####################################################
iris_data = np.loadtxt("iris.csv",delimiter=',',skiprows=1)
    
## Add code here ##
#question 1
#print (np.bincount(iris_data[:, 4]))
#average petal length for each iris species
average0 = sum(iris_data[np.where(iris_data[:,4] == 0)][:,2])
average1 = sum(iris_data[np.where(iris_data[:,4] == 1)][:,2])
average2 = sum(iris_data[np.where(iris_data[:,4] == 2)][:,2])
print ("average petal length for each iris species: ", average0, average1, average2)


