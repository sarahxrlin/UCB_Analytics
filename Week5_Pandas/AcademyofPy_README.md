

```python
#import modules
import csv
import pandas as pd
import numpy as np
```


```python
#read in csv

students_file = pd.read_csv('students_complete.csv')
schools_file = pd.read_csv('schools_complete.csv')

students_file.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python

schools_file
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
  </tbody>
</table>
</div>




```python
# District Summary
# Create a high level snapshot (in table form) of the district's key metrics, including:

#Total Schools
num_schools = schools_file["name"].nunique()
num_schools

```




    15




```python
#Total Students
num_students = students_file["name"].nunique()
num_students

```




    32715




```python
#Total Budget
total_budget = schools_file["budget"].sum()
total_budget = "$" + str(total_budget)

```


```python
#Average Math Score
avg_math_score = round(students_file["math_score"].mean(),2)
avg_math_score

```




    78.99




```python
#Average Reading Score
avg_rdg_score = round(students_file["reading_score"].mean(),2)
avg_rdg_score

```




    81.88




```python
#% Passing Math

pass_math = len(students_file[students_file["math_score"] > 70])/num_students*100
pass_math = round(pass_math,2)
pass_math

#pass_math_perc = (pass_math['name'])/num_students * 100, 2)
#pass_math_perc

```




    86.68




```python
#% Passing Reading
pass_read = students_file[students_file["reading_score"] > 70].count()

pass_read_perc = round(pass_read['name']/num_students * 100, 2)
pass_read_perc

```




    99.34




```python
#Overall Passing Rate (Average of the above two)

avg_overall = (pass_math + pass_read_perc)/2
avg_overall
```




    93.01




```python
# District Summary table
district_summary = pd.DataFrame({"Total Schools": [num_schools],
"Total Students": [num_students],
"Total Budget": [total_budget],
"Average Math Score": [avg_math_score],
"Average Reading Score": [avg_rdg_score],
"% Passing Math": [pass_math],
"% Passing Reading": [pass_read_perc],
"Overall Passing Rate (Average of the above two)": [avg_overall]})

district_summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate (Average of the above two)</th>
      <th>Total Budget</th>
      <th>Total Schools</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>86.68</td>
      <td>99.34</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>93.01</td>
      <td>$24649428</td>
      <td>15</td>
      <td>32715</td>
    </tr>
  </tbody>
</table>
</div>




```python
#School Summary

#Create an overview table that summarizes key metrics about each school, including:
#School Name
merged_df = pd.merge(students_file, schools_file, how = 'left', left_on="school", right_on = "name")
merged_df.head(100)

grouped_df = merged_df.groupby('school')
#print(type(grouped_df))

grouped_df.count().head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name_x</th>
      <th>gender</th>
      <th>grade</th>
      <th>reading_score</th>
      <th>math_score</th>
      <th>School ID</th>
      <th>name_y</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
      <td>1468</td>
    </tr>
  </tbody>
</table>
</div>




```python
#School Type

#set index for school_file
new_schools_file = schools_file.set_index('name')
new_schools_file
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>1</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>3</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>5</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>6</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>7</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>8</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>9</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>10</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>11</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>12</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>13</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>14</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
  </tbody>
</table>
</div>




```python
#School Type
#Total Students
num_students = students_file["school"].value_counts()
num_students.head()

```




    Bailey High School       4976
    Johnson High School      4761
    Hernandez High School    4635
    Rodriguez High School    3999
    Figueroa High School     2949
    Name: school, dtype: int64




```python
#Total School Budget
school_budget = new_schools_file["budget"]
school_budget
```




    name
    Huang High School        1910635
    Figueroa High School     1884411
    Shelton High School      1056600
    Hernandez High School    3022020
    Griffin High School       917500
    Wilson High School       1319574
    Cabrera High School      1081356
    Bailey High School       3124928
    Holden High School        248087
    Pena High School          585858
    Wright High School       1049400
    Rodriguez High School    2547363
    Johnson High School      3094650
    Ford High School         1763916
    Thomas High School       1043130
    Name: budget, dtype: int64




