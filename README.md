# Coding Assignment: API

## Task
Given external services:

Service A: https://run.mocky.io/v3/9a01a1b9-26e1-4c8a-84db-d534352e1461

Service B: https://run.mocky.io/v3/ba026992-281a-42a6-8447-ae1c8a04106e

> Create a HTTP service that reads the data from the external services and exposes an endpoint from which one would be able to get the combined mean and sum of the data.

Expected result:

```bash
    curl http://localhost:8000/

    # returns format
    >>> {
    >>>     "mean": 1781.85,
    >>>     "sum": 220950
    >>> }
```

## Setup & Run API

```bash
cd ./coding_assignment_api

# setup environment
# conda
conda create -n apienv python=3.8
conda activate apienv
conda install --file requirements.txt -y
# or with pip
# python -m pip install -r requirements.txt

# run tests
pytest tests.py

# run app
python -m app

# in a second terminal window run
curl http://localhost:8000
```
