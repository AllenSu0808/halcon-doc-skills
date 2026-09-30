# y_range_funct_1d (Operator)

## Name

`y_range_funct_1d` — Smallest and largest y value of the function.

## Signature

`def y_range_funct_1d(function: Sequence[Union[float, int]]) -> Tuple[float, float]`

## Description

`y_range_funct_1d` calculates the smallest and
the largest y value of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`ymin`** (output_control)  number `→` float

Smallest y value.

**`ymax`** (output_control)  number `→` float

Largest y value.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
