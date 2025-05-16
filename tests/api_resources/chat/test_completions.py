# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from groq import Groq, AsyncGroq
from tests.utils import assert_matches_type
from groq.types.chat import ChatCompletion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Groq) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Groq) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                    "name": "name",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            exclude_domains=["string"],
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            include_domains=["string"],
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            metadata={"foo": "string"},
            n=1,
            parallel_tool_calls=True,
            presence_penalty=-2,
            reasoning_format="hidden",
            response_format={"type": "text"},
            search_settings={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
                "include_images": True,
            },
            seed=0,
            service_tier="auto",
            stop="\n",
            store=True,
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_logprobs=0,
            top_p=1,
            user="user",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Groq) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Groq) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(ChatCompletion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGroq) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGroq) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                    "name": "name",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            exclude_domains=["string"],
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "name": "name",
                    "description": "description",
                    "parameters": {"foo": "bar"},
                }
            ],
            include_domains=["string"],
            logit_bias={"foo": 0},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            metadata={"foo": "string"},
            n=1,
            parallel_tool_calls=True,
            presence_penalty=-2,
            reasoning_format="hidden",
            response_format={"type": "text"},
            search_settings={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
                "include_images": True,
            },
            seed=0,
            service_tier="auto",
            stop="\n",
            store=True,
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_logprobs=0,
            top_p=1,
            user="user",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGroq) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGroq) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "content",
                    "role": "system",
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(ChatCompletion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
