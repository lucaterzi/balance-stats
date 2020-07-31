# Balance Stats

## How to install

I suggest you to use a virtual environment to run this code. The instructions below use `virtualenv`.

First, make sure `virtualenv` is installed in your system:

```
python -m pip install virtualenv
```

Create the virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```

Et voilà, now you have a working virtual environment!

This code does not use external packages, so you don't need to install any requirements.

## Example

To run `balance_stats.py` with the provided example, make sure to have the virtual environment activated and then run:

```
python balance_stats.py 2019-01-01 2019-12-31 examples/transactions.csv
```

The output should be

```
{
  "start_date": "2019-01-01",
  "end_date": "2019-12-31",
  "average_balance": "947.95",
  "maximum_balance": "5000.00",
  "minimum_balance": "0.00"
}
```