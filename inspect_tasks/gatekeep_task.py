"""Optional Inspect AI task wrapper (works when inspect-ai is installed).

Core Gatekeep does not require Inspect or Docker — use `gatekeep serve` / CLI.
This module lets labs plug the same world into Inspect later.
"""

from __future__ import annotations

# Soft dependency — import only when used
TASK_DOC = """
Gatekeep Inspect task (optional):

  from inspect_tasks.gatekeep_task import gatekeep

  inspect eval inspect_tasks/gatekeep_task.py --model <provider/model>

Without a paid model, prefer:

  gatekeep suite
  gatekeep serve
"""


def get_task_help() -> str:
    return TASK_DOC
