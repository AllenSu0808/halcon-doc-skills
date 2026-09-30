# shape_histo_point (Operator)

## Name

`shape_histo_point` — Determine a histogram of features along all threshold values.

## Signature

`def shape_histo_point(region: HObject, image: HObject, feature: str, row: int, column: int) -> Tuple[Sequence[Union[int, float]], Sequence[float]]`

## Description

Like [`shape_histo_all`](shape_histo_all.md) the operator
`shape_histo_point` carries out 255 threshold value operations
within *`region`* with the gray values of *`image`*.
Contrary to [`shape_histo_all`](shape_histo_all.md) only the segmented region
containing the pixel (*`row`*, *`column`*) is taken
into account here. The entry i in the histogram then corresponds
to the number of holes of this region segmented with the threshold
i (*`feature`* = *"holes"*) or the feature value of
the region (*`feature`* = *"convexity"*,
*"compactness"*, *"anisometry"*), respectively.

## Attention

Note that the operator `shape_histo_point` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Region in which the features are to be examined.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Gray value image.

**`feature`** (input_control)  string `→` str

Feature to be examined.

Default:
"convexity"

List of values:
"anisometry", "compactness", "convexity", "holes"

**`row`** (input_control)  point.y `→` int

Row of the pixel which the region must contain.

Default:
256

Suggested values:
10, 50, 100, 200, 300, 400

**`column`** (input_control)  point.x `→` int

Column of the pixel which the region must contain.

Default:
256

Suggested values:
10, 50, 100, 200, 300, 400

**`absolute_histo`** (output_control)  histogram-array `→` Sequence[Union[int, float]]

Absolute distribution of the feature.

**`relative_histo`** (output_control)  histogram-array `→` Sequence[float]

Relative distribution of the feature.

## Result

The operator `shape_histo_point` returns the value 2 (
H_MSG_TRUE)
if an
image with defined gray values is entered. The behavior in case of
empty input (no input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`get_mbutton`,
`area_center`

## Possible Successors

`histo_to_thresh`,
`threshold`,
`gen_region_histo`

## Alternatives

`shape_histo_all`

## See also

`connection`,
`connect_and_holes`,
`convexity`,
`compactness`

## Module

Foundation
