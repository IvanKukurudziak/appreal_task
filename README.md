# Python developer
Home assignment (Python Task)

### General
Used Python 3.9 

Used CSV library

### Tasks
`csv-task` - convert “TSV” (tab-separated values) to “CSV” (comma-separated values
 - convert it to a valid CSV format into the file named python_home_task_file.csv and attach the file
 - add a column to the CSV file, column named `price_edited`. Fill the column with the float value from the `search_price` column

Run the task:
```
$ python csv-task.py --infile python_home_task_file.csv 
--out python_home_task_file_with_price.csv
```
<br />
  
`regex-tasks` - remove all the knit products without jumpers from the input csv file. To
perform the selection task, used regex rather than code.

Run the task:
```
$ python regex-task.py --infile python_home_task_file.csv --out
python_home_task_file_regex.csv
```