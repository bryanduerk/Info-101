from os import X_OK
import pandas as pd

class PowerLiftData:
        
    def ___init___(self):
        self.data = []

    def load(self):
        self.data = pd.read_csv(r'data/usa_sbd_data_2020-10-16.csv')
        self.npDataArray = self.data.to_numpy()


    # This section uses Pandas, which simplifies statistics on tabular data
    def ages(self):
        print(self.data['Age'].mean())
        self.data['AgeRank'] = pd.qcut(self.data['Age'], q = 5, labels = False)
        groupedByAge = self.data.groupby(['AgeRank'])
        ageStats  = groupedByAge['Age'].agg(['min', 'median', 'mean', 'max'])
        print(ageStats)
        print(groupedByAge['Squat1Kg'].mean())

    def print(self):
        print(self.data.head())
        # print(list(self.data.columns))
        
    # This section uses a standard numerical python array and iterates
    def printNames(self, firstName):
        for row in self.npDataArray:
            if (row[1].startswith(firstName)):
                print(row)
        

runner = PowerLiftData()
runner.load()
runner.printNames('Bryan')
#runner.ages()
#runner.print()
