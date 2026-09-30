# derivate_funct_1d (Operator)

## Name

`derivate_funct_1d` — Calculate the derivatives of a function.

## Signature

`derivate_funct_1d( : : Function, Mode : Derivative)`

## Description

`derivate_funct_1d` calculates the derivatives of the function
*`Function`* up to the second degree. It uses a finite
difference approximation of order O(h^2). The derivative is also
a function with the same sampling points as *`Function`*. With
the parameter *`Mode`*, *'first'* and *'second'*
derivatives can be selected.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function

**`Mode`** (input_control)  string `→`  (string)

Type of derivative

Default:
'first'

List of values:
'first', 'second'

**`Derivative`** (output_control)  function_1d `→`  (real / integer)

Derivative of the input function

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`smooth_funct_1d_gauss`,
`smooth_funct_1d_mean`

## Module

Foundation
