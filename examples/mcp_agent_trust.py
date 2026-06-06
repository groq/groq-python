#!/usr/bin/env -S rye run python
"""
Example: Verify AI agent trust via TWZRD Agent Intel, then route through Groq.

TWZRD Agent Intel (https://intel.twzrd.xyz) scores autonomous agents on Solana
based on on-chain transaction history. This example:

1. Calls the free TWZRD MCP server to get a trust score for an agent wallet.
2. Passes the raw score to Groq (llama-3.3-70b-versatile) for a plain-language
   recommendation on whether the agent is safe to transact with.

Install: pip install groq mcp
"""

import asyncio
import json
import os

from groq import Groq
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


TWZRD_MCP_URL = "https://intel.twzrd.xyz/mcp"
GROQ_MODEL = "llama-3.3-70b-versatile"


async def get_agent_score(wallet: str) -> dict:
    """Return the TWZRD trust score for a Solana wallet."""
    async with streamablehttp_client(TWZRD_MCP_URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("score_agent", {"wallet": wallet})
            return json.loads(result.content[0].text)


def interpret_score_with_groq(wallet: str, score_data: dict) -> str:
    """Ask Groq to explain what the trust score means."""
    client = Groq()  # reads GROQ_API_KEY from environment

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a concise security advisor for AI agent payment systems. "
                    "Given a trust score, recommend whether to proceed."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Agent wallet: {wallet}\n"
                    f"Trust score data:\n{json.dumps(score_data, indent=2)}\n\n"
                    "Should a payment system route funds through this agent? "
                    "Answer in 2-3 sentences."
                ),
            },
        ],
        temperature=0.3,
        max_tokens=256,
    )
    return response.choices[0].message.content


async def main() -> None:
    # A known active agent on Solana mainnet (has 48+ x402 transactions)
    wallet = "D1QkbFJKiPsymJ65RKHhF6DFB8sPMfpBaFBzuHKfJGWi"

    print(f"Fetching TWZRD trust score for {wallet} ...")
    score_data = await get_agent_score(wallet)
    print("Score data:", json.dumps(score_data, indent=2))

    print("\nAsking Groq for a recommendation ...")
    recommendation = interpret_score_with_groq(wallet, score_data)
    print("Groq says:", recommendation)


if __name__ == "__main__":
    asyncio.run(main())
