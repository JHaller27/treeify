from tree import *


EMPTY_INDENT = '   '
PIPED_INDENT = '│  '
SPLIT_INDENT = '├─'
ELBOW_INDENT = '└─'
ARRAY_INDEX =  '─┐'


class UnicodeWriter(IWriter):
    def write_primitive(self, node: PrimitiveNode):
        pass

    def write_list(self, node: ListNode):
        pass

    def write_dict(self, node: DictNode):
        pass

    def flush(self):
        pass
