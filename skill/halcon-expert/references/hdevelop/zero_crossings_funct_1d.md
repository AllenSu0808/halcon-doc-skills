# zero_crossings_funct_1d (Operator)

## Name

`zero_crossings_funct_1d` — Calculate the zero crossings of a function.

## Signature

`zero_crossings_funct_1d( : : Function : ZeroCrossings)`

## Description

`zero_crossings_funct_1d` calculates the zero crossings
*`ZeroCrossings`* of the function *`Function`*. A linear
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

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function

**`ZeroCrossings`** (output_control)  real-array `→`  (real)

Zero crossings of the input function

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`smooth_funct_1d_gauss`,
`smooth_funct_1d_mean`

## Module

Foundation
