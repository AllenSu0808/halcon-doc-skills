# zero_crossings_funct_1d (Operator)

## Name

`zero_crossings_funct_1d` — Calculate the zero crossings of a function.

## Signature

`def zero_crossings_funct_1d(function: Sequence[Union[float, int]]) -> Sequence[float]`

## Description

`zero_crossings_funct_1d` calculates the zero crossings
*`zero_crossings`* of the function *`function`*. A linear
interpolation is applied to the function between its sampling points
so that the coordinates of the zero crossing can be calculated
exactly. If an entire line segment between two sampling points has
a value of *0*, only the end points of its supporting
interval are returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function

**`zero_crossings`** (output_control)  real-array `→` Sequence[float]

Zero crossings of the input function

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`smooth_funct_1d_gauss`,
`smooth_funct_1d_mean`

## Module

Foundation
