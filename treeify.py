import yaml
import argparse
from tree import *
from writer import UnicodeWriter


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="Path to YAML input file")
args = parser.parse_args()

if args.path is None:
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


def to_node(struct) -> INode:
    if isinstance(struct, dict):
        node = DictNode()
        for k, v in struct.items():
            node.add_node(k, to_node(v))

        return node

    if isinstance(struct, list):
        node = ListNode()
        for v in struct:
            node.add_node(to_node(v))

        return node

    return PrimitiveNode(struct)


data = "\n".join(lines)
data_struct = yaml.safe_load(data)

root = to_node(data_struct)

writer = UnicodeWriter()
root.write_to(writer)
