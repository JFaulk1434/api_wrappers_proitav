"""Python wrapper for SW0401-N081-000 RS232 Switcher 4x1 with ARC Extraction"""


class SW0401_N081_API:
    """Python API Wrapper for SW0401-N081-000"""

    def set_input(input: int):
        """Switch Input"""
        if input == 1:
            str = "in1"
        elif input == 2:
            str = "in2"
        elif input == 3:
            str = "in3"
        else:
            str = "in4"

        return f"SET SW {str} out"
