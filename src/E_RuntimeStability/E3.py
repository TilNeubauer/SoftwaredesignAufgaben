import os
import logging

# 1) Log-Level aus Environment lesen (z.B. myloglevel=DEBUG)
level_str = os.getenv("myloglevel", "DEBUG").upper()  # Default DEBUG (wie im Snippet)

# 2) String -> logging-Level mappen, Fallback auf Default wenn ungültig
level = getattr(logging, level_str, logging.DEBUG)

logging.basicConfig(
    format="%(asctime)s:%(levelname)s: %(message)s",
    level=level
)

numberlist = [-2, -1, 0, 1, 2, "a", 1 / 4]

for number in numberlist:
    try:
        logging.debug(f"Working on number {number}")
        inverse = 1.0 / number
    except ZeroDivisionError as e:
        logging.error(f"Tried to divide by zero, error is {e}")
    except TypeError:
        logging.warning("The list does not only contain numbers")


'''
starten default: in Powerschell
pdm run src/E_RuntimeStability/E3.py

DEBUG(wie default): in Powerschell
    $env:myloglevel="DEBUG"
    pdm run src/E_RuntimeStability/E3.py


nur WARNING: in Powerschell
    $env:myloglevel="WARNING"
    pdm run src/E_RuntimeStability/E3.py

nur ERROR: in Powerschell
    $env:myloglevel="ERROR"
    python .\deinscript.py
'''
