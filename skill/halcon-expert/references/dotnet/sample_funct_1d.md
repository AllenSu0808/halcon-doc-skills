# SampleFunct1d (Operator)

## Name

`SampleFunct1d` — Sample a function equidistantly in an interval.

## Signature

`static void HOperatorSet.SampleFunct1d(HTuple function, HTuple XMin, HTuple XMax, HTuple XDist, HTuple border, out HTuple sampledFunction)`

`HFunction1D HFunction1D.SampleFunct1d(HTuple XMin, HTuple XMax, HTuple XDist, string border)`

`HFunction1D HFunction1D.SampleFunct1d(double XMin, double XMax, double XDist, string border)`

## Description

`SampleFunct1d` samples the input function *`function`*
in the interval [*`XMin`*,*`XMax`*] at equidistant points
with the distance *`XDist`*. The last point lies in the
interval if *`XMax`*-*`XMin`* is not an integer multiple
of *`XDist`*. To obtain the samples, the input function is
interpolated linearly. The parameter *`border`* determines the
values of the function *`function`* outside of its domain.
For *`border`*=*"zero"* these values are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
and for *`border`*=*"cyclic"* they are continued
cyclically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`XMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum x value of the output function.

**`XMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum x value of the output function.

Restriction:
`XMax > XMin`

**`XDist`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Distance of the samples.

Restriction:
`XDist > 0`

**`border`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Border treatment for the input function.

Default:
"constant"

List of values:
"constant", "cyclic", "mirror", "zero"

**`sampledFunction`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Sampled function.

## Possible Predecessors

`TransformFunct1d`,
`CreateFunct1dArray`,
`CreateFunct1dPairs`

## Module

Foundation
