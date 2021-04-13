EMPTY_INDENT = '    '
PIPED_INDENT = '|   '
SPLIT_INDENT = '├─'
ELBOW_INDENT = '└─'
ARRAY_INDEX =  '──┐'


class INode:
    def to_str(self, prefix: str = "") -> str:
        raise NotImplementedError


class PrimitiveNode(INode):
    def __init__(self, value):
        self._value = str(value)

    def to_str(self, prefix: str = "") -> str:
        return self._value


class ListNode(INode):
    _children: list[INode]

    def __init__(self):
        self._children = list()

    def add_node(self, node: INode):
        self._children.append(node)

    def to_str(self, prefix: str = "") -> str:
        out_str = ""

        for idx in range(len(self._children) - 1):
            out_str += f'\n{prefix}{SPLIT_INDENT}{ARRAY_INDEX}'
            out_str += self._children[idx].to_str(prefix + PIPED_INDENT)

        out_str += f'\n{prefix}{ELBOW_INDENT}{ARRAY_INDEX}'
        out_str += self._children[-1].to_str(prefix + PIPED_INDENT)

        return out_str


class DictNode(INode):
    _children: dict[str, INode]

    def __init__(self):
        self._children = dict()

    def add_node(self, key: str, node: INode):
        self._children[key] = node

    def to_str(self, prefix: str = "") -> str:
        out_str = ""

        keys = list(self._children.keys())
        for kidx in range(len(keys) - 1):
            key = keys[kidx]

            out_str += f'\n{prefix}{SPLIT_INDENT} {key}'
            out_str += self._children[key].to_str(prefix + PIPED_INDENT)

        key = keys[-1]
        out_str += f'\n{prefix}{ELBOW_INDENT} {key}'
        out_str += self._children[key].to_str(prefix + EMPTY_INDENT)

        return out_str


root = DictNode()

alpha = ListNode()
root.add_node("alpha", alpha)
for i in range(1, 4):
    alpha.add_node(PrimitiveNode(f"alpha.{i}"))

bravo = DictNode()
root.add_node("bravo", bravo)
for i in range(1, 4):
    bravo.add_node(f"{i}", PrimitiveNode(f"bravo.{i}"))

charlie = PrimitiveNode("charlie")
root.add_node("charlie", charlie)

print(root.to_str())
