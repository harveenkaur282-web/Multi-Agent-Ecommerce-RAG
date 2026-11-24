# Amazon Bedrock AgentCore

This directory contains the AgentCore CLI project configuration and its CDK
deployment scaffold. It was added from the Udacity course starter and is not
deployed yet.

## Files and directories

- `agentcore.json` declares the runtime entry point, runtime version, code
  location, and other AgentCore resources.
- `aws-targets.json` lists AWS account/Region deployment targets. It is
  intentionally empty; add a target only when ready to deploy.
- `.llm-context/` contains read-only schema references for the two JSON
  configuration files.
- `cdk/` contains the TypeScript CDK application used by the AgentCore CLI.
- `.gitignore` excludes local credentials, CLI state, and generated build
  artifacts.

The configured runtime currently expects `agent_orchestrator.py` in
`build/runtime/` and targets Python 3.12. That runtime package and entry point
have not been created, so the scaffold is not ready to deploy. The main
repository's local Python environment may use a different Python version.

## Validate the CDK scaffold

From this directory:

```powershell
cd cdk
npm ci
npm run build
npm test
```

Do not run `agentcore deploy` until the runtime code/package exists and a
deployment target has been intentionally configured. The existing
`infrastructure/starter_stack.yaml` remains the source for the currently
deployed DynamoDB, S3, IAM, and CloudWatch resources.

Shared Python agent logic belongs in
`src/multi_agent_ecommerce_rag/`; the runtime entry point can import it when the
agent implementation is added.
