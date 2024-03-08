# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .translation import (
    Translation,
    AsyncTranslation,
    TranslationWithRawResponse,
    AsyncTranslationWithRawResponse,
    TranslationWithStreamingResponse,
    AsyncTranslationWithStreamingResponse,
)
from .transcription import (
    TranscriptionResource,
    AsyncTranscriptionResource,
    TranscriptionResourceWithRawResponse,
    AsyncTranscriptionResourceWithRawResponse,
    TranscriptionResourceWithStreamingResponse,
    AsyncTranscriptionResourceWithStreamingResponse,
)

__all__ = ["Audio", "AsyncAudio"]


class Audio(SyncAPIResource):
    @cached_property
    def transcription(self) -> TranscriptionResource:
        return TranscriptionResource(self._client)

    @cached_property
    def translation(self) -> Translation:
        return Translation(self._client)

    @cached_property
    def with_raw_response(self) -> AudioWithRawResponse:
        return AudioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioWithStreamingResponse:
        return AudioWithStreamingResponse(self)


class AsyncAudio(AsyncAPIResource):
    @cached_property
    def transcription(self) -> AsyncTranscriptionResource:
        return AsyncTranscriptionResource(self._client)

    @cached_property
    def translation(self) -> AsyncTranslation:
        return AsyncTranslation(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAudioWithRawResponse:
        return AsyncAudioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioWithStreamingResponse:
        return AsyncAudioWithStreamingResponse(self)


class AudioWithRawResponse:
    def __init__(self, audio: Audio) -> None:
        self._audio = audio

    @cached_property
    def transcription(self) -> TranscriptionResourceWithRawResponse:
        return TranscriptionResourceWithRawResponse(self._audio.transcription)

    @cached_property
    def translation(self) -> TranslationWithRawResponse:
        return TranslationWithRawResponse(self._audio.translation)


class AsyncAudioWithRawResponse:
    def __init__(self, audio: AsyncAudio) -> None:
        self._audio = audio

    @cached_property
    def transcription(self) -> AsyncTranscriptionResourceWithRawResponse:
        return AsyncTranscriptionResourceWithRawResponse(self._audio.transcription)

    @cached_property
    def translation(self) -> AsyncTranslationWithRawResponse:
        return AsyncTranslationWithRawResponse(self._audio.translation)


class AudioWithStreamingResponse:
    def __init__(self, audio: Audio) -> None:
        self._audio = audio

    @cached_property
    def transcription(self) -> TranscriptionResourceWithStreamingResponse:
        return TranscriptionResourceWithStreamingResponse(self._audio.transcription)

    @cached_property
    def translation(self) -> TranslationWithStreamingResponse:
        return TranslationWithStreamingResponse(self._audio.translation)


class AsyncAudioWithStreamingResponse:
    def __init__(self, audio: AsyncAudio) -> None:
        self._audio = audio

    @cached_property
    def transcription(self) -> AsyncTranscriptionResourceWithStreamingResponse:
        return AsyncTranscriptionResourceWithStreamingResponse(self._audio.transcription)

    @cached_property
    def translation(self) -> AsyncTranslationWithStreamingResponse:
        return AsyncTranslationWithStreamingResponse(self._audio.translation)
