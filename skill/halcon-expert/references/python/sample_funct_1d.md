# sample_funct_1d (Operator)

## Name

`sample_funct_1d` — Sample a function equidistantly in an interval.

## Signature

`def sample_funct_1d(function: Sequence[Union[float, int]], xmin: Union[float, int], xmax: Union[float, int], xdist: Union[float, int], border: str) -> Sequence[Union[float, int]]`

## Description

`sample_funct_1d` samples the input function *`function`*
in the interval [*`xmin`*,*`xmax`*] at equidistant points
with the distance *`xdist`*. The last point lies in the
interval if *`xmax`*-*`xmin`* is not an integer multiple
of *`xdist`*. To obtain the samples, the input function is
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

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function.

**`xmin`** (input_control)  number `→` Union[float, int]

Minimum x value of the output function.

**`xmax`** (input_control)  number `→` Union[float, int]

Maximum x value of the output function.

Restriction:
`XMax > XMin`

**`xdist`** (input_control)  number `→` Union[float, int]

Distance of the samples.

Restriction:
`XDist > 0`

**`border`** (input_control)  string `→` str

Border treatment for the input function.

Default:
"constant"

List of values:
"constant", "cyclic", "mirror", "zero"

**`sampled_function`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Sampled function.

## Possible Predecessors

`transform_funct_1d`,
`create_funct_1d_array`,
`create_funct_1d_pairs`

## Module

Foundation
