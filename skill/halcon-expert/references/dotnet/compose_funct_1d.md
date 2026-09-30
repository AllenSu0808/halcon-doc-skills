# ComposeFunct1d (Operator)

## Name

`ComposeFunct1d` — Compose two functions.

## Signature

`static void HOperatorSet.ComposeFunct1d(HTuple function1, HTuple function2, HTuple border, out HTuple composedFunction)`

`HFunction1D HFunction1D.ComposeFunct1d(HFunction1D function2, string border)`

## Description

`ComposeFunct1d` composes two functions, i.e., calculates
ComposedFunction(x) = Function2(Function1(x)).
*`composedFunction`* has the same domain (x-range) as
*`function1`*. If the range (y value range) of
*`function1`* is larger than the domain of *`function2`*,
the parameter *`border`* determines the border treatment of
*`function2`*. For *`border`*=*"zero"* values
outside the domain of *`function2`* are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
and for *`border`*=*"cyclic"* they are continued
cyclically. To obtain y values, *`function2`* is interpolated
linearly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function1`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function 1.

**`function2`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function 2.

**`border`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Border treatment for the input functions.

Default:
"constant"

List of values:
"constant", "cyclic", "mirror", "zero"

**`composedFunction`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Composed function.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
