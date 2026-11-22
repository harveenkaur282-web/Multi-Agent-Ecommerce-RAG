"""Load project settings from environment variables and an optional .env file."""

import os
from collections.abc import Mapping
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    aws_region: str
    project_name: str
    returns_kb_id: str | None
    shipping_kb_id: str | None
    warranty_kb_id: str | None


def get_settings(environ: Mapping[str, str] | None = None) -> Settings:
    """Return settings from the environment, loading .env when no mapping is given."""
    if environ is None:
        load_dotenv()
        environ = os.environ

    return Settings(
        aws_region=environ.get("AWS_REGION", "").strip() or "us-east-1",
        project_name=environ.get("PROJECT_NAME", "").strip() or "udacity-agentcore",
        returns_kb_id=environ.get("RETURNS_KB_ID", "").strip() or None,
        shipping_kb_id=environ.get("SHIPPING_KB_ID", "").strip() or None,
        warranty_kb_id=environ.get("WARRANTY_KB_ID", "").strip() or None,
    )
