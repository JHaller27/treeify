from tree import *
from writer import UnicodeWriter


root = DictNode()

dict_node = DictNode()
root.add_node("dict", dict_node)

sub_dict = DictNode()
dict_node.add_node("subdict", sub_dict)

list_node = ListNode()
dict_node.add_node("list", list_node)

for i in [1, 2]:
    sub_dict.add_node(f"key{i}", PrimitiveNode(f"val{i}"))
    list_node.add_node(PrimitiveNode(f"val{i}"))

dict_node.add_node("primitive", PrimitiveNode("string"))

list_node = ListNode()
root.add_node("list", list_node)

sub_list = ListNode()
list_node.add_node(sub_list)

sub_dict = DictNode()
list_node.add_node(sub_dict)

for i in [1, 2]:
    sub_list.add_node(PrimitiveNode(f"val{i}"))
    sub_dict.add_node(f"key{i}", PrimitiveNode(f"val{i}"))

list_node.add_node(PrimitiveNode("primitive"))

writer = UnicodeWriter()
root.write_to(writer)
