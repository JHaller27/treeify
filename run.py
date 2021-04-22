import yaml
import argparse
from writer import UnicodeWriter
from treeify import treeify


def width_arg(rval: str) -> int:
    ival = int(rval)
    if ival < 2:
        raise argparse.ArgumentTypeError(f"value may not be smaller than 2. Found '{ival}'.")
    return ival


parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, nargs="?",
                    help="Path to YAML input file (use '-' for stdin). Default: -")
parser.add_argument("-w", "--width", type=width_arg, default=4,
                    help="Indent size (must be no smaller than 2)")
args = parser.parse_args()

if args.path is None or args.path == "-":
    lines = []
    line = input()
    while line != "":
        lines.append(line)
        try:
            line = input()
        except EOFError:
            line = ""
else:
    with open(args.path, "r") as fp:
        lines = fp.readlines()


data = "\n".join(lines)
data_struct = yaml.safe_load(data)

root = treeify(data_struct)

writer = UnicodeWriter(args.width)
root.write_to(writer)
