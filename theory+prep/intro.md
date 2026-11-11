1. Design multi-agent architectures using hierarchical, flat, and hybrid patterns with clear agent boundaries, communication paths, and tradeoffs.
2. Implement multi-agent systems on Amazon Bedrock AgentCore and the Strands Agents SDK, assigning the right foundation model (Nova Lite, Nova Pro, Claude) to each agent role.
3. Orchestrate and route work across agents with sequential, parallel, and conditional workflows, including content- and LLM-based routing and Saga-style state coordination on DynamoDB and AgentCore Memory.
4. Build multi-agent RAG with specialized retrievers over Bedrock Knowledge Bases backed by Amazon S3 Vectors.
5. Deploy multi-agent systems to production with Bedrock Guardrails, AgentCore Gateway, CloudWatch + X-Ray observability, and runtime versioning.

# project preview
multi agent customer service for novamart-fictional company
5 collaborating agents handle order lookups, refund decisions, and policy questions 
policy agent powered by parallel multi-agent RAG across three Bedrock Knowledge bases
system deployed to agentcore runtime with bedrock guardrails, session memory, and cloudwatch/x-ray observability

