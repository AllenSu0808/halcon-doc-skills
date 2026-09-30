# cooc_feature_image (Operator)

## Name

`cooc_feature_image` — Calculate a co-occurrence matrix and derive gray value features thereof.

## Signature

`def cooc_feature_image(regions: HObject, image: HObject, ld_gray: int, direction: Union[int, str]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def cooc_feature_image_s(regions: HObject, image: HObject, ld_gray: int, direction: Union[int, str]) -> Tuple[float, float, float, float]`

## Description

The call of `cooc_feature_image` corresponds to the consecutive
execution of the operators [`gen_cooc_matrix`](gen_cooc_matrix.md) and
[`cooc_feature_matrix`](cooc_feature_matrix.md). If several direction matrices of the
co-occurrence matrix are to be evaluated consecutively, it is more
efficient to generate the matrix via [`gen_cooc_matrix`](gen_cooc_matrix.md) and
then call the operator [`cooc_feature_matrix`](cooc_feature_matrix.md) for the resulting
matrix. The parameter *`direction`* transfers the direction
of the neighborhood in angle or *"mean"*. In the case of
*"mean"* the mean value is calculated in all four
directions.

## Attention

Note that the operator `cooc_feature_image` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region to be examined.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Corresponding gray values.

**`ld_gray`** (input_control)  integer `→` int

Number of gray values to be distinguished
($2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

Default:
6

List of values:
1, 2, 3, 4, 5, 6, 7, 8

**`direction`** (input_control)  integer `→` Union[int, str]

Direction in which the matrix is to be calculated.

Default:
0

List of values:
0, 45, 90, 135, "mean"

**`energy`** (output_control)  real(-array) `→` Sequence[float]

Gray value energy.

**`correlation`** (output_control)  real(-array) `→` Sequence[float]

Correlation of gray values.

**`homogeneity`** (output_control)  real(-array) `→` Sequence[float]

Local homogeneity of gray values.

**`contrast`** (output_control)  real(-array) `→` Sequence[float]

Gray value contrast.

## Result

The operator `cooc_feature_image` returns the value 2 (
H_MSG_TRUE)
if an
image with defined gray values (byte) is entered and the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`, the behavior
in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`. If
necessary an exception is raised.

## Possible Predecessors

`gen_cooc_matrix`

## Alternatives

`cooc_feature_matrix`

## See also

`intensity`,
`min_max_gray`,
`entropy_gray`,
`select_gray`

## Module

Foundation