```python
#Per Student Budget

new_schools_file["budget per student"] = new_schools_file["budget"]/new_schools_file["size"]
new_schools_file.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget per student</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>1</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>3</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Average Math Score
grouped_df_avg_math = round(grouped_df['math_score'].mean(), 2)
grouped_df_avg_math.head()
```




    school
    Bailey High School      77.05
    Cabrera High School     83.06
    Figueroa High School    76.71
    Ford High School        77.10
    Griffin High School     83.35
    Name: math_score, dtype: float64




```python
#Average Reading Score
grouped_df_avg_read = round(grouped_df['reading_score'].mean(), 2)
grouped_df_avg_read.head()
```




    school
    Bailey High School      81.03
    Cabrera High School     83.98
    Figueroa High School    81.16
    Ford High School        80.75
    Griffin High School     83.82
    Name: reading_score, dtype: float64




```python
#% Passing Math

stu_pass_math = students_file[students_file["math_score"] > 70]
math_groupby_df = stu_pass_math.groupby('school')
math_groupby_df
num_pass_math = math_groupby_df['math_score'].count()
new_schools_file["# pass math"] = num_pass_math
new_schools_file["% pass math"] = round((new_schools_file["# pass math"]/new_schools_file["size"])*100, 2)
new_schools_file.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget per student</th>
      <th># pass math</th>
      <th>% pass math</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>1847</td>
      <td>63.32</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>1</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>1880</td>
      <td>63.75</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>1583</td>
      <td>89.89</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>3</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>3001</td>
      <td>64.75</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>1317</td>
      <td>89.71</td>
    </tr>
  </tbody>
</table>
</div>




```python
#% Passing Reading
stu_pass_read = students_file[students_file["reading_score"] > 70]
read_groupby_df = stu_pass_read.groupby('school')
read_groupby_df
num_pass_read = read_groupby_df['reading_score'].count()
new_schools_file["# pass reading"] = num_pass_read
new_schools_file["% pass reading"] = round((new_schools_file["# pass reading"]/new_schools_file["size"])*100, 2)
new_schools_file.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget per student</th>
      <th># pass math</th>
      <th>% pass math</th>
      <th># pass reading</th>
      <th>% pass reading</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>1847</td>
      <td>63.32</td>
      <td>2299</td>
      <td>78.81</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>1</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>1880</td>
      <td>63.75</td>
      <td>2313</td>
      <td>78.43</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>1583</td>
      <td>89.89</td>
      <td>1631</td>
      <td>92.62</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>3</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>3001</td>
      <td>64.75</td>
      <td>3624</td>
      <td>78.19</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>1317</td>
      <td>89.71</td>
      <td>1371</td>
      <td>93.39</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Overall Passing Rate (Average of the above two)

new_schools_file["overall % passing rate"] = round((new_schools_file["% pass math"] + new_schools_file["% pass reading"])/2, 2)
new_schools_file.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>budget per student</th>
      <th># pass math</th>
      <th>% pass math</th>
      <th># pass reading</th>
      <th>% pass reading</th>
      <th>overall % passing rate</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>0</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>1847</td>
      <td>63.32</td>
      <td>2299</td>
      <td>78.81</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>1</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>1880</td>
      <td>63.75</td>
      <td>2313</td>
      <td>78.43</td>
      <td>71.09</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>2</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>1583</td>
      <td>89.89</td>
      <td>1631</td>
      <td>92.62</td>
      <td>91.26</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>3</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>3001</td>
      <td>64.75</td>
      <td>3624</td>
      <td>78.19</td>
      <td>71.47</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>4</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>1317</td>
      <td>89.71</td>
      <td>1371</td>
      <td>93.39</td>
      <td>91.55</td>
    </tr>
  </tbody>
</table>
</div>




