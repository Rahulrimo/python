
# class ABC:
#     def __init__(self):
#       self.public_attribute = NONE
  
#     def public_function():
#       pass


class ABC:
    def __init__(self):
      self.__protected_attribute = NONE
  
    def _protected_function():
      pass
  
obj1 = ABC()
print(obj1.__private_function)  # This will raise an AttributeError