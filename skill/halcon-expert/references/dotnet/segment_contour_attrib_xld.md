# SegmentContourAttribXld (Operator)

## Name

`SegmentContourAttribXld` — Segment XLD contour parts whose local attributes fulfill given
conditions.

## Signature

`static void HOperatorSet.SegmentContourAttribXld(HObject contour, out HObject contourPart, HTuple attribute, HTuple operation, HTuple min, HTuple max)`

`HXLDCont HXLDCont.SegmentContourAttribXld(HTuple attribute, string operation, HTuple min, HTuple max)`

`HXLDCont HXLDCont.SegmentContourAttribXld(string attribute, string operation, double min, double max)`

## Description

`SegmentContourAttribXld` segments the contour in
*`contour`* into contour parts *`contourPart`*. The segmentation
of the contour depends on the values of its attributes *`attribute`*
(see the possible values for *`attribute`* below).
The operator checks which attribute values lie within the given limits
(*`min`*, *`max`*) and returns the corresponding contour
segments with its attributes in *`contourPart`*.

If *`operation`* is set to *"and"*, each of the given attributes
must lie within the limits.
If *`operation`* is set to *"or"*, at least one of
the attributes has to be within the limits. The attributes are processed
in the same order as they are given in *`attribute`*.
If only one attribute is used, the value of *`operation`* is
ignored.
The parameters *`min`* and *`max`* can be set to
*"min"* or *"max"* in order to leave bottom and top limit,
respectively, open.

Note that not all attributes are defined in all contours per default.
Which attributes
are defined for a contour depends on how the contour was
instantiated, and whether some operations have been previously performed on
it. For example, the attributes *"width_right"* and
*"width_left"* are only
defined, if the contour was created with the operator [`LinesGauss`](lines_gauss.md).
Likewise, the attribute *"distance"* is only present if the distances
to some other contour was previously calculated with
[`DistanceContoursXld`](distance_contours_xld.md) or [`ApplyDistanceTransformXld`](apply_distance_transform_xld.md).

Condition: $Min_{i}\le Attribute_{i}(Object)\le Max_{i}$

Possible values for *`attribute`*:

- **'edge_direction':** —

  Edge direction
- **'angle':** —

  Angle of the direction perpendicular to the contour
- **'response':** —

  Magnitude of the second derivative
- **'width_right':** —

  Line width to the right of the line
- **'width_left':** —

  Line width to the left of the line
- **'contrast':** —

  Contrast of the line point
- **'asymmetry':** —

  Asymmetry of the line point
- **'distance':** —

  Minimum pointwise distance to a reference contour

To find out which operators add the attributes above to contours and further
details about those attributes, see [`GetContourAttribXld`](get_contour_attrib_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contour to be segmented.

**`contourPart`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Segmented contour parts.

**`attribute`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Contour attributes to be checked.

Default:
"distance"

List of values:
"angle", "asymmetry", "contrast", "distance", "edge_direction", "response", "width_left", "width_right"

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Linkage type of the individual attributes.

Default:
"and"

List of values:
"and", "or"

**`min`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Lower limits of the attribute values.

Default:
150.0

Minimum increment:
0.001

Recommended increment:
1.0

**`max`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Upper limits of the attribute values.

Default:
99999.0

Minimum increment:
0.001

Recommended increment:
1.0

Restriction:
`Max >= Min`

## Example (HDevelop)

```
read_image (Image, 'fabrik')
edges_sub_pix (Image, Edges, 'canny', 1, 20, 40)
* select 'vertical' edges:
segment_contour_attrib_xld (Edges, ContourPart, 'edge_direction', \
                            'and', rad(90-20), rad(90+20))
```

## Result

The operator `SegmentContourAttribXld` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input
(no input objects available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`LinesGauss`,
`EdgesSubPix`,
`ApplyDistanceTransformXld`,
`DistanceContoursXld`

## Possible Successors

`FitLineContourXld`,
`FitEllipseContourXld`,
`FitCircleContourXld`,
`FitRectangle2ContourXld`

## See also

`SplitContoursXld`,
`GetContourGlobalAttribXld`,
`QueryContourAttribsXld`,
`GetContourAttribXld`

## Module

Foundation
