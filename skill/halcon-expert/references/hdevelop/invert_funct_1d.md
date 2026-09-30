# invert_funct_1d (Operator)

## Name

`invert_funct_1d` — Calculate the inverse of a function.

## Signature

`invert_funct_1d( : : Function : InverseFunction)`

## Description

`invert_funct_1d` calculates the inverse function of the input
function *`Function`* and returns it in
*`InverseFunction`*. The function *`Function`* must be
monotonic. If this is not the case an error message is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`InverseFunction`** (output_control)  function_1d `→`  (real / integer)

Inverse of the input function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
