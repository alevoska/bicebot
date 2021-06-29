import random
import re

MAX_DICE_COUNT = 20


def roll(num: int) -> list[int]:
    rolls = [random.randint(1, 6) for n in range(num)]
    return rolls


def parsecommand(line: str, prefix: str) -> str:
    if len(line) < 2 or line[0] != prefix:
        return None

    statement = line[len(prefix):].split()
    command = statement[0]
    resist = (command[-1] == "r")

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

    if not resist:
        if result == 6:
            if rolls.count(6) >= 2:
                comment = "Critical Success"
            else:
                comment = "Full Success"
        elif result >= 4:
            comment = "Partial Success"
        else:
            comment = "Bad Outcome"
    else:
        if rolls.count(6) > 1:
            comment = "Critical! Recover 1 stress"
        else:
            comment = f"Take {6 - result} stress"

    return f"**{comment}!**\n[**{result}**] from {rolls}"
