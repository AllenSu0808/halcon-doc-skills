# get_y_value_funct_1d (Operator)

## Name

`get_y_value_funct_1d` — Return the value of a function at an arbitrary position.

## Signature

`get_y_value_funct_1d( : : Function, X, Border : Y)`

## Description

`get_y_value_funct_1d` returns the y value of the function
*`Function`* at the x coordinates specified by *`X`*.
To obtain the y values, the input function is
interpolated linearly. The parameter *`Border`* determines the
values of the function *`Function`* outside of its domain.
For *`Border`*=*'zero'* these values are set to 0, for
*`Border`*=*'constant'* they are set to the
corresponding value at the border, for
*`Border`*=*'mirror'* they are mirrored at the border,
for *`Border`*=*'cyclic'* they are continued
cyclically, and for *`Border`*=*'error'* an
exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`X`** (input_control)  number(-array) `→`  (real)

X coordinate at which the function should be
evaluated.

**`Border`** (input_control)  string `→`  (string)

Border treatment for the input function.

Default:
'constant'

List of values:
'constant', 'cyclic', 'error', 'mirror', 'zero'

**`Y`** (output_control)  number(-array) `→`  (real)

Y value at the given x value.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
