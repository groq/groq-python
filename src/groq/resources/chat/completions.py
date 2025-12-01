# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.chat.chat_completion import ChatCompletion
from ...types.chat.chat_completion_chunk import ChatCompletionChunk
from ...types.chat.chat_completion_tool_param import ChatCompletionToolParam
from ...types.chat.chat_completion_message_param import ChatCompletionMessageParam
from ...types.chat.chat_completion_tool_choice_option_param import ChatCompletionToolChoiceOptionParam

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/groq/groq-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/groq/groq-python#with_streaming_response
        """
        return CompletionsWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion: ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Literal[True],
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ChatCompletionChunk]: ...

    @overload
    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: bool,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]: ...

    def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use. For details on which models are compatible with the Chat
              API, see available [models](https://console.groq.com/docs/models)

          citation_options: Whether to enable citations in the response. When enabled, the model will
              include citations for information retrieved from provided documents or web
              searches.

          compound_custom: Custom configuration of models and tools for Compound.

          disable_tool_validation: If set to true, groq will return called tools without validating that the tool
              is present in request.tools. tool_choice=required/none will still be enforced,
              but the request cannot require a specific tool be used.

          documents: A list of documents to provide context for the conversation. Each document
              contains text that can be referenced by the model.

          exclude_domains: Deprecated: Use search_settings.exclude_domains instead. A list of domains to
              exclude from the search results when the model uses a web search tool.

          frequency_penalty: This is not yet supported by any of our models. Number between -2.0 and 2.0.
              Positive values penalize new tokens based on their existing frequency in the
              text so far, decreasing the model's likelihood to repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          include_domains: Deprecated: Use search_settings.include_domains instead. A list of domains to
              include in the search results when the model uses a web search tool.

          include_reasoning: Whether to include reasoning in the response. If true, the response will include
              a `reasoning` field. If false, the model's reasoning will not be included in the
              response. This field is mutually exclusive with `reasoning_format`.

          logit_bias: This is not yet supported by any of our models. Modify the likelihood of
              specified tokens appearing in the completion.

          logprobs: This is not yet supported by any of our models. Whether to return log
              probabilities of the output tokens or not. If true, returns the log
              probabilities of each output token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: Deprecated in favor of `max_completion_tokens`. The maximum number of tokens
              that can be generated in the chat completion. The total length of input tokens
              and generated tokens is limited by the model's context length.

          metadata: This parameter is not currently supported.

          n: How many chat completion choices to generate for each input message. Note that
              the current moment, only n=1 is supported. Other values will result in a 400
              response.

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: This is not yet supported by any of our models. Number between -2.0 and 2.0.
              Positive values penalize new tokens based on whether they appear in the text so
              far, increasing the model's likelihood to talk about new topics.

          reasoning_effort: qwen3 models support the following values Set to 'none' to disable reasoning.
              Set to 'default' or null to let Qwen reason.

              openai/gpt-oss-20b and openai/gpt-oss-120b support 'low', 'medium', or 'high'.
              'medium' is the default value.

          reasoning_format: Specifies how to output reasoning tokens This field is mutually exclusive with
              `include_reasoning`.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. `json_schema`
              response format is only available on
              [supported models](https://console.groq.com/docs/structured-outputs#supported-models).
              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          search_settings: Settings for web search functionality when the model uses a web search tool.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed, and you should refer to the
              `system_fingerprint` response parameter to monitor changes in the backend.

          service_tier: The service tier to use for the request. Defaults to `on_demand`.

              - `auto` will automatically select the highest tier available within the rate
                limits of your organization.
              - `flex` uses the flex tier, which will succeed or fail quickly.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: This parameter is not currently supported.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message. [Example code](/docs/text-chat#streaming-a-chat-completion).

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or top_p but not
              both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: This is not yet supported by any of our models. An integer between 0 and 20
              specifying the number of most likely tokens to return at each token position,
              each with an associated log probability. `logprobs` must be set to `true` if
              this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or temperature but not both.

          user: A unique identifier representing your end-user, which can help us monitor and
              detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/openai/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "citation_options": citation_options,
                    "compound_custom": compound_custom,
                    "disable_tool_validation": disable_tool_validation,
                    "documents": documents,
                    "exclude_domains": exclude_domains,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "include_domains": include_domains,
                    "include_reasoning": include_reasoning,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "reasoning_format": reasoning_format,
                    "response_format": response_format,
                    "search_settings": search_settings,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/groq/groq-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/groq/groq-python#with_streaming_response
        """
        return AsyncCompletionsWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion: ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Literal[True],
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ChatCompletionChunk]: ...

    @overload
    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: bool,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]: ...

    async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        model: Union[
            str,
            Literal[
                "compound-beta",
                "compound-beta-mini",
                "gemma2-9b-it",
                "llama-3.1-8b-instant",
                "llama-3.3-70b-versatile",
                "meta-llama/llama-4-maverick-17b-128e-instruct",
                "meta-llama/llama-4-scout-17b-16e-instruct",
                "meta-llama/llama-guard-4-12b",
                "moonshotai/kimi-k2-instruct",
                "openai/gpt-oss-120b",
                "openai/gpt-oss-20b",
                "qwen/qwen3-32b",
            ],
        ],
        citation_options: Optional[Literal["enabled", "disabled"]] | Omit = omit,
        compound_custom: Optional[completion_create_params.CompoundCustom] | Omit = omit,
        disable_tool_validation: Optional[bool] | Omit = omit,
        documents: Optional[Iterable[completion_create_params.Document]] | Omit = omit,
        exclude_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        function_call: Optional[completion_create_params.FunctionCall] | Omit = omit,
        functions: Optional[Iterable[completion_create_params.Function]] | Omit = omit,
        include_domains: Optional[SequenceNotStr[str]] | Omit = omit,
        include_reasoning: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        n: Optional[int] | Omit = omit,
        parallel_tool_calls: Optional[bool] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        reasoning_effort: Optional[Literal["none", "default", "low", "medium", "high"]] | Omit = omit,
        reasoning_format: Optional[Literal["hidden", "raw", "parsed"]] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        search_settings: Optional[completion_create_params.SearchSettings] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        store: Optional[bool] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[ChatCompletionToolChoiceOptionParam] | Omit = omit,
        tools: Optional[Iterable[ChatCompletionToolParam]] | Omit = omit,
        top_logprobs: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        user: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use. For details on which models are compatible with the Chat
              API, see available [models](https://console.groq.com/docs/models)

          citation_options: Whether to enable citations in the response. When enabled, the model will
              include citations for information retrieved from provided documents or web
              searches.

          compound_custom: Custom configuration of models and tools for Compound.

          disable_tool_validation: If set to true, groq will return called tools without validating that the tool
              is present in request.tools. tool_choice=required/none will still be enforced,
              but the request cannot require a specific tool be used.

          documents: A list of documents to provide context for the conversation. Each document
              contains text that can be referenced by the model.

          exclude_domains: Deprecated: Use search_settings.exclude_domains instead. A list of domains to
              exclude from the search results when the model uses a web search tool.

          frequency_penalty: This is not yet supported by any of our models. Number between -2.0 and 2.0.
              Positive values penalize new tokens based on their existing frequency in the
              text so far, decreasing the model's likelihood to repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          include_domains: Deprecated: Use search_settings.include_domains instead. A list of domains to
              include in the search results when the model uses a web search tool.

          include_reasoning: Whether to include reasoning in the response. If true, the response will include
              a `reasoning` field. If false, the model's reasoning will not be included in the
              response. This field is mutually exclusive with `reasoning_format`.

          logit_bias: This is not yet supported by any of our models. Modify the likelihood of
              specified tokens appearing in the completion.

          logprobs: This is not yet supported by any of our models. Whether to return log
              probabilities of the output tokens or not. If true, returns the log
              probabilities of each output token returned in the `content` of `message`.

          max_completion_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          max_tokens: Deprecated in favor of `max_completion_tokens`. The maximum number of tokens
              that can be generated in the chat completion. The total length of input tokens
              and generated tokens is limited by the model's context length.

          metadata: This parameter is not currently supported.

          n: How many chat completion choices to generate for each input message. Note that
              the current moment, only n=1 is supported. Other values will result in a 400
              response.

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: This is not yet supported by any of our models. Number between -2.0 and 2.0.
              Positive values penalize new tokens based on whether they appear in the text so
              far, increasing the model's likelihood to talk about new topics.

          reasoning_effort: qwen3 models support the following values Set to 'none' to disable reasoning.
              Set to 'default' or null to let Qwen reason.

              openai/gpt-oss-20b and openai/gpt-oss-120b support 'low', 'medium', or 'high'.
              'medium' is the default value.

          reasoning_format: Specifies how to output reasoning tokens This field is mutually exclusive with
              `include_reasoning`.

          response_format: An object specifying the format that the model must output. Setting to
              `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs
              which ensures the model will match your supplied JSON schema. `json_schema`
              response format is only available on
              [supported models](https://console.groq.com/docs/structured-outputs#supported-models).
              Setting to `{ "type": "json_object" }` enables the older JSON mode, which
              ensures the message the model generates is valid JSON. Using `json_schema` is
              preferred for models that support it.

          search_settings: Settings for web search functionality when the model uses a web search tool.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed, and you should refer to the
              `system_fingerprint` response parameter to monitor changes in the backend.

          service_tier: The service tier to use for the request. Defaults to `on_demand`.

              - `auto` will automatically select the highest tier available within the rate
                limits of your organization.
              - `flex` uses the flex tier, which will succeed or fail quickly.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          store: This parameter is not currently supported.

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message. [Example code](/docs/text-chat#streaming-a-chat-completion).

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or top_p but not
              both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for. A max of 128 functions are supported.

          top_logprobs: This is not yet supported by any of our models. An integer between 0 and 20
              specifying the number of most likely tokens to return at each token position,
              each with an associated log probability. `logprobs` must be set to `true` if
              this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or temperature but not both.

          user: A unique identifier representing your end-user, which can help us monitor and
              detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/openai/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "citation_options": citation_options,
                    "compound_custom": compound_custom,
                    "disable_tool_validation": disable_tool_validation,
                    "documents": documents,
                    "exclude_domains": exclude_domains,
                    "frequency_penalty": frequency_penalty,
                    "function_call": function_call,
                    "functions": functions,
                    "include_domains": include_domains,
                    "include_reasoning": include_reasoning,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "n": n,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "reasoning_format": reasoning_format,
                    "response_format": response_format,
                    "search_settings": search_settings,
                    "seed": seed,
                    "service_tier": service_tier,
                    "stop": stop,
                    "store": store,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "user": user,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )


class CompletionsWithRawResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithRawResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsWithStreamingResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithStreamingResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
