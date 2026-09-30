# get_pair_funct_1d (Operator)

## Name

`get_pair_funct_1d` — Access a function value using the index of the control points.

## Signature

`get_pair_funct_1d( : : Function, Index : X, Y)`

## Description

`get_pair_funct_1d` accesses a function value
of *`Function`*. This is done by specifying the
index of one or more control points of the function.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`Index`** (input_control)  integer(-array) `→`  (integer)

Index of the control points.

**`X`** (output_control)  number(-array) `→`  (real)

X value at the given control points.

**`Y`** (output_control)  number(-array) `→`  (real)

Y value at the given control points.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
