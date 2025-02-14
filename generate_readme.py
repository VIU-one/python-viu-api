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
    request = {request_type}(param="value")
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
    proto_files = [f for f in os.listdir("generated") if f.endswith(".py") and not f.startswith("__")]
    if not proto_files:
        return None, None, None, None

    with open(os.path.join("generated", proto_files[0]), "r") as f:
        content = f.read()

    service_match = re.search(r"class (\w+)Stub\(betterproto\.ServiceStub\):", content)
    request_matches = re.findall(r"async def (\w+)\(self, request: (\w+)", content)

    if not service_match or not request_matches:
        return None, None, None, None

    service_name = service_match.group(1)
    method_name, request_type = request_matches[0]  # Take the first method for example usage
    methods_list = "\n".join([f"- {method}({req})" for method, req in request_matches])
    
    return service_name, proto_files[0].replace(".py", ""), method_name, request_type, methods_list

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
