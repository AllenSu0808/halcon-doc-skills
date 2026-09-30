# gen_cooc_matrix (Operator)

## Name

`gen_cooc_matrix` — Calculate the co-occurrence matrix of a region in an image.

## Signature

`gen_cooc_matrix(Regions, Image : Matrix : LdGray, Direction : )`

## Description

The operator `gen_cooc_matrix` determines from the input
regions how often the gray values i and j are located next to
each other in a certain direction (*0*, *45*,
*90*, *135* degrees), stores this number in the
co-occurrence matrix at the locations (i,j) and (j,i) (the
matrix is symmetrical), and finally scales the matrix with the
number of entries. *`LdGray`* indicates the number of gray
values to be distinguished (namely $2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

*Example:* Input image with gray values (scaled with *`LdGray`*=2)
![figure](../assets/3b6aa31d123dd75d.svg)

Co-occurrence matrix (not scaled):

![figure](../assets/0dee97f26d08776d.svg)

## Attention

Note that the operator `gen_cooc_matrix` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Region to be checked.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Image providing the gray values.

**`Matrix`** (output_object)  image(-array) `→` object (real)

Co-occurrence matrix (matrices).

**`LdGray`** (input_control)  integer `→`  (integer)

Number of gray values to be distinguished
($2LdGray$ ![figure](../assets/f6a5edf72cef7b35.svg)).

Default:
6

List of values:
1, 2, 3, 4, 5, 6, 7, 8

Value range:
`LdGray` (lin)

Minimum increment:
1

Recommended increment:
1

**`Direction`** (input_control)  integer `→`  (integer)

Direction of neighbor relation.

Default:
0

List of values:
0, 45, 90, 135

## Result

The operator `gen_cooc_matrix` returns the value 2 (
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

`draw_region`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`threshold`,
`erosion_circle`,
`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`sub_image`

## Alternatives

`cooc_feature_image`

## See also

`cooc_feature_matrix`

## Module

Foundation
