#this is to get the problem in block
def split_blocks(file_path, separator="--- Problem"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()


    block= content.split(separator)

    #remove any empty or whitespace only blocks
    new_blocks = []
    for item in block:
        if item.strip():
            new_blocks.append(item.strip())

    return new_blocks


def get_problem_block(file_path, index, separator="--- Problem"):
    blokc = split_blocks(file_path, separator)

    if index >= len(blokc):
        return None
    
    return blokc[index]