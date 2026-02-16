from typing import Annotated
from pydantic import Field, ValidationError, validate_call

@validate_call
def testfun(a: Annotated[int, Field(gt=0)], b: Annotated[int, Field(gt=0)], c: Annotated[int, Field(gt=0)]) -> int:
    return a, b, c



print(testfun(1, 1, 1)) 
print(testfun(1, -1, 1))  # ok