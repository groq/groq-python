import pytest

def build_auth_header(api_key: str) -> dict[str, str]:
    if not api_key:
        raise ValueError("API key required")
    cleaned = api_key.strip()
    if not cleaned:
        raise ValueError("API key cannot be empty")
    return {"Authorization": f"Bearer {cleaned}"}

def test_build_auth_header():
    assert build_auth_header("gsk_123456789") == {"Authorization": "Bearer gsk_123456789"}
    assert build_auth_header("  gsk_abcdef  ") == {"Authorization": "Bearer gsk_abcdef"}

def test_empty_api_key():
    with pytest.raises(ValueError):
        build_auth_header("")
