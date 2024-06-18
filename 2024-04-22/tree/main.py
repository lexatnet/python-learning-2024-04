import random
import pprint


def genarate_node_name():
    names = [
        "vasya",
        "petya",
        "inna",
    ]
    return random.choice(names)


def generate_node(childs):
    return {
        "name": genarate_node_name(),
        "childs": childs,
    }


def generate_tree(childs_limit=3, deep_limit=3):
    childs = []

    if deep_limit > 0:
        for i in range(random.randint(1, childs_limit)):
            node = generate_tree(childs_limit=childs_limit, deep_limit=deep_limit - 1)
            childs.append(node)

    return generate_node(childs=childs)


def get_node_name(node):
    return node["name"]


def get_node_childs(node):
    return node["childs"]


def print_tree(tree, node_mark="-", level="", level_step="  ", connector="|"):
    name = get_node_name(tree)
    print(f"{level}{node_mark}{name}")
    childs = get_node_childs(tree)
    if len(childs) > 0:
        template = f"{level}{level_step}{connector}"
        print(template)
        for child in childs:
            print_tree(child, level=template)
        print(f"{level}{level_step}")


tree = generate_tree()
print_tree(tree)
