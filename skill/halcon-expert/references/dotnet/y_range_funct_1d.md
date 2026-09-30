# YRangeFunct1d (Operator)

## Name

`YRangeFunct1d` — Smallest and largest y value of the function.

## Signature

`static void HOperatorSet.YRangeFunct1d(HTuple function, out HTuple YMin, out HTuple YMax)`

`void HFunction1D.YRangeFunct1d(out double YMin, out double YMax)`

## Description

`YRangeFunct1d` calculates the smallest and
the largest y value of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`YMin`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Smallest y value.

**`YMax`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Largest y value.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
