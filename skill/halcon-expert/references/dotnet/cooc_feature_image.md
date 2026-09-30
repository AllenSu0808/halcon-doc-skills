# CoocFeatureImage (Operator)

## Name

`CoocFeatureImage` — Calculate a co-occurrence matrix and derive gray value features thereof.

## Signature

`static void HOperatorSet.CoocFeatureImage(HObject regions, HObject image, HTuple ldGray, HTuple direction, out HTuple energy, out HTuple correlation, out HTuple homogeneity, out HTuple contrast)`

`HTuple HImage.CoocFeatureImage(HRegion regions, int ldGray, HTuple direction, out HTuple correlation, out HTuple homogeneity, out HTuple contrast)`

`double HImage.CoocFeatureImage(HRegion regions, int ldGray, int direction, out double correlation, out double homogeneity, out double contrast)`

`HTuple HRegion.CoocFeatureImage(HImage image, int ldGray, HTuple direction, out HTuple correlation, out HTuple homogeneity, out HTuple contrast)`

`double HRegion.CoocFeatureImage(HImage image, int ldGray, int direction, out double correlation, out double homogeneity, out double contrast)`

## Description

The call of `CoocFeatureImage` corresponds to the consecutive
execution of the operators [`GenCoocMatrix`](gen_cooc_matrix.md) and
[`CoocFeatureMatrix`](cooc_feature_matrix.md). If several direction matrices of the
co-occurrence matrix are to be evaluated consecutively, it is more
efficient to generate the matrix via [`GenCoocMatrix`](gen_cooc_matrix.md) and
then call the operator [`CoocFeatureMatrix`](cooc_feature_matrix.md) for the resulting
matrix. The parameter *`direction`* transfers the direction
of the neighborhood in angle or *"mean"*. In the case of
*"mean"* the mean value is calculated in all four
directions.

## Attention

Note that the operator `CoocFeatureImage` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be examined.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Corresponding gray values.

**`ldGray`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of gray values to be distinguished
($2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

Default:
6

List of values:
1, 2, 3, 4, 5, 6, 7, 8

**`direction`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Direction in which the matrix is to be calculated.

Default:
0

List of values:
0, 45, 90, 135, "mean"

**`energy`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Gray value energy.

**`correlation`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Correlation of gray values.

**`homogeneity`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Local homogeneity of gray values.

**`contrast`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Gray value contrast.

## Result

The operator `CoocFeatureImage` returns the value 2 (
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

`GenCoocMatrix`

## Alternatives

`CoocFeatureMatrix`

## See also

`Intensity`,
`MinMaxGray`,
`EntropyGray`,
`SelectGray`

## Module

Foundation
