# pqcvt - parquet converter

A simple CLI to covert parquet, csv and excel files.

# Installation

To install the cli run:

```bash
pip install git+https://git@github.com/fergarciadlc/pqcvt.git
```

# Usage
```
>> pqcvt --help
Usage: pqcvt [OPTIONS] INPUTFILE

Options:
  -f, --format [csv|excel|parquet]
                                  Format to convert the file.  [required]
  -o, --output TEXT               Output filename.
  --force-str                     Force string type in table.
  --help                          Show this message and exit.
```

##  Example:
To convert `test.csv` file to a compressed parquet file run the following:
```bash
pqcvt test.csv -f parquet
```
And a `test.parquet` will be generated on the same path.

Notice that the input filename remains in the output file but with a different format, if you want to specify the name of tha output file run the following:
```bash
pqcvt test.csv -f parquet -o new_file.parquet
```
