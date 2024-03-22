# import pandas as pd

# pd.DataFrame()

class RailwayForm:

    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(f"Time is {self.time}")

myApplication = RailwayForm()
myApplication.name = "jibran"
myApplication.train = "ABC"
myApplication.time = "12:00"
myApplication.printData()