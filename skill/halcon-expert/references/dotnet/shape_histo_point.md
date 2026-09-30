# ShapeHistoPoint (Operator)

## Name

`ShapeHistoPoint` — Determine a histogram of features along all threshold values.

## Signature

`static void HOperatorSet.ShapeHistoPoint(HObject region, HObject image, HTuple feature, HTuple row, HTuple column, out HTuple absoluteHisto, out HTuple relativeHisto)`

`HTuple HRegion.ShapeHistoPoint(HImage image, string feature, int row, int column, out HTuple relativeHisto)`

## Description

Like [`ShapeHistoAll`](shape_histo_all.md) the operator
`ShapeHistoPoint` carries out 255 threshold value operations
within *`region`* with the gray values of *`image`*.
Contrary to [`ShapeHistoAll`](shape_histo_all.md) only the segmented region
containing the pixel (*`row`*, *`column`*) is taken
into account here. The entry i in the histogram then corresponds
to the number of holes of this region segmented with the threshold
i (*`feature`* = *"holes"*) or the feature value of
the region (*`feature`* = *"convexity"*,
*"compactness"*, *"anisometry"*), respectively.

## Attention

Note that the operator `ShapeHistoPoint` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Region in which the features are to be examined.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Gray value image.

**`feature`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Feature to be examined.

Default:
"convexity"

List of values:
"anisometry", "compactness", "convexity", "holes"

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row of the pixel which the region must contain.

Default:
256

Suggested values:
10, 50, 100, 200, 300, 400

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column of the pixel which the region must contain.

Default:
256

Suggested values:
10, 50, 100, 200, 300, 400

**`absoluteHisto`** (output_control)  histogram-array `→` [HTuple](HTuple.md) (*double* / int / long)

Absolute distribution of the feature.

**`relativeHisto`** (output_control)  histogram-array `→` [HTuple](HTuple.md) (*double*)

Relative distribution of the feature.

## Result

The operator `ShapeHistoPoint` returns the value 2 (
H_MSG_TRUE)
if an
image with defined gray values is entered. The behavior in case of
empty input (no input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`GetMbutton`,
`AreaCenter`

## Possible Successors

`HistoToThresh`,
`Threshold`,
`GenRegionHisto`

## Alternatives

`ShapeHistoAll`

## See also

`Connection`,
`ConnectAndHoles`,
`Convexity`,
`Compactness`

## Module

Foundation
