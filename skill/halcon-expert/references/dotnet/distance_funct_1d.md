# DistanceFunct1d (Operator)

## Name

`DistanceFunct1d` — Compute the distance of two functions.

## Warning

**`DistanceFunct1d` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.DistanceFunct1d(HTuple function1, HTuple function2, HTuple mode, HTuple sigma, out HTuple distance)`

`HTuple HFunction1D.DistanceFunct1d(HFunction1D function2, HTuple mode, HTuple sigma)`

`HTuple HFunction1D.DistanceFunct1d(HFunction1D function2, string mode, double sigma)`

## Description

`DistanceFunct1d` calculates the distance of two functions.
The two functions may differ in length.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function1`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function 1.

**`function2`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function 2.

**`mode`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Modes of invariants.

Default:
"length"

List of values:
"length", "mean"

**`sigma`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Variance of the optional smoothing with a
Gaussian filter.

Default:
0.0

Suggested values:
0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0

**`distance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double* / int / long)

Distance of the functions.

## Module

Foundation
