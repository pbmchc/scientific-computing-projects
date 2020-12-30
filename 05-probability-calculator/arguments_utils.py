def convert_to_arguments_list(arguments):
    arguments_list = []

    for name, occurrences in arguments.items():
        arguments_list.extend([name] * occurrences)

    return arguments_list
