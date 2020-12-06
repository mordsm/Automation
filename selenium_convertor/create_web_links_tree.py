import json

json_data = [{
    "title": "Food",
    "path": "/root",
}, {
    "title": "Cloths",
    "path": "/root",
}, {
    "title": "Veg",
    "path": "/root/Food",
}, {
    "title": "Brinjal",
    "path": "/root/Food/Veg",
}, {
    "title": "T shirt",
    "path": "/root/Cloths",
}, {
    "title": "Shirt",
    "path": "/root/Cloths",
}, {
    "title": "Green brinjal",
    "path": "/root/Food/Veg/Brinjal",
}];


def addToTree(node, treeNodes):
    parentNode = GetTheParentNodeChildArray(node["path"], treeNodes) or treeNodes;

    parentNode.append({
        "title": node["title"],
        "path": node["path"],
        "children": []
    });


def GetTheParentNodeChildArray(path, treeNodes):
    possibleParent = False
    for i in range(len(treeNodes)):
        treeNode = treeNodes[i];
        if (path == (treeNode["path"] + '/' + treeNode["title"])):
            return treeNode["children"];
        elif (len(treeNode["children"]) > 0):
            possibleParent = False;
        for item in treeNode["children"]:
            if path.indexOf(item["path"] + '/' + item["title"]) == 0:
                possibleParent = True;
            return False;

    if (possibleParent):
        return GetTheParentNodeChildArray(path, treeNode["children"])


# Create the item tree starting from menuItems
def createTree(nodes):
    tree = [];

    for i in range(len(nodes)):
        node = nodes[i];
        addToTree(node, tree);

    return tree;


# variable = "json_data" is the set of URLS
menuItemsTree = createTree(json_data)
print(json.dumps(menuItemsTree))