```python
# School Summary Table 

school_summary_df = pd.DataFrame({
    "Type": new_schools_file['type'],
    "Total Students": new_schools_file['size'],
    "Total School Budget": new_schools_file['budget'],
    "Per Student Budget": new_schools_file["budget per student"],
    "Average Math Score": grouped_df_avg_math,
    "Average Reading Score": grouped_df_avg_read,
    "% Passing Math": new_schools_file["% pass math"],
    "% Passing Reading": new_schools_file["% pass reading"],
    "Overall % Passing Rate": new_schools_file["overall % passing rate"]
})

school_summary_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall % Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>64.63</td>
      <td>79.30</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>71.96</td>
      <td>628.0</td>
      <td>3124928</td>
      <td>4976</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.56</td>
      <td>93.86</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>91.71</td>
      <td>582.0</td>
      <td>1081356</td>
      <td>1858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.75</td>
      <td>78.43</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>71.09</td>
      <td>639.0</td>
      <td>1884411</td>
      <td>2949</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>65.75</td>
      <td>77.51</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>71.63</td>
      <td>644.0</td>
      <td>1763916</td>
      <td>2739</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>89.71</td>
      <td>93.39</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>91.55</td>
      <td>625.0</td>
      <td>917500</td>
      <td>1468</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Performing Schools (By Passing Rate)
top_schools = school_summary_df.sort_values(by='Overall % Passing Rate',ascending=False)
top_schools.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall % Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>90.93</td>
      <td>93.25</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>92.09</td>
      <td>578.0</td>
      <td>1319574</td>
      <td>2283</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>91.68</td>
      <td>92.20</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>91.94</td>
      <td>609.0</td>
      <td>585858</td>
      <td>962</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>90.28</td>
      <td>93.44</td>
      <td>83.68</td>
      <td>83.96</td>
      <td>91.86</td>
      <td>583.0</td>
      <td>1049400</td>
      <td>1800</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>89.56</td>
      <td>93.86</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>91.71</td>
      <td>582.0</td>
      <td>1081356</td>
      <td>1858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>90.63</td>
      <td>92.74</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>91.68</td>
      <td>581.0</td>
      <td>248087</td>
      <td>427</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Bottom Performing Schools (By Passing Rate) 
bottom_schools = school_summary_df.sort_values(by='Overall % Passing Rate',ascending=True)
bottom_schools.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall % Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>64.07</td>
      <td>77.74</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>70.90</td>
      <td>637.0</td>
      <td>2547363</td>
      <td>3999</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>63.32</td>
      <td>78.81</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>71.06</td>
      <td>655.0</td>
      <td>1910635</td>
      <td>2917</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>63.85</td>
      <td>78.28</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>71.06</td>
      <td>650.0</td>
      <td>3094650</td>
      <td>4761</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>63.75</td>
      <td>78.43</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>71.09</td>
      <td>639.0</td>
      <td>1884411</td>
      <td>2949</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>64.75</td>
      <td>78.19</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>71.47</td>
      <td>652.0</td>
      <td>3022020</td>
      <td>4635</td>
      <td>District</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Math Scores by Grade

#Create a table that lists the average Math Score for students of 
#each grade level (9th, 10th, 11th, 12th) at each school.

groupedby_grade = students_file.groupby(['school', 'grade'])
math_score_by_grade = round(groupedby_grade['math_score'].mean(),2)
math_score_by_grade.head(10)


```




    school                grade
    Bailey High School    10th     77.00
                          11th     77.52
                          12th     76.49
                          9th      77.08
    Cabrera High School   10th     83.15
                          11th     82.77
                          12th     83.28
                          9th      83.09
    Figueroa High School  10th     76.54
                          11th     76.88
    Name: math_score, dtype: float64




```python
#Reading Scores by Grade

#Create a table that lists the average Reading Score for students of 
# each grade level (9th, 10th, 11th, 12th) at each school.

groupedby_grade = students_file.groupby(['school', 'grade'])
read_score_by_grade = round(groupedby_grade['reading_score'].mean(),2)
read_score_by_grade.head(10)
```




    school                grade
    Bailey High School    10th     80.91
                          11th     80.95
                          12th     80.91
                          9th      81.30
    Cabrera High School   10th     84.25
                          11th     83.79
                          12th     84.29
                          9th      83.68
    Figueroa High School  10th     81.41
                          11th     80.64
    Name: reading_score, dtype: float64




