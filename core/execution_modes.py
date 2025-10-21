"""
Execution modes for the cinema application.
Handles deployment mode with error recovery and development mode.
"""

from time import sleep
from core.application import run_main_application_loop
from core.error_handler import handle_application_error, show_restart_message


def run_deployment_mode() -> None:
    """
    Runs the application in deployment mode with error handling and auto-restart.
    Continues running until user explicitly chooses to shut down.
    """
    print("modo deploy")
    sleep(2)
    
    shut_down = False
    
    while not shut_down:
        try:
            run_main_application_loop()
            
        except Exception as error:
            shut_down = handle_application_error(error)
            
        finally:
            if not shut_down:
                show_restart_message()


def run_development_mode() -> None:
    """
    Runs the application in development mode without error handling.
    Allows errors to propagate for debugging purposes.
    
    Note: In a full development setup, you would use the traceback
    library to show detailed error information including line numbers
    and file locations.
    """
    run_main_application_loop()


def determine_and_run_application_mode(args: list[str]) -> None:
    """
    Determines the application mode based on command line arguments
    and runs the appropriate mode.
    """
    if args[-1] == "deploy":
        run_deployment_mode()
    else:
        run_development_mode()