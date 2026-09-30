# NumPointsFunct1d (Operator)

## Name

`NumPointsFunct1d` — Number of control points of the function.

## Signature

`static void HOperatorSet.NumPointsFunct1d(HTuple function, out HTuple length)`

`int HFunction1D.NumPointsFunct1d()`

## Description

`NumPointsFunct1d` calculates the number of control points
of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`length`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of control points.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
