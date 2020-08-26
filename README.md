# Solidity-Metric-Parser

This Solidity metric parser, parses Solidity files and generates a .csv file containing 3 metrics for each Solidity file that is parsed.

## Installation

Use python version 3 to run the python scripts.

Install Slither from [Here.](https://github.com/crytic/slither)

Install solc select from [Here.](https://github.com/crytic/solc-select)




## Usage

### Metrics Calculation

Make sure smart contracts are in a folder called contracts\

```bash
Python3 parserTest.py
```

### Security Analysis
Change Solidity version corresponding to the Solidity file.
```bash
solc use 0.x.x
```

```bash
slither solidityfile.sol
```

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
