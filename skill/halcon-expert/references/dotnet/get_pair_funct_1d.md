# GetPairFunct1d (Operator)

## Name

`GetPairFunct1d` — Access a function value using the index of the control points.

## Signature

`static void HOperatorSet.GetPairFunct1d(HTuple function, HTuple index, out HTuple x, out HTuple y)`

`void HFunction1D.GetPairFunct1d(HTuple index, out HTuple x, out HTuple y)`

`void HFunction1D.GetPairFunct1d(int index, out double x, out double y)`

## Description

`GetPairFunct1d` accesses a function value
of *`function`*. This is done by specifying the
index of one or more control points of the function.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the control points.

**`x`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

X value at the given control points.

**`y`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Y value at the given control points.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
