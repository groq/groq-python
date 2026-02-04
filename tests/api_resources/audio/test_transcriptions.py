# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from groq import Groq, AsyncGroq
from tests.utils import assert_matches_type
from groq.types.audio import Transcription

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    def test_method_create(self, client: Groq) -> None:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    def test_method_create_with_all_params(self, client: Groq) -> None:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=b"raw file contents",
            language="string",
            prompt="prompt",
            response_format="json",
            temperature=0,
            timestamp_granularities=["word"],
            url="url",
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    def test_raw_response_create(self, client: Groq) -> None:
        response = client.audio.transcriptions.with_raw_response.create(
            model="whisper-large-v3-turbo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(Transcription, transcription, path=["response"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    def test_streaming_response_create(self, client: Groq) -> None:
        with client.audio.transcriptions.with_streaming_response.create(
            model="whisper-large-v3-turbo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(Transcription, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    async def test_method_create(self, async_client: AsyncGroq) -> None:
        transcription = await async_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGroq) -> None:
        transcription = await async_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=b"raw file contents",
            language="string",
            prompt="prompt",
            response_format="json",
            temperature=0,
            timestamp_granularities=["word"],
            url="url",
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGroq) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.create(
            model="whisper-large-v3-turbo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(Transcription, transcription, path=["response"])

    @pytest.mark.skip(reason="Unsupported either condition")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGroq) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.create(
            model="whisper-large-v3-turbo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(Transcription, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True
