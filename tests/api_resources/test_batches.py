# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from groq import Groq, AsyncGroq
from groq.types import (
    BatchListResponse,
    BatchCancelResponse,
    BatchCreateResponse,
    BatchRetrieveResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Groq) -> None:
        batch = client.batches.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Groq) -> None:
        batch = client.batches.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Groq) -> None:
        response = client.batches.with_raw_response.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Groq) -> None:
        with client.batches.with_streaming_response.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Groq) -> None:
        batch = client.batches.retrieve(
            "batch_id",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Groq) -> None:
        response = client.batches.with_raw_response.retrieve(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Groq) -> None:
        with client.batches.with_streaming_response.retrieve(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Groq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Groq) -> None:
        batch = client.batches.list()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Groq) -> None:
        response = client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Groq) -> None:
        with client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchListResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Groq) -> None:
        batch = client.batches.cancel(
            "batch_id",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Groq) -> None:
        response = client.batches.with_raw_response.cancel(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Groq) -> None:
        with client.batches.with_streaming_response.cancel(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Groq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.cancel(
                "",
            )


class TestAsyncBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGroq) -> None:
        batch = await async_client.batches.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGroq) -> None:
        batch = await async_client.batches.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGroq) -> None:
        response = await async_client.batches.with_raw_response.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGroq) -> None:
        async with async_client.batches.with_streaming_response.create(
            completion_window="completion_window",
            endpoint="/v1/chat/completions",
            input_file_id="input_file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGroq) -> None:
        batch = await async_client.batches.retrieve(
            "batch_id",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGroq) -> None:
        response = await async_client.batches.with_raw_response.retrieve(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGroq) -> None:
        async with async_client.batches.with_streaming_response.retrieve(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGroq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGroq) -> None:
        batch = await async_client.batches.list()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGroq) -> None:
        response = await async_client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGroq) -> None:
        async with async_client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchListResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncGroq) -> None:
        batch = await async_client.batches.cancel(
            "batch_id",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncGroq) -> None:
        response = await async_client.batches.with_raw_response.cancel(
            "batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncGroq) -> None:
        async with async_client.batches.with_streaming_response.cancel(
            "batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncGroq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.cancel(
                "",
            )
