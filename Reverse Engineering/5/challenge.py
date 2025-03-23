import marshal

# Load the serialized code object
with open("challenge.dat", "rb") as f:
    serialized_data = f.read()

# Deserialize and execute
code_obj = marshal.loads(serialized_data)
exec(code_obj)
