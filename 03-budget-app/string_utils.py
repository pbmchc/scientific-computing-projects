def limit_string_length(value, max_length):
    return value[:max_length] if len(value) > max_length else value
