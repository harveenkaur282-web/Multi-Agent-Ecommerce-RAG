# Multi-Agent-Ecommerce-RAG

A production-grade multi-agent customer support system using Amazon Bedrock AgentCore and the Strands Agents SDK

The system consists of five AI agents working together in an Orchestrator → Workers hierarchy:

An Orchestrator Agent that understands customer intent and routes requests to the right specialist
An Inventory Agent that retrieves order and customer data from DynamoDB
A Policy Agent that answers policy questions using parallel multi-agent RAG across three Knowledge Bases
A Refund Agent that makes return eligibility decisions based on order data and policy rules
A Communication Agent that composes the final customer-facing response
The system is deployed to AgentCore Runtime with Bedrock Guardrails for safety, session memory for multi-turn conversations, and CloudWatch/X-Ray observability for monitoring and debugging.

## Deliverables
Need to submit:

Completed src/agent_orchestrator.py — All TODO items implemented (Tasks 2, 3, 4, 6)
Three Bedrock Knowledge Bases — Created in the AWS Console with synced data sources (Task 5)
Populated .env file — With your Knowledge Base IDs, AgentCore Runtime ARN, and Guardrail configuration
X-Ray Service Map screenshot — Showing the full trace of an end-to-end request through your multi-agent system (Task 6)
