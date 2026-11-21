"""Small status helper used to demonstrate static analysis."""


def status_message(service: str) -> str:
    """Return a human-readable status for a named training service."""
    return f"{service}: operational"
