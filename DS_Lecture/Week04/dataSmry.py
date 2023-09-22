import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def adjust_data_frame(df):
  df['Males'] = df['Males'].str.replace('years','').astype('float')
  df['Females'] = df['Females'].str.replace('years','').astype('float')

def mean_median_mode(df):
  mean = {}
  median = {}
  mode = {}
  
  std = {}
  var = {}

  for c in ['Males','Females','Birth rate','Death rate']:
    mean[c] = df[c].mean()
    median[c] = df[c].median()
    mode[c]=dict(df[c].mode()) #frequency가 가장 높은 값

    std[c] = df[c].std()
    var[c] = df[c].var()

    print(f"mean = {mean}")
    print(f"median = {median}")
    print(f"mode = {mode}")

def percentile(df):

  p = [x for x in range(0,101,10)]

  for c in ['Males','Females','Birth rate','Death rate']:
    percentile = np.percentile(df[c],p)
    plt.plot(p, percentile, 'o-')
    plt.xlabel('percentile')
    plt.ylabel(c)
    plt.xticks(p)
    plt.yticks(np.arange(0, max(percentile)+1 , max(percentile)/10.0 ))
    plt.show()

def boxplot(df):
  boxplot = df[['Males','Females','Birth rate','Death rate']].boxplot()
  plt.show()

def histogram(df):
  # for c in ['Males','Females','Birth rate','Death rate']:
  #   plt.hist(df[c] , facecolor='blue',bins=20)
  #   plt.xlabel(c)
  #   plt.show()

  for c in ['Score','Social support']:
    plt.hist(df[c] , facecolor='blue',bins=20)
    plt.xlabel(c)
    plt.show()

def scatter_plot(df):
  for c1 in ['Males','Females','Birth rate','Death rate']:
    for c2 in ['Males','Females','Birth rate','Death rate']:
      if c1==c2 :
        continue
      plt.scatter(df[c1],df[c2])
      plt.xlabel(c1)
      plt.ylabel(c2)
      plt.show()
def df_merge(df1,df2):
  df = pd.merge(df1,df2 , on='Country',how='inner')

  return df


if __name__ == '__main__' :
  # './DS_Lecture/Week04/Life_expectancy.scv'
  csv_file = './DS_Lecture/Week04/Life_expectancy.csv'
  csv_file2 = './DS_Lecture/Week04/2019_happiness_index.csv'

  df = pd.read_csv(csv_file2)
  histogram(df)
  # adjust_data_frame(df)