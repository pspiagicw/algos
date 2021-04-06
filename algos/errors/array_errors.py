class IndexOutOfBoundsException(Exception):
    """Exception raised when index is not accessible in array """
    def __init__(self,index):
        self.message = 'Index {index} is out of bounds'.format(index=index)
        super().__init__(self.message)
class TypeException(Exception):
    """Exception raised when type existing and given type don't match"""
    def __init__(self,existing,given):
        self.message = 'Type {existing} does not match for incoming type {given}'.format(existing=existing,given=given)
        super().__init__(self.message)
