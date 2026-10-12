from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from groq import Groq, AsyncGroq
from groq.types.audio import Translation, Transcription

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

# A transcript is arbitrary user speech, so it may happen to be valid JSON.
TEXT_BODIES = ["Hello there.", "42", "true", "null", "3.5", "[1, 2]", '{"text": "hi"}']


def _text_response(body: str) -> httpx.Response:
    return httpx.Response(200, headers={"Content-Type": "text/plain; charset=utf-8"}, content=body)


class TestTranscriptions:
    @pytest.mark.parametrize("body", TEXT_BODIES)
    @pytest.mark.respx(base_url=base_url)
    def test_response_format_text_returns_str(self, body: str, respx_mock: MockRouter, client: Groq) -> None:
        respx_mock.post("/openai/v1/audio/transcriptions").mock(return_value=_text_response(body))

        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3", file=("audio.wav", b"RIFF"), response_format="text"
        )
        assert transcription == body

    @pytest.mark.respx(base_url=base_url)
    def test_response_format_json_returns_model(self, respx_mock: MockRouter, client: Groq) -> None:
        respx_mock.post("/openai/v1/audio/transcriptions").mock(
            return_value=httpx.Response(200, json={"text": "Hello there."})
        )

        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3", file=("audio.wav", b"RIFF"), response_format="json"
        )
        assert isinstance(transcription, Transcription)
        assert transcription.text == "Hello there."

    @pytest.mark.parametrize("body", TEXT_BODIES)
    @pytest.mark.respx(base_url=base_url)
    async def test_async_response_format_text_returns_str(
        self, body: str, respx_mock: MockRouter, async_client: AsyncGroq
    ) -> None:
        respx_mock.post("/openai/v1/audio/transcriptions").mock(return_value=_text_response(body))

        transcription = await async_client.audio.transcriptions.create(
            model="whisper-large-v3", file=("audio.wav", b"RIFF"), response_format="text"
        )
        assert transcription == body


class TestTranslations:
    @pytest.mark.parametrize("body", TEXT_BODIES)
    @pytest.mark.respx(base_url=base_url)
    def test_response_format_text_returns_str(self, body: str, respx_mock: MockRouter, client: Groq) -> None:
        respx_mock.post("/openai/v1/audio/translations").mock(return_value=_text_response(body))

        translation = client.audio.translations.create(
            model="whisper-large-v3", file=("audio.wav", b"RIFF"), response_format="text"
        )
        assert translation == body

    @pytest.mark.respx(base_url=base_url)
    def test_response_format_json_returns_model(self, respx_mock: MockRouter, client: Groq) -> None:
        respx_mock.post("/openai/v1/audio/translations").mock(
            return_value=httpx.Response(200, json={"text": "Hello there."})
        )

        translation = client.audio.translations.create(
            model="whisper-large-v3", file=("audio.wav", b"RIFF"), response_format="json"
        )
        assert isinstance(translation, Translation)
        assert translation.text == "Hello there."

    @pytest.mark.parametrize("body", TEXT_BODIES)
    @pytest.mark.respx(base_url=base_url)
    async def test_async_response_format_text_returns_str(
        self, body: str, respx_mock: MockRouter, async_client: AsyncGroq
    ) -> None:
        respx_mock.post("/openai/v1/audio/translations").mock(return_value=_text_response(body))

        translation = await async_client.audio.translations.create(
            model="whisper-large-v3", file=("audio.wav", b"RIFF"), response_format="text"
        )
        assert translation == body
