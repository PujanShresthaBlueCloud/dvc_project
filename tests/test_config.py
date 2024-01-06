import pytest # we can use this as well

class NotInRange(Exception):
    """
    Custome error message for input value provided 
    """
    
    def __init__(self, message="Value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
