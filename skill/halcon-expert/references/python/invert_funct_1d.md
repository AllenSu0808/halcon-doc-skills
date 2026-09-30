# invert_funct_1d (Operator)

## Name

`invert_funct_1d` — Calculate the inverse of a function.

## Signature

`def invert_funct_1d(function: Sequence[Union[float, int]]) -> Sequence[Union[float, int]]`

## Description

`invert_funct_1d` calculates the inverse function of the input
function *`function`* and returns it in
*`inverse_function`*. The function *`function`* must be
monotonic. If this is not the case an error message is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`inverse_function`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Inverse of the input function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
