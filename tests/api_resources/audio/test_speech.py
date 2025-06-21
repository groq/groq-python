# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from groq import Groq, AsyncGroq
from groq._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Groq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.audio.speech.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Groq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.audio.speech.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
            response_format="flac",
            sample_rate=48000,
            speed=1,
        )
        assert speech.is_closed
        assert speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Groq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = client.audio.speech.with_raw_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert speech.json() == {"foo": "bar"}
        assert isinstance(speech, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Groq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.audio.speech.with_streaming_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, StreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True


class TestAsyncSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncGroq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.audio.speech.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncGroq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.audio.speech.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
            response_format="flac",
            sample_rate=48000,
            speed=1,
        )
        assert speech.is_closed
        assert await speech.json() == {"foo": "bar"}
        assert cast(Any, speech.is_closed) is True
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncGroq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        speech = await async_client.audio.speech.with_raw_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
        )

        assert speech.is_closed is True
        assert speech.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await speech.json() == {"foo": "bar"}
        assert isinstance(speech, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncGroq, respx_mock: MockRouter) -> None:
        respx_mock.post("/openai/v1/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.audio.speech.with_streaming_response.create(
            input="The quick brown fox jumped over the lazy dog",
            model="playai-tts",
            voice="Fritz-PlayAI",
        ) as speech:
            assert not speech.is_closed
            assert speech.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await speech.json() == {"foo": "bar"}
            assert cast(Any, speech.is_closed) is True
            assert isinstance(speech, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, speech.is_closed) is True
