# Consumer-Driven Contract Testing with Pact and Python

This repo is part of a Medium post where I discuss how to use Pact as platform to add CDC testing to your projects.


## Instructions

1. Create venv and install requirements

```bash
python3 -m venv venv
pip install -r requirements.txt
```

2. Ensure the Pact broker is running and up

### Consumer

```bash
cd consumer
./run_pytest.sh

```

### Provider

```bash
cd provider
./run_pytest.sh

```
