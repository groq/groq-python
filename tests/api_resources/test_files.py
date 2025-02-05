# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from groq import Groq, AsyncGroq
from groq.types import (
    FileInfoResponse,
    FileListResponse,
    FileCreateResponse,
    FileDeleteResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Groq) -> None:
        file = client.files.create(
            file=b"raw file contents",
            purpose="batch",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Groq) -> None:
        response = client.files.with_raw_response.create(
            file=b"raw file contents",
            purpose="batch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Groq) -> None:
        with client.files.with_streaming_response.create(
            file=b"raw file contents",
            purpose="batch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Groq) -> None:
        file = client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Groq) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Groq) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Groq) -> None:
        file = client.files.delete(
            "file_id",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Groq) -> None:
        response = client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Groq) -> None:
        with client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Groq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_content(self, client: Groq) -> None:
        file = client.files.content(
            "file_id",
        )
        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_raw_response_content(self, client: Groq) -> None:
        response = client.files.with_raw_response.content(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_streaming_response_content(self, client: Groq) -> None:
        with client.files.with_streaming_response.content(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_content(self, client: Groq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.content(
                "",
            )

    @parametrize
    def test_method_info(self, client: Groq) -> None:
        file = client.files.info(
            "file_id",
        )
        assert_matches_type(FileInfoResponse, file, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Groq) -> None:
        response = client.files.with_raw_response.info(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileInfoResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Groq) -> None:
        with client.files.with_streaming_response.info(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileInfoResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_info(self, client: Groq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.info(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGroq) -> None:
        file = await async_client.files.create(
            file=b"raw file contents",
            purpose="batch",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGroq) -> None:
        response = await async_client.files.with_raw_response.create(
            file=b"raw file contents",
            purpose="batch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGroq) -> None:
        async with async_client.files.with_streaming_response.create(
            file=b"raw file contents",
            purpose="batch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGroq) -> None:
        file = await async_client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGroq) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGroq) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGroq) -> None:
        file = await async_client.files.delete(
            "file_id",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGroq) -> None:
        response = await async_client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGroq) -> None:
        async with async_client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGroq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_content(self, async_client: AsyncGroq) -> None:
        file = await async_client.files.content(
            "file_id",
        )
        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_raw_response_content(self, async_client: AsyncGroq) -> None:
        response = await async_client.files.with_raw_response.content(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_streaming_response_content(self, async_client: AsyncGroq) -> None:
        async with async_client.files.with_streaming_response.content(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_content(self, async_client: AsyncGroq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.content(
                "",
            )

    @parametrize
    async def test_method_info(self, async_client: AsyncGroq) -> None:
        file = await async_client.files.info(
            "file_id",
        )
        assert_matches_type(FileInfoResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncGroq) -> None:
        response = await async_client.files.with_raw_response.info(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileInfoResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncGroq) -> None:
        async with async_client.files.with_streaming_response.info(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileInfoResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_info(self, async_client: AsyncGroq) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.info(
                "",
            )
