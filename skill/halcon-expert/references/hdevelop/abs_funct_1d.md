# abs_funct_1d (Operator)

## Name

`abs_funct_1d` — Absolute value of the y values.

## Signature

`abs_funct_1d( : : Function : FunctionAbsolute)`

## Description

`abs_funct_1d` calculates the absolute values of all y values
of *`Function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`FunctionAbsolute`** (output_control)  function_1d `→`  (real / integer)

Function with the absolute values of the y values.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
