class Sample:
    a = "Ahad"      # Class attribute

obj = Sample()
obj.a = "Saad"        # Instance attribute just for obj. ''' it dose'nt change the class attribute
# Sample.a = "Saad"     # It will chnage the class attribute

print(Sample.a)
print(obj.a)
