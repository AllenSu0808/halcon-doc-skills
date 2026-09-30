# XRangeFunct1d (Operator)

## Name

`XRangeFunct1d` — Smallest and largest x value of the function.

## Signature

`static void HOperatorSet.XRangeFunct1d(HTuple function, out HTuple XMin, out HTuple XMax)`

`void HFunction1D.XRangeFunct1d(out double XMin, out double XMax)`

## Description

`XRangeFunct1d` calculates the smallest and
the largest x value of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`XMin`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Smallest x value.

**`XMax`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Largest x value.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
