# ScaleYFunct1d (Operator)

## Name

`ScaleYFunct1d` — Multiplication and addition of the y values.

## Signature

`static void HOperatorSet.ScaleYFunct1d(HTuple function, HTuple mult, HTuple add, out HTuple functionScaled)`

`HFunction1D HFunction1D.ScaleYFunct1d(double mult, double add)`

## Description

`ScaleYFunct1d` multiplies and adds the y values
of *`function`* with the parameters
*`mult`* and *`add`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`mult`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Factor for scaling of the y values.

Default:
2.0

Suggested values:
0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0

**`add`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Constant which is added to the y values.

Default:
0.0

Suggested values:
-10.0, -5.0, 1.0, 0.0, 5.0, 10.0

**`functionScaled`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Transformed function.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
