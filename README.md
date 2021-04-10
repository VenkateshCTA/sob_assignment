# sob_assignment
A simple Python code which parses multiple CSVs, transforms the different CSVs columns &amp; load it into single CSV

## Things which I have considered for the problem statement

1. All the files under the /dir are .csv files
2. Euros & Cents are merged into single column called "amount" in the final merged CSV
3. All the collected input csv files should be inside ./data/ folder

## How to Run

User's python interpreter should be in Python 3

Below is command to run the script

```python process_bank_data.py```

## Output:
1. Displays what all CSV files are processing.
2. Shows before & after processing of the files
3. Finally it displays the collective output in the JSON format
```
All files in data/ folders are ['bank1.csv', 'bank2.csv', 'bank3.csv']
##################################################
                  data/bank1.csv
##################################################
------Before Processing-------
OrderedDict([('timestamp', 'Oct 1 2019'), ('type', 'remove'), ('amount', '99.20'), ('from', '198'), ('to', '182')])
OrderedDict([('timestamp', 'Oct 2 2019'), ('type', 'add'), ('amount', '2000.10'), ('from', '188'), ('to', '198')])
-------After Processing-------
{"date": "2019-Oct-01", "transaction": "remove", "amount": "99.20", "from": "198", "to": "182"}
{"date": "2019-Oct-02", "transaction": "add", "amount": "2000.10", "from": "188", "to": "198"}

##################################################
                  data/bank2.csv
##################################################
------Before Processing-------
OrderedDict([('date', '03-10-2019'), ('transaction', 'remove'), ('amounts', '99.40'), ('to', '182'), ('from', '198')])
OrderedDict([('date', '04-10-2019'), ('transaction', 'add'), ('amounts', '2123.50'), ('to', '198'), ('from', '188')])
-------After Processing-------
{"date": "2019-Oct-03", "transaction": "remove", "amount": "99.40", "from": "198", "to": "182"}
{"date": "2019-Oct-04", "transaction": "add", "amount": "2123.50", "from": "188", "to": "198"}

##################################################
                  data/bank3.csv
##################################################
------Before Processing-------
OrderedDict([('date_readable', '5 Oct 2019'), ('type', 'remove'), ('euro', '5'), ('cents', '7'), ('to', '182'), ('from', '198')])
OrderedDict([('date_readable', '6 Oct 2019'), ('type', 'add'), ('euro', '1060'), ('cents', '8'), ('to', '198'), ('from', '188')])
-------After Processing-------
{"date": "2019-Oct-05", "transaction": "remove", "amount": "5.7", "from": "198", "to": "182"}
{"date": "2019-Oct-06", "transaction": "add", "amount": "1060.8", "from": "188", "to": "198"}

The formatted collective data as below
{"date": "2019-Oct-01", "transaction": "remove", "amount": "99.20", "from": "198", "to": "182"}
{"date": "2019-Oct-02", "transaction": "add", "amount": "2000.10", "from": "188", "to": "198"}
{"date": "2019-Oct-03", "transaction": "remove", "amount": "99.40", "from": "198", "to": "182"}
{"date": "2019-Oct-04", "transaction": "add", "amount": "2123.50", "from": "188", "to": "198"}
{"date": "2019-Oct-05", "transaction": "remove", "amount": "5.7", "from": "198", "to": "182"}
{"date": "2019-Oct-06", "transaction": "add", "amount": "1060.8", "from": "188", "to": "198"}
```
## Maintainability
For integrating new Bank's data one must analyse the data and must extend the configuration
