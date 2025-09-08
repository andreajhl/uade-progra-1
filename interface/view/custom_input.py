from typing import Type, Callable, Any, Union


def custom_input(
    input_message="Ingrese un valor: ",
    input_type: Type = str,
    error_message="Valor incorrecto",
    validator: Callable[
        [Any], Union[tuple[Exception, None], tuple[None, Any]]
    ] = lambda x: (None, x),
    validator_params: dict = {},
) -> Any:
    while True:
        user_input = input(input_message)

        if input_type == int or input_type == float:

            if not user_input.isnumeric():
                print(error_message)
                continue

            user_input = input_type(user_input)
            (validation_error_message, user_input) = validator(
                user_input, **validator_params
            )

            if validation_error_message != None:
                print(validation_error_message)
                continue

            return user_input

        if input_type == str:

            user_input = input_type(user_input)
            (validation_error_message, user_input) = validator(
                user_input, **validator_params
            )

            if validation_error_message != None:
                print(validation_error_message)
                continue

            return user_input
