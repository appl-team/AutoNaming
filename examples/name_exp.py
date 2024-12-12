from argparse import ArgumentParser

from autonaming import name_this_exp

parser = ArgumentParser()
parser.add_argument(
    "--learning_rate", type=float, default=0.001, help="Learning rate for training"
)
parser.add_argument(
    "--batch_size", type=int, default=32, help="Batch size for training"
)
parser.add_argument("--model", type=str, default="resnet18", help="Model architecture")
parser.add_argument("--timestamp", action="store_true", help="Add timestamp or not")
args = parser.parse_args()

# python examples/name_exp.py --learning_rate 0.01 --model vit
# Might output something like: "vit_lr0.01_bs32"

if __name__ == "__main__":
    name = name_this_exp(parser, args, add_timestamp=args.timestamp)
    print(name)
