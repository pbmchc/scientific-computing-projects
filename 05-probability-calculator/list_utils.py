def is_part_of_list(list_to_check, root_list):
    return all(root_list.count(item) >= list_to_check.count(item) for item in list_to_check)
