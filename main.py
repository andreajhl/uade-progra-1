"""
Cinema Management Application - Clean Entry Point
Refactored to separate concerns: application logic, error handling, and execution modes.
"""

import sys
from core.execution_modes import determine_and_run_application_mode


def main() -> None:
    """
    Clean main entry point.
    Delegates to execution mode handlers for proper separation of concerns.
    """
    determine_and_run_application_mode(sys.argv)


if __name__ == "__main__":
    main()
