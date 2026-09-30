# ZeroCrossingsFunct1d (Operator)

## Name

`ZeroCrossingsFunct1d` — Calculate the zero crossings of a function.

## Signature

`static void HOperatorSet.ZeroCrossingsFunct1d(HTuple function, out HTuple zeroCrossings)`

`HTuple HFunction1D.ZeroCrossingsFunct1d()`

## Description

`ZeroCrossingsFunct1d` calculates the zero crossings
*`zeroCrossings`* of the function *`function`*. A linear
interpolation is applied to the function between its sampling points
so that the coordinates of the zero crossing can be calculated
exactly. If an entire line segment between two sampling points has
a value of *0*, only the end points of its supporting
interval are returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function

**`zeroCrossings`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Zero crossings of the input function

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`,
`SmoothFunct1dGauss`,
`SmoothFunct1dMean`

## Module

Foundation
