import sys, uuid
sys.path.insert(0, 'src')
from multi_agent_ecommerce_rag.agent_orchestrator import (
    build_refund_agent, _create_workflow_state, _update_workflow_state,
)

CASES = {
    "A": ("CUST-002", "ORD-28001",
          "Order ORD-28001: Mechanical Keyboard K2, order date 2026-10-10, "
          "status delivered, price 89.99. Customer tier: Standard."),
    "B": ("CUST-001", "ORD-27180",
          "Order ORD-27180: Coffee Maker Deluxe, order date 2026-08-21, "
          "status delivered, price 79.99. Customer tier: Premium."),
    "C": ("CUST-003", "ORD-29003",
          "Order ORD-29003: Bluetooth Speaker, order date 2026-11-09, "
          "status cancelled, price 49.99. Customer tier: Premium."),
    "D": ("CUST-001", "ORD-27176",
          "Order ORD-27176: Wireless Headphones Pro, order date 2026-11-12, "
          "status delivered, price 149.99. Customer tier: Premium."),
}

cid, oid, facts = CASES[sys.argv[1]]
sid = f"smoke-{uuid.uuid4().hex[:8]}"
_create_workflow_state(sid, cid)
_update_workflow_state(sid, {"inventory_agent": facts}, expected_version=0)

agent = build_refund_agent()
print(agent(f"session_id: {sid}. Customer {cid} wants to return order {oid} "
            f"because they no longer need it. Decide and act."))