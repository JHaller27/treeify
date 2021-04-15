from tree import *


EMPTY_INDENT = '  '
PIPED_INDENT = '│ '
SPLIT_INDENT = '├ '
ELBOW_INDENT = '└ '


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

    def _write_kv_pairs(self, pairs: list[(str, INode)]):
        def _write(key: str, val: INode, split: str, indent: str):
            if len(self._prefixes) == 0:
                split = ""
                indent = ""
            print(self._prefix, split, key, sep="")
            self._push_prefix(indent)
            val.write_to(self)
            self._pop_prefix()

        for k, v in pairs[:-1]:
            _write(k, v, SPLIT_INDENT, PIPED_INDENT)

        k, v = pairs[-1]
        _write(k, v, ELBOW_INDENT, EMPTY_INDENT)

    def write_primitive(self, node: PrimitiveNode):
        indent = "" if len(self._prefixes) == 0 else ELBOW_INDENT
        print(self._prefix, indent, node.value, sep="")

    def write_list(self, node: ListNode):
        children = list(enumerate(node.values()))
        self._write_kv_pairs(children)

    def write_dict(self, node: DictNode):
        children = node.values()
        self._write_kv_pairs(children)

    def flush(self):
        pass
