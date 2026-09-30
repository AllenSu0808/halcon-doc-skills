# funct_1d_to_pairs (Operator)

## Name

`funct_1d_to_pairs` — Access to the x/y values of a function.

## Signature

`funct_1d_to_pairs( : : Function : XValues, YValues)`

## Description

`funct_1d_to_pairs` splits the input function *`Function`*
into tuples for the x and y values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`XValues`** (output_control)  number-array `→`  (real / integer)

X values of the function.

**`YValues`** (output_control)  number-array `→`  (real / integer)

Y values of the function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
