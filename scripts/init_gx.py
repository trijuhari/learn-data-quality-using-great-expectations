import great_expectations as gx
import os

print(f"Great Expectations Version: {gx.__version__}")

# Try to initialize file-based context
context = gx.get_context(mode="file")

print("Context initialized.")
print(f"Context root: {context.root_directory}")

# In GX 1.0+, the structure might be different, but let's see what happens.
