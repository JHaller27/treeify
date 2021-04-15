class INode:
    def write_to(self, writer: "IWriter") -> None:
        raise NotImplementedError


class PrimitiveNode(INode):
    def __init__(self, value):
        self._value = str(value)

    @property
    def value(self) -> str:
        return self._value

    def write_to(self, writer: "IWriter") -> None:
        writer.write_primitive(self)


class ListNode(INode):
    _children: list[INode]

    def __init__(self):
        self._children = list()

    def values(self) -> list[INode]:
        return list(self._children)

    def add_node(self, node: INode):
        self._children.append(node)

    def write_to(self, writer: "IWriter") -> None:
        writer.write_list(self)


class DictNode(INode):
    _children: dict[str, INode]

    def __init__(self):
        self._children = dict()

    def values(self) -> list[tuple[str, INode]]:
        return [(k, v) for k, v in self._children.items()]

    def add_node(self, key: str, node: INode):
        self._children[key] = node

    def write_to(self, writer: "IWriter") -> None:
        writer.write_dict(self)


class IWriter:
    def write_primitive(self, node: PrimitiveNode):
        raise NotImplementedError

    def write_list(self, node: ListNode):
        raise NotImplementedError

    def write_dict(self, node: DictNode):
        raise NotImplementedError

    def flush(self):
        raise NotImplementedError
