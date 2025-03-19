# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.audio import speech_create_params
from ..._base_client import make_request_options

__all__ = ["Speech", "AsyncSpeech"]


class Speech(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/groq/groq-python#accessing-raw-response-data-eg-headers
        """
        return SpeechWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/groq/groq-python#with_streaming_response
        """
        return SpeechWithStreamingResponse(self)

    def create(
        self,
        *,
        input: str,
        model: str,
        voice: str,
        response_format: Literal["wav"] | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Generates audio from the input text.

        Args:
          input: The text to generate audio for.

          model: One of the available TTS models

          voice: The voice to use when generating the audio.

          response_format: The format to audio in. Supported formats are `wav`.

          speed: The speed of the generated audio. 1.0 is the only supported value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/openai/v1/audio/speech",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "voice": voice,
                    "response_format": response_format,
                    "speed": speed,
                },
                speech_create_params.SpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncSpeech(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/groq/groq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/groq/groq-python#with_streaming_response
        """
        return AsyncSpeechWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: str,
        model: str,
        voice: str,
        response_format: Literal["wav"] | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Generates audio from the input text.

        Args:
          input: The text to generate audio for.

          model: One of the available TTS models

          voice: The voice to use when generating the audio.

          response_format: The format to audio in. Supported formats are `wav`.

          speed: The speed of the generated audio. 1.0 is the only supported value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/openai/v1/audio/speech",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "voice": voice,
                    "response_format": response_format,
                    "speed": speed,
                },
                speech_create_params.SpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class SpeechWithRawResponse:
    def __init__(self, speech: Speech) -> None:
        self._speech = speech

        self.create = to_custom_raw_response_wrapper(
            speech.create,
            BinaryAPIResponse,
        )


class AsyncSpeechWithRawResponse:
    def __init__(self, speech: AsyncSpeech) -> None:
        self._speech = speech

        self.create = async_to_custom_raw_response_wrapper(
            speech.create,
            AsyncBinaryAPIResponse,
        )


class SpeechWithStreamingResponse:
    def __init__(self, speech: Speech) -> None:
        self._speech = speech

        self.create = to_custom_streamed_response_wrapper(
            speech.create,
            StreamedBinaryAPIResponse,
        )


class AsyncSpeechWithStreamingResponse:
    def __init__(self, speech: AsyncSpeech) -> None:
        self._speech = speech

        self.create = async_to_custom_streamed_response_wrapper(
            speech.create,
            AsyncStreamedBinaryAPIResponse,
        )
