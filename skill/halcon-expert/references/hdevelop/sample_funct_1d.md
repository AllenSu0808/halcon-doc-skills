# sample_funct_1d (Operator)

## Name

`sample_funct_1d` — Sample a function equidistantly in an interval.

## Signature

`sample_funct_1d( : : Function, XMin, XMax, XDist, Border : SampledFunction)`

## Description

`sample_funct_1d` samples the input function *`Function`*
in the interval [*`XMin`*,*`XMax`*] at equidistant points
with the distance *`XDist`*. The last point lies in the
interval if *`XMax`*-*`XMin`* is not an integer multiple
of *`XDist`*. To obtain the samples, the input function is
interpolated linearly. The parameter *`Border`* determines the
values of the function *`Function`* outside of its domain.
For *`Border`*=*'zero'* these values are set to 0, for
*`Border`*=*'constant'* they are set to the
corresponding value at the border, for
*`Border`*=*'mirror'* they are mirrored at the border,
and for *`Border`*=*'cyclic'* they are continued
cyclically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`XMin`** (input_control)  number `→`  (real / integer)

Minimum x value of the output function.

**`XMax`** (input_control)  number `→`  (real / integer)

Maximum x value of the output function.

Restriction:
`XMax > XMin`

**`XDist`** (input_control)  number `→`  (real / integer)

Distance of the samples.

Restriction:
`XDist > 0`

**`Border`** (input_control)  string `→`  (string)

Border treatment for the input function.

Default:
'constant'

List of values:
'constant', 'cyclic', 'mirror', 'zero'

**`SampledFunction`** (output_control)  function_1d `→`  (real / integer)

Sampled function.

## Possible Predecessors

`transform_funct_1d`,
`create_funct_1d_array`,
`create_funct_1d_pairs`

## Module

Foundation
