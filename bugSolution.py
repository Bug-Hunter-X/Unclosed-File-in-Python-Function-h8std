def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some operations with the file ...
            f.write('This is some text.')
    except Exception as e:
        print(f"An error occurred: {e}")