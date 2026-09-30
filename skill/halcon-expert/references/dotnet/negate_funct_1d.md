# NegateFunct1d (Operator)

## Name

`NegateFunct1d` — Negation of the y values.

## Signature

`static void HOperatorSet.NegateFunct1d(HTuple function, out HTuple functionInverted)`

`HFunction1D HFunction1D.NegateFunct1d()`

## Description

`NegateFunct1d` negates all y values
of *`function`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`functionInverted`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Function with the negated y values.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
