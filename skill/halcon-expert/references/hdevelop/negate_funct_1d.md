# negate_funct_1d (Operator)

## Name

`negate_funct_1d` — Negation of the y values.

## Signature

`negate_funct_1d( : : Function : FunctionInverted)`

## Description

`negate_funct_1d` negates all y values
of *`Function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`FunctionInverted`** (output_control)  function_1d `→`  (real / integer)

Function with the negated y values.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
