
def format_schema_errors(errs):
    """
    format the errors dictionary to list, select the first error in value list
    :param errs:
    :return: list of errors ["INVALID_STH"]
    """
    for e in errs.values():
        return e[0]