```python
#Scores by School Spending

#Create a table that breaks down school performances based on average Spending Ranges (Per Student). 
#Use 4 reasonable bins to group school spending. Include in the table each of the following:
school_summary_df.describe()

# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
# Overall Passing Rate (Average of the above two)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall % Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.0000</td>
      <td>15.000000</td>
      <td>1.500000e+01</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>78.200667</td>
      <td>86.178000</td>
      <td>80.431333</td>
      <td>82.529333</td>
      <td>82.1880</td>
      <td>620.066667</td>
      <td>1.643295e+06</td>
      <td>2611.333333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>13.476081</td>
      <td>7.625455</td>
      <td>3.374382</td>
      <td>1.520326</td>
      <td>10.5372</td>
      <td>28.544368</td>
      <td>9.347763e+05</td>
      <td>1420.915282</td>
    </tr>
    <tr>
      <th>min</th>
      <td>63.320000</td>
      <td>77.510000</td>
      <td>76.630000</td>
      <td>80.740000</td>
      <td>70.9000</td>
      <td>578.000000</td>
      <td>2.480870e+05</td>
      <td>427.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>64.350000</td>
      <td>78.355000</td>
      <td>77.060000</td>
      <td>81.000000</td>
      <td>71.2800</td>
      <td>591.500000</td>
      <td>1.046265e+06</td>
      <td>1698.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>89.560000</td>
      <td>92.200000</td>
      <td>83.060000</td>
      <td>83.730000</td>
      <td>91.2600</td>
      <td>628.000000</td>
      <td>1.319574e+06</td>
      <td>2283.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>90.245000</td>
      <td>93.080000</td>
      <td>83.390000</td>
      <td>83.905000</td>
      <td>91.6950</td>
      <td>641.500000</td>
      <td>2.228999e+06</td>
      <td>3474.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>91.680000</td>
      <td>93.860000</td>
      <td>83.840000</td>
      <td>84.040000</td>
      <td>92.0900</td>
      <td>655.000000</td>
      <td>3.124928e+06</td>
      <td>4976.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# create 4 bins
bins = [575, 600, 625, 650,675]
bin_names = ['575-600', '600-625', '625-650', '650-675']
```


```python
# place per student budget into bins
pd.cut(school_summary_df["Per Student Budget"], bins, labels=bin_names)
```




    Bailey High School       625-650
    Cabrera High School      575-600
    Figueroa High School     625-650
    Ford High School         625-650
    Griffin High School      600-625
    Hernandez High School    650-675
    Holden High School       575-600
    Huang High School        650-675
    Johnson High School      625-650
    Pena High School         600-625
    Rodriguez High School    625-650
    Shelton High School      575-600
    Thomas High School       625-650
    Wilson High School       575-600
    Wright High School       575-600
    Name: Per Student Budget, dtype: category
    Categories (4, object): [575-600 < 600-625 < 625-650 < 650-675]




```python
# get just the columns we want
school_summary_trim = pd.DataFrame(school_summary_df, columns=['Average Math Score',
                                                                'Average Reading Score',
                                                               '% Passing Math',
                                                               '% Passing Reading',
                                                                'Overall % Passing Rate'])
school_summary_trim
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.05</td>
      <td>81.03</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.06</td>
      <td>83.98</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.71</td>
      <td>81.16</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.10</td>
      <td>80.75</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.35</td>
      <td>83.82</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.29</td>
      <td>80.93</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.80</td>
      <td>83.81</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.63</td>
      <td>81.18</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.07</td>
      <td>80.97</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.84</td>
      <td>84.04</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.84</td>
      <td>80.74</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.36</td>
      <td>83.73</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.42</td>
      <td>83.85</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.68</td>
      <td>83.96</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
# add bins to each school
school_summary_trim["Spending Ranges (per Student)"] = pd.cut(school_summary_df["Per Student Budget"], 
                                                            bins, labels=bin_names)

school_summary_trim
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
      <th>Spending Ranges (per Student)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.05</td>
      <td>81.03</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
      <td>625-650</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.06</td>
      <td>83.98</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
      <td>575-600</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.71</td>
      <td>81.16</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
      <td>625-650</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.10</td>
      <td>80.75</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
      <td>625-650</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.35</td>
      <td>83.82</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
      <td>600-625</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.29</td>
      <td>80.93</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
      <td>650-675</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.80</td>
      <td>83.81</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
      <td>575-600</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.63</td>
      <td>81.18</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
      <td>650-675</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.07</td>
      <td>80.97</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
      <td>625-650</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.84</td>
      <td>84.04</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
      <td>600-625</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.84</td>
      <td>80.74</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
      <td>625-650</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.36</td>
      <td>83.73</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
      <td>575-600</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.42</td>
      <td>83.85</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
      <td>625-650</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
      <td>575-600</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.68</td>
      <td>83.96</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
      <td>575-600</td>
    </tr>
  </tbody>
</table>
</div>




```python
spending_groups_trim = school_summary_trim.groupby('Spending Ranges (per Student)')

