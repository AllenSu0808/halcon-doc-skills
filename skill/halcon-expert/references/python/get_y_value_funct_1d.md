# get_y_value_funct_1d (Operator)

## Name

`get_y_value_funct_1d` — Return the value of a function at an arbitrary position.

## Signature

`def get_y_value_funct_1d(function: Sequence[Union[float, int]], x: MaybeSequence[float], border: str) -> Sequence[float]`

`def get_y_value_funct_1d_s(function: Sequence[Union[float, int]], x: MaybeSequence[float], border: str) -> float`

## Description

`get_y_value_funct_1d` returns the y value of the function
*`function`* at the x coordinates specified by *`x`*.
To obtain the y values, the input function is
interpolated linearly. The parameter *`border`* determines the
values of the function *`function`* outside of its domain.
For *`border`*=*"zero"* these values are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
for *`border`*=*"cyclic"* they are continued
cyclically, and for *`border`*=*"error"* an
exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`x`** (input_control)  number(-array) `→` MaybeSequence[float]

X coordinate at which the function should be
evaluated.

**`border`** (input_control)  string `→` str

Border treatment for the input function.

Default:
"constant"

List of values:
"constant", "cyclic", "error", "mirror", "zero"

**`y`** (output_control)  number(-array) `→` Sequence[float]

Y value at the given x value.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
