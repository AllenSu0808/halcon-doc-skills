# x_range_funct_1d (Operator)

## Name

`x_range_funct_1d` — Smallest and largest x value of the function.

## Signature

`def x_range_funct_1d(function: Sequence[Union[float, int]]) -> Tuple[float, float]`

## Description

`x_range_funct_1d` calculates the smallest and
the largest x value of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`xmin`** (output_control)  number `→` float

Smallest x value.

**`xmax`** (output_control)  number `→` float

Largest x value.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
