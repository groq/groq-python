# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from groq import Groq, AsyncGroq
from groq.types import CreateEmbeddingResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Groq) -> None:
        embedding = client.embeddings.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
        )
        assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Groq) -> None:
        embedding = client.embeddings.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
            encoding_format="float",
            user="user",
        )
        assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Groq) -> None:
        response = client.embeddings.with_raw_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Groq) -> None:
        with client.embeddings.with_streaming_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGroq) -> None:
        embedding = await async_client.embeddings.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
        )
        assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGroq) -> None:
        embedding = await async_client.embeddings.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
            encoding_format="float",
            user="user",
        )
        assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGroq) -> None:
        response = await async_client.embeddings.with_raw_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGroq) -> None:
        async with async_client.embeddings.with_streaming_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="nomic-embed-text-v1_5",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(CreateEmbeddingResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
