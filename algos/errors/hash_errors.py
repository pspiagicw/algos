class KeyNotFoundException(Exception):
    """Exception raised when the key in a hashtable is not present"""
    def __init__(self,key):
        self.message = 'Key {key} is not present'.format(key=key)
        super().__init__(self.message)
