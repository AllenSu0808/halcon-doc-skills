# GenCoocMatrix (Operator)

## Name

`GenCoocMatrix` — Calculate the co-occurrence matrix of a region in an image.

## Signature

`static void HOperatorSet.GenCoocMatrix(HObject regions, HObject image, out HObject matrix, HTuple ldGray, HTuple direction)`

`HImage HImage.GenCoocMatrix(HRegion regions, int ldGray, int direction)`

`HImage HRegion.GenCoocMatrix(HImage image, int ldGray, int direction)`

## Description

The operator `GenCoocMatrix` determines from the input
regions how often the gray values i and j are located next to
each other in a certain direction (*0*, *45*,
*90*, *135* degrees), stores this number in the
co-occurrence matrix at the locations (i,j) and (j,i) (the
matrix is symmetrical), and finally scales the matrix with the
number of entries. *`ldGray`* indicates the number of gray
values to be distinguished (namely $2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

*Example:* Input image with gray values (scaled with *`ldGray`*=2)
![figure](../assets/3b6aa31d123dd75d.svg)

Co-occurrence matrix (not scaled):

![figure](../assets/0dee97f26d08776d.svg)

## Attention

Note that the operator `GenCoocMatrix` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be checked.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Image providing the gray values.

**`matrix`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Co-occurrence matrix (matrices).

**`ldGray`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of gray values to be distinguished
($2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

Default:
6

List of values:
1, 2, 3, 4, 5, 6, 7, 8

Value range:
`ldGray` (lin)

Minimum increment:
1

Recommended increment:
1

**`direction`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Direction of neighbor relation.

Default:
0

List of values:
0, 45, 90, 135

## Result

The operator `GenCoocMatrix` returns the value 2 (
H_MSG_TRUE)
if
an image with defined gray values is entered and the parameters are
correct. The behavior in case of empty input (no input images
available) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`DrawRegion`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`Threshold`,
`ErosionCircle`,
`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`SubImage`

## Alternatives

`CoocFeatureImage`

## See also

`CoocFeatureMatrix`

## Module

Foundation
