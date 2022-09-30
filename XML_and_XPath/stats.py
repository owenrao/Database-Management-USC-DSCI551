from lxml import objectify
import json

def gen_IND(root):
    INodeDirectory = {"directory":[]}
    for directory in root["INodeDirectorySection"].getchildren():
        directory_node = {}
        directory_node["parent"] = directory["parent"].text
        directory_node["child"] = []
        for child in directory.getchildren()[1:]:
            directory_node["child"].append(child.text)
        INodeDirectory["directory"].append(directory_node)
    return INodeDirectory

def gen_IN(root):
    INode = {"lastInodeId":root["INodeSection"]["lastInodeId"].text,
            "numInodes":root["INodeSection"]["numInodes"].text,
            "inode":[]}
    for inode in root["INodeSection"].getchildren()[2:]:
        inode_dict = {child.tag:child.text for child in inode.getchildren() if child.tag != "blocks"}
        try:
            inode_dict["blocks"] = [{child.tag:child.text for child in block.getchildren()} for block in inode["blocks"].getchildren()]
        except:
            pass
        INode["inode"].append(inode_dict)
    return INode

def file_list(INode):
    return [file_dict for file_dict in INode["inode"] if file_dict["type"]=="FILE"]
def dir_list(INode):
    return [dir_dict for dir_dict in INode["inode"] if dir_dict["type"]=="DIRECTORY"]

def find_directory_depth(INodeDirectory):
    def recursion(parent_id):
        max_depth = 0
        try:
            child_list = [dic for dic in INodeDirectory["directory"] if dic["parent"]==parent_id][0]["child"]
            for child_id in child_list:
                depth = recursion(child_id)
                if depth > max_depth: max_depth = depth
            return max_depth+1
        except IndexError:
            return 1
    root_inumber = INodeDirectory["directory"][0]["parent"]
    return recursion(root_inumber)

def file_size(file_list):
    size_list = [sum([int(block["numBytes"]) for block in file["blocks"]]) for file in file_list]
    return {"max":max(size_list),"min":min(size_list)}

def main(input_path,output_path):
    xml = objectify.parse(open(input_path))
    root = xml.getroot()
    INodeDirectory = gen_IND(root)
    INode = gen_IN(root)
    fl = file_list(INode)
    dl = dir_list(INode)
    result = {"number of files": len(fl), "number of directories": len(dl),
              "maximum depth of directory tree": find_directory_depth(INodeDirectory),
              }

    if fl == []:
        return result
    else:
        result["file size"] = file_size(fl)
        with open(output_path,"w") as handle:
            handle.write(json.dumps(result))
        print("Finished")

if __name__ == "__main__":
    import sys
    main(sys.argv[1],sys.argv[2])