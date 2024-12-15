def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some operations with the file ...
    # missing f.close()