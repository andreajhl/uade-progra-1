"""
Core application logic - Cinema management application flow.
Contains the main business flow without error handling or mode concerns.
"""

from interface.controllers.init_interface import init_interface


def run_main_application_loop() -> None:
    """
    Main application loop.
    Starts the cinema management system with the new architecture.
    """
    init_interface()