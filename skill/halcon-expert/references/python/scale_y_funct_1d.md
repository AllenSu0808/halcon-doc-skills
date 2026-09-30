# scale_y_funct_1d (Operator)

## Name

`scale_y_funct_1d` — Multiplication and addition of the y values.

## Signature

`def scale_y_funct_1d(function: Sequence[Union[float, int]], mult: float, add: float) -> Sequence[Union[float, int]]`

## Description

`scale_y_funct_1d` multiplies and adds the y values
of *`function`* with the parameters
*`mult`* and *`add`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`mult`** (input_control)  number `→` float

Factor for scaling of the y values.

Default:
2.0

Suggested values:
0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0

**`add`** (input_control)  number `→` float

Constant which is added to the y values.

Default:
0.0

Suggested values:
-10.0, -5.0, 1.0, 0.0, 5.0, 10.0

**`function_scaled`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Transformed function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
