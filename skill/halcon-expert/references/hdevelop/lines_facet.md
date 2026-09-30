# lines_facet (Operator)

## Name

`lines_facet` — Detection of lines using the facet model.

## Signature

`lines_facet(Image : Lines : MaskSize, Low, High, LightDark : )`

## Description

The operator `lines_facet` can be used to extract lines
(curvilinear structures) from the image *`Image`*. The
extracted lines are returned in *`Lines`* as subpixel
precise XLD-contours. The parameter *`LightDark`*
determines, whether bright or dark lines are extracted.

The extraction is done by using the facet model, i.e., a least
squares fit, to determine the parameters of a quadratic polynomial
in x and y for each point of the image. The parameter
*`MaskSize`* determines the size of the window used for the
least squares fit. Larger values of *`MaskSize`* lead to a
larger smoothing of the image, but can lead to worse localization of
the line. The parameters of the polynomial are used to calculate
the line direction for each pixel. Pixels which exhibit a local
maximum in the second directional derivative perpendicular to the
line direction are marked as line points. The line points found in
this manner are then linked to contours. This is done by
immediately accepting line points that have a second derivative
larger than *`High`*. Points that have a second derivative
smaller than *`Low`* are rejected. All other line points are
accepted if they are connected to accepted points by a connected
path. This is similar to a hysteresis threshold operation with
infinite path length (see [`hysteresis_threshold`](hysteresis_threshold.md)).
However, this function is not used internally since it does not
allow the extraction of subpixel precise contours.

The gist of how to select the thresholds in the description of
[`lines_gauss`](lines_gauss.md) also holds for this operator. A value of
Sigma = 1.5 there roughly corresponds to a *`MaskSize`* of 5
here.

The extracted lines are returned in a topologically sound data
structure in *`Lines`*. This means that lines are correctly
split at junction points.

`lines_facet` defines the following attributes for each
line point:

- ***'angle'*:** —

  The angle of the direction perpendicular
  to the line
- ***'response'*:** —

  The magnitude of the second derivative

Use [`get_contour_attrib_xld`](get_contour_attrib_xld.md) to obtain attribute values.
See the operator reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further
information about contour attributes.

## Attention

The smaller the filter size *`MaskSize`* is chosen, the more
short, fragmented lines will be extracted. This can lead to
considerably longer execution times.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`Lines`** (output_object)  xld_cont-array `→` object

Extracted lines.

**`MaskSize`** (input_control)  integer `→`  (integer)

Size of the facet model mask.

Default:
5

List of values:
3, 5, 7, 9, 11

**`Low`** (input_control)  number `→`  (real / integer)

Lower threshold for the hysteresis threshold
operation.

Default:
3

Suggested values:
0, 0.5, 1, 2, 3, 4, 5, 8, 10

Value range:
`0
≤
Low`

Recommended increment:
0.5

**`High`** (input_control)  number `→`  (real / integer)

Upper threshold for the hysteresis threshold
operation.

Default:
8

Suggested values:
0, 0.5, 1, 2, 3, 4, 5, 8, 10, 12, 15, 18, 20, 25

Value range:
`0
≤
High`

Recommended increment:
0.5

Restriction:
`High >= Low`

**`LightDark`** (input_control)  string `→`  (string)

Extract bright or dark lines.

Default:
'light'

List of values:
'dark', 'light'

## Example (HDevelop)

```
* Detection of lines in an aerial image
read_image(Image,'mreut4_3')
lines_facet(Image,Lines,5,3,8,'light')
dev_display(Lines)
```

## Complexity

Let A be the number of pixels in the domain of *`Image`*.
Then the runtime complexity is O(A**`MaskSize`*).

The amount of temporary memory required is dependent on the height H
of the domain of *`Image`* and the width W of *`Image`*.
Let S = W*H, then `lines_facet` requires at least 55*S
bytes of temporary memory during execution.

## Result

`lines_facet` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Successors

`gen_polygons_xld`

## Alternatives

`lines_gauss`

## See also

`bandpass_image`,
`dyn_threshold`,
`topographic_sketch`

## References

A. Busch: “Fast Recognition of Lines in Digital Images Without
User-Supplied Parameters”. In H. Ebner, C. Heipke, K.Eder, eds.,
“Spatial Information from Digital Photogrammetry and Computer
Vision”, International Archives of Photogrammetry and Remote
Sensing, Vol. 30, Part 3/1, pp. 91-97, 1994.

## Module

2D Metrology
