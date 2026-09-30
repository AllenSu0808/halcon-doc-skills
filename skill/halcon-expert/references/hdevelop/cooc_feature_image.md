# cooc_feature_image (Operator)

## Name

`cooc_feature_image` — Calculate a co-occurrence matrix and derive gray value features thereof.

## Signature

`cooc_feature_image(Regions, Image : : LdGray, Direction : Energy, Correlation, Homogeneity, Contrast)`

## Description

The call of `cooc_feature_image` corresponds to the consecutive
execution of the operators [`gen_cooc_matrix`](gen_cooc_matrix.md) and
[`cooc_feature_matrix`](cooc_feature_matrix.md). If several direction matrices of the
co-occurrence matrix are to be evaluated consecutively, it is more
efficient to generate the matrix via [`gen_cooc_matrix`](gen_cooc_matrix.md) and
then call the operator [`cooc_feature_matrix`](cooc_feature_matrix.md) for the resulting
matrix. The parameter *`Direction`* transfers the direction
of the neighborhood in angle or *'mean'*. In the case of
*'mean'* the mean value is calculated in all four
directions.

## Attention

Note that the operator `cooc_feature_image` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Corresponding gray values.

**`LdGray`** (input_control)  integer `→`  (integer)

Number of gray values to be distinguished
($2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

Default:
6

List of values:
1, 2, 3, 4, 5, 6, 7, 8

**`Direction`** (input_control)  integer `→`  (integer / string)

Direction in which the matrix is to be calculated.

Default:
0

List of values:
0, 45, 90, 135, 'mean'

**`Energy`** (output_control)  real(-array) `→`  (real)

Gray value energy.

**`Correlation`** (output_control)  real(-array) `→`  (real)

Correlation of gray values.

**`Homogeneity`** (output_control)  real(-array) `→`  (real)

Local homogeneity of gray values.

**`Contrast`** (output_control)  real(-array) `→`  (real)

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
