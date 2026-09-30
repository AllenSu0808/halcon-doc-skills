# GetYValueFunct1d (Operator)

## Name

`GetYValueFunct1d` — Return the value of a function at an arbitrary position.

## Signature

`static void HOperatorSet.GetYValueFunct1d(HTuple function, HTuple x, HTuple border, out HTuple y)`

`HTuple HFunction1D.GetYValueFunct1d(HTuple x, string border)`

`double HFunction1D.GetYValueFunct1d(double x, string border)`

## Description

`GetYValueFunct1d` returns the y value of the function
*`function`* at the x coordinates specified by *`x`*.
To obtain the y values, the input function is
interpolated linearly. The parameter *`border`* determines the
values of the function *`function`* outside of its domain.
For *`border`*=*"zero"* these values are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
for *`border`*=*"cyclic"* they are continued
cyclically, and for *`border`*=*"error"* an
exception is raised.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`x`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate at which the function should be
evaluated.

**`border`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Border treatment for the input function.

Default:
"constant"

List of values:
"constant", "cyclic", "error", "mirror", "zero"

**`y`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Y value at the given x value.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
