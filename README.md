# your_grpc_client

This package provides a gRPC client for ApiService using BetterProto.

## Installation
pip install your_grpc_client

## Usage Example
import asyncio
from generated.viuapi import ApiServiceStub, text

async def main():
    client = ApiServiceStub("your.api.endpoint:443")
    request = text(text="Your text here")  # Adjust based on method params
    response = await client.embed_n_v_embed_v2(request)
    print(response)

asyncio.run(main())

## Available Methods
- embed_n_v_embed_v2(text) -> EmbedNVEmbedV2Response
- embed_b_g_e_gemma2(text) -> EmbedBGEGemma2Response

---
Generated automatically from .proto files using GitHub Actions.
