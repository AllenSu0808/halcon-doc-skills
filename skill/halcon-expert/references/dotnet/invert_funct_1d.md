# InvertFunct1d (Operator)

## Name

`InvertFunct1d` — Calculate the inverse of a function.

## Signature

`static void HOperatorSet.InvertFunct1d(HTuple function, out HTuple inverseFunction)`

`HFunction1D HFunction1D.InvertFunct1d()`

## Description

`InvertFunct1d` calculates the inverse function of the input
function *`function`* and returns it in
*`inverseFunction`*. The function *`function`* must be
monotonic. If this is not the case an error message is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`inverseFunction`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Inverse of the input function.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
