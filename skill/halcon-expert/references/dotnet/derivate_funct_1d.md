# DerivateFunct1d (Operator)

## Name

`DerivateFunct1d` — Calculate the derivatives of a function.

## Signature

`static void HOperatorSet.DerivateFunct1d(HTuple function, HTuple mode, out HTuple derivative)`

`HFunction1D HFunction1D.DerivateFunct1d(string mode)`

## Description

`DerivateFunct1d` calculates the derivatives of the function
*`function`* up to the second degree. It uses a finite
difference approximation of order O(h^2). The derivative is also
a function with the same sampling points as *`function`*. With
the parameter *`mode`*, *"first"* and *"second"*
derivatives can be selected.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of derivative

Default:
"first"

List of values:
"first", "second"

**`derivative`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Derivative of the input function

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`,
`SmoothFunct1dGauss`,
`SmoothFunct1dMean`

## Module

Foundation
