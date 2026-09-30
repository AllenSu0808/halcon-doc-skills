# num_points_funct_1d (Operator)

## Name

`num_points_funct_1d` — Number of control points of the function.

## Signature

`def num_points_funct_1d(function: Sequence[Union[float, int]]) -> int`

## Description

`num_points_funct_1d` calculates the number of control points
of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`length`** (output_control)  integer `→` int

Number of control points.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
