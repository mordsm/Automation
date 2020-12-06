import json

try:
    with open("nodes.json", "r") as read_file:
        data = json.load(read_file)
        print(type(data))
        print(1)
        inp = ""
        while inp != "x":
            for key in data["nodes"][0]:
                node = {}
                node[key] = input("Enter " + key + " :")
                if node[key] == "x":
                    inp = "x"
                    break
                data["nodes"].append(node)

        new = input("enter new key (y)? :")
        print(4)
        if new == "y":
            print(5)
            key = input("enter new key : ")
            for node in data["nodes"]:
                node[key] = input("for[" + str(node) + "]Enter " + key + " :")
        read_file.close()
        with open("nodes.json", "w") as write_file:
            json.dump(data, write_file)

except Exception  as e:
    print(e)


