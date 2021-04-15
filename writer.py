from tree import *


EMPTY_INDENT = '   '
PIPED_INDENT = '│  '
SPLIT_INDENT = '├─'
ELBOW_INDENT = '└─'
ARRAY_INDEX =  '─┬'


class UnicodeWriter(IWriter):
    def __init__(self):
        self._prefixes = []

    def _push_prefix(self, addition: str):
        prefix = self._prefix + addition
        self._prefixes.append(prefix)

    def _pop_prefix(self) -> str:
        return self._prefixes.pop()

    @property
    def _prefix(self) -> str:
        if len(self._prefixes) == 0:
            return ""

        return self._prefixes[-1]

    def write_primitive(self, node: PrimitiveNode):
        print(self._prefix, node.value, sep="")

    def write_list(self, node: ListNode):
        def _write(key: int, val: INode, split: str, indent: str):
            print(self._prefix, split, key, sep="")
            self._push_prefix(indent)
            val.write_to(self)
            self._pop_prefix()

        children = list(enumerate(node.values()))
        for k, v in children[:-1]:
            _write(k, v, SPLIT_INDENT, PIPED_INDENT)

        k, v = children[-1]
        _write(k, v, ELBOW_INDENT, EMPTY_INDENT)

    def write_dict(self, node: DictNode):
        def _write(key: str, val: INode, split: str, indent: str):
            print(self._prefix, split, key, sep="")
            self._push_prefix(indent)
            val.write_to(self)
            self._pop_prefix()

        children = node.values()
        for k, v in children[:-1]:
            _write(k, v, SPLIT_INDENT, PIPED_INDENT)

        k, v = children[-1]
        _write(k, v, ELBOW_INDENT, EMPTY_INDENT)

    def flush(self):
        pass
