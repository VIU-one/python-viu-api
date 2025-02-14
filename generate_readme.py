import os
import re

# Define the README template
README_TEMPLATE = """# {package_name}

This package provides a gRPC client for {service_name} using BetterProto.

## Installation
pip install {package_name}

## Usage Example
import asyncio
from generated.{service_import} import {service_name}Stub, {request_type}

async def main():
    client = {service_name}Stub("your.api.endpoint:443")
    request = {request_type}(text="Your text here")  # Adjust based on method params
    response = await client.{method_name}(request)
    print(response)

asyncio.run(main())

## Available Methods
{methods_list}

---
Generated automatically from .proto files using GitHub Actions.
"""

def extract_proto_info():
    """Parses the generated BetterProto Python file to extract service, request types, and methods."""
    
    # Ensure the 'generated' directory exists
    if not os.path.exists("generated"):
        print("Error: 'generated/' directory does not exist.")
        return None, None, None, None, None

    proto_files = [f for f in os.listdir("generated") if f.endswith(".py") and not f.startswith("__")]

    # If no Python files are found
    if not proto_files:
        print("Error: No generated BetterProto files found in 'generated/'.")
        return None, None, None, None, None

    # Debug: Print the files found
    print("Found generated files:", proto_files)

    with open(os.path.join("generated", proto_files[0]), "r") as f:
        content = f.read()

    # Debug: Print a portion of the content to verify format
    print("Generated file content preview:\n", content[:500])

    # Updated regex to correctly match BetterProto service classes
    service_match = re.search(r"class (\w+)Stub\(betterproto\.ServiceStub\):", content)
    request_matches = re.findall(r"async def (\w+)\(self, \*.*,? (\w+):.*?\) -> (\w+):", content)

    # Debug: Print matches
    if service_match:
        print("Found gRPC Service Class:", service_match.group(1))
    else:
        print("Error: No gRPC service class found.")

    if request_matches:
        print("Found RPC Methods:", request_matches)
    else:
        print("Error: No gRPC methods found.")

    # If no service class or methods are found
    if not service_match or not request_matches:
        return None, None, None, None, None

    service_name = service_match.group(1)
    first_method, first_request, first_response = request_matches[0]  # Take the first method for example usage
    methods_list = "\n".join([f"- {method}({req}) -> {resp}" for method, req, resp in request_matches])
    
    return service_name, proto_files[0].replace(".py", ""), first_method, first_request, methods_list


def main():
    service_name, service_import, method_name, request_type, methods_list = extract_proto_info()
    if not service_name:
        print("No gRPC service found!")
        return

    readme_content = README_TEMPLATE.format(
        package_name="your_grpc_client",
        service_name=service_name,
        service_import=service_import,
        method_name=method_name,
        request_type=request_type,
        methods_list=methods_list
    )

    with open("README.md", "w") as f:
        f.write(readme_content)

    print("README.md updated!")

if __name__ == "__main__":
    main()
