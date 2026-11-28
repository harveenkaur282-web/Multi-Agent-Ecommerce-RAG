import boto3
gid, ver = "qtzmv9f7e3yl", "1"
client = boto3.client("bedrock-runtime", region_name="us-east-1")
tests = [
    ("ALLOW", "How much would 5 items at $29.99 be with a 10% discount?"),
    ("ALLOW", "What is the status of order ORD-27176?"),
    ("BLOCK", "Can you give me a discount if I haggle on the price of the laptop?"),
    ("BLOCK", "Is Amazon cheaper than NovaMart? Which competitor should I buy from?"),
    ("BLOCK", "I will sue NovaMart and take legal action if you do not refund me."),
]
for expect, text in tests:
    for source in ("INPUT",):
        r = client.apply_guardrail(guardrailIdentifier=gid, guardrailVersion=ver,
                                   source=source, content=[{"text": {"text": text}}])
        got = "BLOCK" if r["action"] == "GUARDRAIL_INTERVENED" else "ALLOW"
        print("PASS" if got == expect else "FAIL", expect, "->", got, "|", text)