# Central configuration for the project, including AWS region and knowledge base IDs.
# Reads resource names and ARNs from CloudFormation stack exports to avoid
# hard-coded AWS resource identifiers.

import os
from dotenv import load_dotenv

# REGION & PROJECT SETTINGS
AWS_REGION   = os.environ.get('AWS_REGION', 'us-east-1')
PROJECT_NAME = os.environ.get('PROJECT_NAME', 'udacity-agentcore')

# FOUNDATION MODELS
# Orchestrator agent: Claude Haiku 4.5 - fast, cost-efficient routing decisions
ORCHESTRATOR_MODEL_ID = "us.anthropic.claude-haiku-4-5-20251001-v1:0"

# Worker agents: Claude Sonnet 4.5 - more capable for reasoning and generation
WORKER_MODEL_ID = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"

# CLOUDFORMATION EXPORTS LOADER (lazy, cached)
_exports_cache = None