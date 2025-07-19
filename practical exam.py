import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('welcome to E-Library Data Insights Dashboard')

class LibraryDashboard:
    def __init__(self):
          self.df=None
    def load_data(self):
        try:
            dataset=input('enter the file path in csv form: ') 
            self.data=pd.read_csv(dataset)
            self.df=pd.DataFrame(self.data)
            print(self.df)
            print('dataset loaded successfully!!')
        except FileNotFoundError:
             print('file not found')

    def calculate_statistics(self):
        print('1.most borrowed book\n2.average borrowing duration')
        choice=int(input('enter your choice: '))
        if choice==1:
                print('most borrowed book is:')
                print(self.df['book_title'].value_counts())
        elif ch==2:
             print('average boeeowing duration is:')
             print(self.df['borrowing_duration_days'].mean())
        else:
             print('invalid choice')

    def filter_transaction(self):
         column_name=input('enetr the column name to filter data: ')
         name=input('enter the name: ')
         print(self.df[self.df[column_name]==name])
    
    def visualization(self):
         print('1.Bar chart\n2.line graph\n3.pie chart\n4.heatmap')
         graph_choice=int(input('enter your choice: '))
         if graph_choice==1:
              y=self.df['book_title'].value_counts().head(5)
              print(y)
              y.plot(kind='bar')
              plt.xlabel('name of books')
              plt.ylabel('number of borrowings')
              plt.title('top 5 most borrowed book')
              plt.show()

         elif graph_choice==2:
              x=self.df['date'].value_counts()
              x.plot(kind='line')
              plt.xlabel('date')
              plt.ylabel('number of borrowing')
              plt.title('borrowing trends over days')
              plt.show()

         elif graph_choice==3:
              z=self.df['genre'].value_counts()
              z.plot(kind='pie')
              plt.title('distribution of books borrowed by genre')
              plt.show()

         elif graph_choice==4:
              heatmap=self.df.corr(numeric_only=True)
              sns.heatmap(heatmap,annot=True)
              plt.title('borrowing activity by day and time')
              plt.show()
        
         else:
              print('invalid choice')
              
library=LibraryDashboard()
while True:
      print('1.load dataset\n2.statistics calculations\n3.data filtering\n4.visualizations\n5.EXit')
      ch=int(input('enter your choice: '))
      if ch==1:
           library.load_data()
      elif ch==2:
           library.calculate_statistics()
      elif ch==3:
           library.filter_transaction()
      elif ch==4:
           library.visualization()
      elif ch==5:
           break
      else:
           print('invalid choice')