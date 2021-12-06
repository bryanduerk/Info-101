import pandas as pd
import numpy as np
class PowerLiftData:
        
    def ___init___(self):
        self.data = []

    def load(self):
        # Read in the data file from Kaggle for USA powerlifting
        self.data = pd.read_csv(r'data/usa_sbd_data_2020-10-16.csv')
        #Creates an array of the data for use in loops 
        self.npDataArray = self.data.to_numpy()


    # This section uses Pandas, which simplifies statistics on tabular data
    def ages(self):
        #Splits data into 5 quintiles based on age
        # self.data['AgeRank'] = pd.qcut(self.data['Age'], q = 5, labels = False)
        groupedByAge = self.data.groupby(['AgeClass'])
        ageStats  = groupedByAge['Age'].agg(['min', 'median', 'mean', 'max'])
        
        print('\n\nAge Groupings by sorting the data and dividing into groups')
        print(ageStats)
        
    def SBDAverage(self):
        print("\n\nMean Squat for Each Attempt")
        # get the location of the 1st attempt, next 2 attempts are the next 2 columns
        self.average(self.data.to_numpy(), self.data.columns.get_loc('Squat1Kg'))
        print("\n\nMean Bench for Each Attempt")
        self.average(self.data.to_numpy(), self.data.columns.get_loc('Bench1Kg'))
        print("\n\nMean Deadlift for Each Attempt")
        self.average(self.data.to_numpy(), self.data.columns.get_loc('Deadlift1Kg'))
    
    def attemptAveragesByAgeClass(self):
        ageClasses = self.data.groupby(['AgeClass'])
        for ageClassName in ageClasses.groups.keys():
            print('\nAge Class:' + ageClassName + '\n')
            group = ageClasses.get_group(ageClassName)
            print("Mean Squat for Each Attempt")
            self.average(group.to_numpy(), group.columns.get_loc('Squat1Kg'))
            print("\nMean Bench for Each Attempt")
            self.average(group.to_numpy(), group.columns.get_loc('Bench1Kg'))
            print("\nMean Deadlift for Each Attempt")
            self.average(group.to_numpy(), group.columns.get_loc('Deadlift1Kg'))
    
    def print(self):
        print(self.data.head())
        
    # This section uses a standard numerical python array and iterates
    def printNames(self, firstName):
        for row in self.npDataArray:
            if (row[1].startswith(firstName)):
                print(row)
    
    # Know that there are 3 attempts, but a simple average is wrong because failed attempts
    # are added as negative. This gets the average of the three
    def average(self, dataArray, columnNum):
        count = [0,0,0]
        sum = [0,0,0]
        mean = [0,0,0]
        for row in dataArray:
            for i in range(3):
                # Need to make sure the value isn't blank and greater than 0
                if (np.isnan(row[columnNum + i]) == False and row[columnNum + i] > 0): 
                    count[i] += 1
                    sum[i] += row[columnNum + i]
        
        for i in range(3):
            mean[i] = sum[i] / count[i]
            print('{:.2f}'.format(mean[i]))
    
# Main part of the program
runner = PowerLiftData()
runner.load()
# runner.SBDAverage()
# runner.printNames('Bryan')
# runner.print()
# runner.ages()
runner.attemptAveragesByAgeClass()
