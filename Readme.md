# Missing Data Generator

This script will generate a data set from the base data set for a certain percentage

## Requirements

1. pandas
2. argparse
3. numpy

## How to use

```
 python imputation.py 
    -if <input csv file> 
    -of <output csv file> 
    -p <percentage>
    -sc <Skip columns>
```

example 
`python imputation.py -if input.csv -of out.csv -p 20`

### list missing value result of a file

```
 python imputation.py 
    -if <input csv file> 
    -l
```

example 
`python imputation.py -if input.csv -l`