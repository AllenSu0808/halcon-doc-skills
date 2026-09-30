# get_pair_funct_1d (Operator)

## Name

`get_pair_funct_1d` — Access a function value using the index of the control points.

## Signature

`def get_pair_funct_1d(function: Sequence[Union[float, int]], index: MaybeSequence[int]) -> Tuple[Sequence[float], Sequence[float]]`

`def get_pair_funct_1d_s(function: Sequence[Union[float, int]], index: MaybeSequence[int]) -> Tuple[float, float]`

## Description

`get_pair_funct_1d` accesses a function value
of *`function`*. This is done by specifying the
index of one or more control points of the function.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index of the control points.

**`x`** (output_control)  number(-array) `→` Sequence[float]

X value at the given control points.

**`y`** (output_control)  number(-array) `→` Sequence[float]

Y value at the given control points.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
