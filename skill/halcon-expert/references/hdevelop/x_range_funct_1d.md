# x_range_funct_1d (Operator)

## Name

`x_range_funct_1d` — Smallest and largest x value of the function.

## Signature

`x_range_funct_1d( : : Function : XMin, XMax)`

## Description

`x_range_funct_1d` calculates the smallest and
the largest x value of *`Function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`XMin`** (output_control)  number `→`  (real)

Smallest x value.

**`XMax`** (output_control)  number `→`  (real)

Largest x value.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
