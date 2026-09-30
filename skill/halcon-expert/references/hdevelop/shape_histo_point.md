# shape_histo_point (Operator)

## Name

`shape_histo_point` — Determine a histogram of features along all threshold values.

## Signature

`shape_histo_point(Region, Image : : Feature, Row, Column : AbsoluteHisto, RelativeHisto)`

## Description

Like [`shape_histo_all`](shape_histo_all.md) the operator
`shape_histo_point` carries out 255 threshold value operations
within *`Region`* with the gray values of *`Image`*.
Contrary to [`shape_histo_all`](shape_histo_all.md) only the segmented region
containing the pixel (*`Row`*, *`Column`*) is taken
into account here. The entry i in the histogram then corresponds
to the number of holes of this region segmented with the threshold
i (*`Feature`* = *'holes'*) or the feature value of
the region (*`Feature`* = *'convexity'*,
*'compactness'*, *'anisometry'*), respectively.

## Attention

Note that the operator `shape_histo_point` only considers
the given *`Region`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

Region in which the features are to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Gray value image.

**`Feature`** (input_control)  string `→`  (string)

Feature to be examined.

Default:
'convexity'

List of values:
'anisometry', 'compactness', 'convexity', 'holes'

**`Row`** (input_control)  point.y `→`  (integer)

Row of the pixel which the region must contain.

Default:
256

Suggested values:
10, 50, 100, 200, 300, 400

**`Column`** (input_control)  point.x `→`  (integer)

Column of the pixel which the region must contain.

Default:
256

Suggested values:
10, 50, 100, 200, 300, 400

**`AbsoluteHisto`** (output_control)  histogram-array `→`  (real / integer)

Absolute distribution of the feature.

**`RelativeHisto`** (output_control)  histogram-array `→`  (real)

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