round(spending_groups_trim.mean(),2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
    </tr>
    <tr>
      <th>Spending Ranges (per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>575-600</th>
      <td>83.43</td>
      <td>83.89</td>
      <td>90.26</td>
      <td>93.18</td>
      <td>91.72</td>
    </tr>
    <tr>
      <th>600-625</th>
      <td>83.60</td>
      <td>83.93</td>
      <td>90.70</td>
      <td>92.80</td>
      <td>91.74</td>
    </tr>
    <tr>
      <th>625-650</th>
      <td>78.03</td>
      <td>81.42</td>
      <td>68.71</td>
      <td>80.69</td>
      <td>74.70</td>
    </tr>
    <tr>
      <th>650-675</th>
      <td>76.96</td>
      <td>81.06</td>
      <td>64.04</td>
      <td>78.50</td>
      <td>71.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
# look at stats table for a good way to select bings
school_summary_df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall % Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Total School Budget</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.000000</td>
      <td>15.0000</td>
      <td>15.000000</td>
      <td>1.500000e+01</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>78.200667</td>
      <td>86.178000</td>
      <td>80.431333</td>
      <td>82.529333</td>
      <td>82.1880</td>
      <td>620.066667</td>
      <td>1.643295e+06</td>
      <td>2611.333333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>13.476081</td>
      <td>7.625455</td>
      <td>3.374382</td>
      <td>1.520326</td>
      <td>10.5372</td>
      <td>28.544368</td>
      <td>9.347763e+05</td>
      <td>1420.915282</td>
    </tr>
    <tr>
      <th>min</th>
      <td>63.320000</td>
      <td>77.510000</td>
      <td>76.630000</td>
      <td>80.740000</td>
      <td>70.9000</td>
      <td>578.000000</td>
      <td>2.480870e+05</td>
      <td>427.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>64.350000</td>
      <td>78.355000</td>
      <td>77.060000</td>
      <td>81.000000</td>
      <td>71.2800</td>
      <td>591.500000</td>
      <td>1.046265e+06</td>
      <td>1698.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>89.560000</td>
      <td>92.200000</td>
      <td>83.060000</td>
      <td>83.730000</td>
      <td>91.2600</td>
      <td>628.000000</td>
      <td>1.319574e+06</td>
      <td>2283.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>90.245000</td>
      <td>93.080000</td>
      <td>83.390000</td>
      <td>83.905000</td>
      <td>91.6950</td>
      <td>641.500000</td>
      <td>2.228999e+06</td>
      <td>3474.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>91.680000</td>
      <td>93.860000</td>
      <td>83.840000</td>
      <td>84.040000</td>
      <td>92.0900</td>
      <td>655.000000</td>
      <td>3.124928e+06</td>
      <td>4976.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by School Size

# Repeat the above breakdown, but this time group schools based on a 
# reasonable approximation of school size (Small, Medium, Large).

# create 4 bins
school_bins = [0, 1500, 3500, 5000]
school_bin_names = ['Small (<1500)', 'Medium (1500-3500)', 'Large (3500-5000)']
```


```python
# get just the columns we want
school_summary_trim_2 = pd.DataFrame(school_summary_df, columns=['Average Math Score',
                                                                'Average Reading Score',
                                                               '% Passing Math',
                                                               '% Passing Reading',
                                                                'Overall % Passing Rate'])
school_summary_trim_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.05</td>
      <td>81.03</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.06</td>
      <td>83.98</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.71</td>
      <td>81.16</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.10</td>
      <td>80.75</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.35</td>
      <td>83.82</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.29</td>
      <td>80.93</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.80</td>
      <td>83.81</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.63</td>
      <td>81.18</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.07</td>
      <td>80.97</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.84</td>
      <td>84.04</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.84</td>
      <td>80.74</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.36</td>
      <td>83.73</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.42</td>
      <td>83.85</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.68</td>
      <td>83.96</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_summary_trim_2["School Size"] = pd.cut(school_summary_df["Total Students"], school_bins, labels=school_bin_names)
school_summary_trim_2

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
      <th>School Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.05</td>
      <td>81.03</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
      <td>Large (3500-5000)</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.06</td>
      <td>83.98</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.71</td>
      <td>81.16</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.10</td>
      <td>80.75</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.35</td>
      <td>83.82</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
      <td>Small (&lt;1500)</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.29</td>
      <td>80.93</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
      <td>Large (3500-5000)</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.80</td>
      <td>83.81</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
      <td>Small (&lt;1500)</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.63</td>
      <td>81.18</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.07</td>
      <td>80.97</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
      <td>Large (3500-5000)</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.84</td>
      <td>84.04</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
      <td>Small (&lt;1500)</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.84</td>
      <td>80.74</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
      <td>Large (3500-5000)</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.36</td>
      <td>83.73</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.42</td>
      <td>83.85</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
      <td>Medium (1500-3500)</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.68</td>
      <td>83.96</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
      <td>Medium (1500-3500)</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_size_stats = school_summary_trim_2.groupby('School Size')

school_size_stats = round(school_size_stats.mean(),2)
school_size_stats
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1500)</th>
      <td>83.66</td>
      <td>83.89</td>
      <td>90.67</td>
      <td>92.78</td>
      <td>91.72</td>
    </tr>
    <tr>
      <th>Medium (1500-3500)</th>
      <td>80.90</td>
      <td>82.82</td>
      <td>80.46</td>
      <td>87.60</td>
      <td>84.03</td>
    </tr>
    <tr>
      <th>Large (3500-5000)</th>
      <td>77.06</td>
      <td>80.92</td>
      <td>64.32</td>
      <td>78.38</td>
      <td>71.35</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by School Type

#Repeat the above breakdown, but this time group 
#schools based on school type (Charter vs. District).

#get columns we want
school_summary_trim_3 = pd.DataFrame(school_summary_df, columns=['Average Math Score',
                                                                'Average Reading Score',
                                                               '% Passing Math',
                                                               '% Passing Reading',
                                                                'Overall % Passing Rate',
                                                                'Type'])
school_summary_trim_3

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.05</td>
      <td>81.03</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.06</td>
      <td>83.98</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.71</td>
      <td>81.16</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.10</td>
      <td>80.75</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.35</td>
      <td>83.82</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.29</td>
      <td>80.93</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.80</td>
      <td>83.81</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>76.63</td>
      <td>81.18</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.07</td>
      <td>80.97</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.84</td>
      <td>84.04</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.84</td>
      <td>80.74</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
      <td>District</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.36</td>
      <td>83.73</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.42</td>
      <td>83.85</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.27</td>
      <td>83.99</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.68</td>
      <td>83.96</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
school_type_stats = school_summary_trim_3.groupby('Type')

round(school_type_stats.mean(),2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall % Passing Rate</th>
    </tr>
    <tr>
      <th>Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.47</td>
      <td>83.90</td>
      <td>90.36</td>
      <td>93.05</td>
      <td>91.71</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.96</td>
      <td>80.97</td>
      <td>64.30</td>
      <td>78.32</td>
      <td>71.31</td>
    </tr>
  </tbody>
</table>
</div>


