def block_jump(blocks_height, jump_height):
    for i in blocks_height:
        if i > jump_height:
            return False
    return True