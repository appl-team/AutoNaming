import re
from argparse import ArgumentParser, Namespace
from datetime import datetime
from typing import Union

import appl
from appl import gen, ppl
from appl.compositor import NumberedList, Tagged

appl.init()


@ppl(docstring_as="system")
def name_this_exp(
    parser: ArgumentParser,
    args: Namespace,
    add_timestamp: Union[bool, str] = False,
) -> str:
    """You are an expert at naming machine learning experiments. You should:
    1. Generate a descriptive and concise name in snake_case that captures the key parameters
    2. Keep names under 100 characters
    3. Include the most important parameters that distinguish this experiment
    4. Use standard abbreviations where appropriate (e.g. lr for learning_rate)
    5. Order parameters from most to least important"""

    # Get parser information
    with Tagged("parser_info"):
        "Arguments defined in the parser:"
        with NumberedList():
            for action in parser._actions:
                if action.dest != "help":
                    (
                        f"Name: {action.dest}, "
                        f"Type: {action.type.__name__ if action.type else 'str'}, "
                        f"Default: {action.default}, "
                        f"Help: {action.help}"
                    )

    # Get actual argument values
    with Tagged("argument_values"):
        "Actual argument values passed:"
        args_dict = vars(args)
        for key, value in args_dict.items():
            if key != "help":
                f"{key}: {value}"

    "Generate a informative snake_case name for this experiment that captures the key parameters."
    "Wrap the proposed name with <name>...</name>, for example: <name>this_is_a_good_name</name>."
    "You do not need to explain the reason, just give the name."
    response = str(gen(stream=True))
    name = re.search(r"<name>(.*)</name>", response).group(1)
    if add_timestamp:
        if isinstance(add_timestamp, str):
            name = f"{name}__{add_timestamp}"
        else:
            name = f"{name}__{datetime.now().strftime('%Y_%m_%d__%H_%M_%S')}"
    return name
