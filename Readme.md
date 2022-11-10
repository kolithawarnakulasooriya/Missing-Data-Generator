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
```

example 
`python imputation.py -if input.csv -of out.csv -p 20`
