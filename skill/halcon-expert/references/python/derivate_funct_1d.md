# derivate_funct_1d (Operator)

## Name

`derivate_funct_1d` — Calculate the derivatives of a function.

## Signature

`def derivate_funct_1d(function: Sequence[Union[float, int]], mode: str) -> Sequence[Union[float, int]]`

## Description

`derivate_funct_1d` calculates the derivatives of the function
*`function`* up to the second degree. It uses a finite
difference approximation of order O(h^2). The derivative is also
a function with the same sampling points as *`function`*. With
the parameter *`mode`*, *"first"* and *"second"*
derivatives can be selected.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function

**`mode`** (input_control)  string `→` str

Type of derivative

Default:
"first"

List of values:
"first", "second"

**`derivative`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Derivative of the input function

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`smooth_funct_1d_gauss`,
`smooth_funct_1d_mean`

## Module

Foundation
