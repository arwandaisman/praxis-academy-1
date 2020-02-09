import pickle

my_custom_pickle = bytes("this is unpicklable", encoding="UTF-8")

# this next statement will raise a _pickle.UnpicklingError
my_new_object = pickle.loads(my_custom_pickle)