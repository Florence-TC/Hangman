def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        instructions = instructions.replace("Simon says", "I")
        return f"{instructions}"
    elif instructions.endswith("Simon says"):
        instructions = instructions.replace(" Simon says", "")
        return f"I {instructions}"
    else:
        return "I won't do it!"

