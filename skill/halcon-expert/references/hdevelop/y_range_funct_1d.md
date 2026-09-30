# y_range_funct_1d (Operator)

## Name

`y_range_funct_1d` — Smallest and largest y value of the function.

## Signature

`y_range_funct_1d( : : Function : YMin, YMax)`

## Description

`y_range_funct_1d` calculates the smallest and
the largest y value of *`Function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`YMin`** (output_control)  number `→`  (real)

Smallest y value.

**`YMax`** (output_control)  number `→`  (real)

Largest y value.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
