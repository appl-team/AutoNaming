# AutoNaming

A Python package that provides LLM-powered naming.

Currently supports automatically naming experiments using information from `parser` and `args` (from `argparse`).

Implemented using [APPL](https://github.com/appl-team/appl).

## Installation

```bash
pip install autonaming
```

## Usage

```python
from argparse import ArgumentParser
from autonaming.exps import name_this_exp

# Create your argument parser as usual
parser = ArgumentParser()
parser.add_argument("--learning_rate", type=float, default=0.001, help="Learning rate for training")
parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training")
parser.add_argument("--model", type=str, default="resnet18", help="Model architecture")

# Parse your arguments
args = parser.parse_args(["--learning_rate", "0.01", "--model", "alexnet"])

# Generate an informative name for your experiment
name = name_this_exp(parser, args, add_timestamp=True)
# Example output: alexnet_lr0.01_bs32__2024_12_11__12_34_56
# You can use this name to name your experiment directory
```

### Instructions for naming experiments

1. Generate a descriptive and concise name in snake_case that captures the key parameters
2. Keep names under 100 characters
3. Include the most important parameters that distinguish this experiment
4. Use standard abbreviations where appropriate (e.g. lr for learning_rate)
5. Order parameters from most to least important
