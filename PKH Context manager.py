# Write your own Context manager for opening a file.
# Special thing is to always print when opening/closing.

class ContextManager:
    def __init__(self, file, functionality):
        self.file = open(file, functionality)

    def __enter__(self):
        print('Opening file...')
        return self.file

    def __exit__(self, type, value, traceback):
        print('Closing file...')
        self.file.close()
        return True


with ContextManager('My_file.txt', 'w') as f:
    f.write("First sentence")

