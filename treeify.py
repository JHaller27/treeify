from tree import *
from writer import UnicodeWriter


root = DictNode()

alpha = ListNode()
root.add_node("alpha", alpha)
for i in range(1, 4):
    alpha.add_node(PrimitiveNode(f"alpha.{i}"))

alpha4 = ListNode()
alpha.add_node(alpha4)
for i in range(1, 4):
    alpha4.add_node(PrimitiveNode(f"alpha.4.{i}"))

bravo = DictNode()
root.add_node("bravo", bravo)
for i in range(1, 4):
    bravo.add_node(f"k{i}", PrimitiveNode(f"bravo.{i}"))

charlie = PrimitiveNode("charlie")
root.add_node("charlie", charlie)

writer = UnicodeWriter()
root.write_to(writer)
