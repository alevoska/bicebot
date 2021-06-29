import random
import re

MAX_DICE_COUNT = 20


def roll(num: int) -> list[int]:
    rolls = [random.randint(1, 6) for n in range(num)]
    return rolls


def parsecommand(line: str) -> str:
    statement = line.split()
    command = statement[0]
    resist = (command[-1] == "r")
    heat = (command[-1] == "h")
    vice = (command[-1] == "v")

    try:
        count = int(re.sub(r"[^0-9]", "", command))
        if count > MAX_DICE_COUNT:
            raise ValueError()
    except ValueError:
        return "Invalid roll"

    if count == 0:
        rolls = roll(2)
        result = min(rolls)
    else:
        rolls = roll(count)
        result = max(rolls)

    if resist:
        if rolls.count(6) > 1:
            comment = "Critical! Recover 1 stress"
        else:
            comment = f"Take {6 - result} stress"
    elif heat:
        if result == 6:
            if rolls.count(6) >= 2:
                comment = "Reduce 5 Heat"
            else:
                comment = "Reduce 3 Heat"
        elif result >= 4:
            comment = "Reduce 2 Heat"
        else:
            comment = "Reduce 1 Heat"
    elif vice:
        comment = f"Clear {result} Stress"
    else:
        if result == 6:
            if rolls.count(6) >= 2:
                comment = "Critical Success"
            else:
                comment = "Full Success"
        elif result >= 4:
            comment = "Partial Success"
        else:
            comment = "Bad Outcome"

    return f"**{comment}!**\n[**{result}**] from {rolls}"
