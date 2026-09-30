# AbsFunct1d (Operator)

## Name

`AbsFunct1d` — Absolute value of the y values.

## Signature

`static void HOperatorSet.AbsFunct1d(HTuple function, out HTuple functionAbsolute)`

`HFunction1D HFunction1D.AbsFunct1d()`

## Description

`AbsFunct1d` calculates the absolute values of all y values
of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`functionAbsolute`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Function with the absolute values of the y values.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
