# Multi-Agent-Ecommerce-RAG

A production-grade multi-agent customer support system using Amazon Bedrock AgentCore and the Strands Agents SDK

The system consists of five AI agents working together in an Orchestrator → Workers hierarchy:

An Orchestrator Agent that understands customer intent and routes requests to the right specialist
An Inventory Agent that retrieves order and customer data from DynamoDB
A Policy Agent that answers policy questions using parallel multi-agent RAG across three Knowledge Bases
A Refund Agent that makes return eligibility decisions based on order data and policy rules
A Communication Agent that composes the final customer-facing response
The system is deployed to AgentCore Runtime with Bedrock Guardrails for safety, session memory for multi-turn conversations, and CloudWatch/X-Ray observability for monitoring and debugging.
