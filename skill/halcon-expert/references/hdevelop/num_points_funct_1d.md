# num_points_funct_1d (Operator)

## Name

`num_points_funct_1d` — Number of control points of the function.

## Signature

`num_points_funct_1d( : : Function : Length)`

## Description

`num_points_funct_1d` calculates the number of control points
of *`Function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`Length`** (output_control)  integer `→`  (integer)

Number of control points.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
