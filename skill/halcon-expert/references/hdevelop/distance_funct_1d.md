# distance_funct_1d (Operator)

## Name

`distance_funct_1d` — Compute the distance of two functions.

## Warning

**`distance_funct_1d` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`distance_funct_1d( : : Function1, Function2, Mode, Sigma : Distance)`

## Description

`distance_funct_1d` calculates the distance of two functions.
The two functions may differ in length.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function1`** (input_control)  function_1d `→`  (real / integer)

Input function 1.

**`Function2`** (input_control)  function_1d `→`  (real / integer)

Input function 2.

**`Mode`** (input_control)  string(-array) `→`  (string)

Modes of invariants.

Default:
'length'

List of values:
'length', 'mean'

**`Sigma`** (input_control)  number(-array) `→`  (real)

Variance of the optional smoothing with a
Gaussian filter.

Default:
0.0

Suggested values:
0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0

**`Distance`** (output_control)  real-array `→`  (real / integer)

Distance of the functions.

## Module

Foundation
