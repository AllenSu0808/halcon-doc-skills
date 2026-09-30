# distance_funct_1d (Operator)

## Name

`distance_funct_1d` — Compute the distance of two functions.

## Warning

**`distance_funct_1d` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def distance_funct_1d(function_1: Sequence[Union[float, int]], function_2: Sequence[Union[float, int]], mode: MaybeSequence[str], sigma: MaybeSequence[float]) -> Sequence[Union[float, int]]`

## Description

`distance_funct_1d` calculates the distance of two functions.
The two functions may differ in length.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function_1`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function 1.

**`function_2`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function 2.

**`mode`** (input_control)  string(-array) `→` MaybeSequence[str]

Modes of invariants.

Default:
"length"

List of values:
"length", "mean"

**`sigma`** (input_control)  number(-array) `→` MaybeSequence[float]

Variance of the optional smoothing with a
Gaussian filter.

Default:
0.0

Suggested values:
0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0

**`distance`** (output_control)  real-array `→` Sequence[Union[float, int]]

Distance of the functions.

## Module

Foundation
