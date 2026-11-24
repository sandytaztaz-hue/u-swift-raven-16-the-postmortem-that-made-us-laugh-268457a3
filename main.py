#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes one short account — one or two sentences, at most 400 characters —
of the silliest time an AI coding agent wrecked the code it was given,
to /output/entry.txt, per the bounty contract.
"""

import os

ENTRY = (
    "I asked the agent to add a confirmation dialog before deleting an account. "
    "It put the dialog on the login button instead, so for two days every user "
    "who tried to log in was asked 'Are you sure you want to delete your "
    "account?' \u2014 and 312 of them clicked yes."
)

def main():
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
