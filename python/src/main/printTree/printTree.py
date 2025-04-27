import json

def print_json_tree(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print("  " * indent + f"├── {key}:")
            print_json_tree(value, indent + 1)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print("  " * indent + f"├── [{i}]:")
            print_json_tree(item, indent + 1)
    else:
        print("  " * indent + f"└── {data}")

# Example usage:
json_data = """
[
    {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling"],
    "address": {
        "street": "123 Main St",
        "zipcode": "10001"
        }
    },
    {
    "name": "Jane Doe",
    "age": 33,
    "city": "New York",
    "hobbies": ["reading", "traveling"],
    "address": {
        "street": "123 Main St",
        "zipcode": "10001"
        }
    },
]
"""

data = json.loads(json_data)
print_json_tree(data)