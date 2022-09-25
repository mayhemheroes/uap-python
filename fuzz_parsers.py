#!/usr/bin/python3
import atheris
atheris.enabled_hooks.add("RegEx")

with atheris.instrument_imports():
    import re
    import sys
    from ua_parser import user_agent_parser


@atheris.instrument_func
def TestOneInput(data):
    if len(data) < 4096:
        pass
    fdp = atheris.FuzzedDataProvider(data)
    user_agent = fdp.ConsumeString(4096)

    # Library only claims to raise TypeError, if the input isn't a string- which is handled. Any others are a problem
    user_agent_parser.Parse(user_agent)


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
