class DataStream:

    def __init__(self):
        print("DataStream Initialization")
        self.data = []

    def get_owner(self):
        pass

    def get_metadata(self):
        pass

    def get_annotations(self):
        pass

    def as_nparray(self):
        """Return the numpy array version of the data object"""
        pass

    def as_pandas_dataframe(self):
        """Return the pandas dataframe version of the data object"""
        pass

    def __iter__(self):
        return _DataIter(self.data)


class _DataIter:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()