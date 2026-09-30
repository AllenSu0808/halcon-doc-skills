# funct_1d_to_pairs (Operator)

## Name

`funct_1d_to_pairs` — Access to the x/y values of a function.

## Signature

`def funct_1d_to_pairs(function: Sequence[Union[float, int]]) -> Tuple[Sequence[Union[int, float]], Sequence[Union[int, float]]]`

## Description

`funct_1d_to_pairs` splits the input function *`function`*
into tuples for the x and y values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`xvalues`** (output_control)  number-array `→` Sequence[Union[int, float]]

X values of the function.

**`yvalues`** (output_control)  number-array `→` Sequence[Union[int, float]]

Y values of the function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
