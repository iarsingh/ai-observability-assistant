TOOLS = ["pick_board", "summarize"]
WRITES = ("silence", "delete rule",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = "latency" if "latency" in goal.lower() else "errors"
    return {"refused": False, "tools": TOOLS, "board": result, "wrote": False, "applied": False}
