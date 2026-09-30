# abs_funct_1d (Operator)

## Name

`abs_funct_1d` — Absolute value of the y values.

## Signature

`def abs_funct_1d(function: Sequence[Union[float, int]]) -> Sequence[Union[float, int]]`

## Description

`abs_funct_1d` calculates the absolute values of all y values
of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`function_absolute`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Function with the absolute values of the y values.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
