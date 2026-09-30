# scale_y_funct_1d (Operator)

## Name

`scale_y_funct_1d` — Multiplication and addition of the y values.

## Signature

`scale_y_funct_1d( : : Function, Mult, Add : FunctionScaled)`

## Description

`scale_y_funct_1d` multiplies and adds the y values
of *`Function`* with the parameters
*`Mult`* and *`Add`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`Mult`** (input_control)  number `→`  (real)

Factor for scaling of the y values.

Default:
2.0

Suggested values:
0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0

**`Add`** (input_control)  number `→`  (real)

Constant which is added to the y values.

Default:
0.0

Suggested values:
-10.0, -5.0, 1.0, 0.0, 5.0, 10.0

**`FunctionScaled`** (output_control)  function_1d `→`  (real / integer)

Transformed function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
