# lines_color (Operator)

## Name

`lines_color` — Detect color lines and their width.

## Signature

`lines_color(Image : Lines : Sigma, Low, High, ExtractWidth, CompleteJunctions : )`

## Description

`lines_color` extracts color lines from the input image
*`Image`* and returns the extracted lines as subpixel precise
XLD-contours in *`Lines`*. Color lines are defined as dark
lines in the amplitude image of the color edge filter (see
[`edges_color`](edges_color.md)). `lines_color` always uses the Canny
color edge filter. Hence, the required partial derivatives of the
image are always computed by convolution with the respective partial
derivatives of the Gaussian smoothing masks (see
[`derivate_gauss`](derivate_gauss.md)). The corresponding smoothing is determined
by the parameter *`Sigma`*.

By defining color lines as dark lines in the amplitude image, in
contrast to [`lines_gauss`](lines_gauss.md), for single-channel images no
distinction is made whether the lines are darker or brighter than
their surroundings. Furthermore, `lines_color` also returns
staircase lines, i.e., lines for which the gray value of the lines
lies between the gray values in the surrounding area to the left and
right sides of the line. In multi-channel images, the above
definition allows each channel to have a different line type. For
example, in a three-channel image the first channel may have a dark
line, the second channel a bright line, and the third channel a
staircase line at the same position.

If *`ExtractWidth`* is set to *'true'* the line width is
extracted for each line point. Because the line extractor is unable
to extract certain junctions because of differential geometric
reasons, it tries to extract these by different means if
*`CompleteJunctions`* is set to *'true'*.

`lines_color` links the line points into lines by using an
algorithm similar to a hysteresis threshold operation, which is also
used in [`lines_gauss`](lines_gauss.md) and [`edges_color_sub_pix`](edges_color_sub_pix.md). Points
with an amplitude larger than *`High`* are immediately accepted
as belonging to a line, while points with an amplitude smaller than
*`Low`* are rejected. All other points are accepted as lines
if they are connected to accepted line points (see also
[`lines_gauss`](lines_gauss.md)). Here, amplitude means the line amplitude of
the dark line (see [`lines_gauss`](lines_gauss.md) and [`lines_facet`](lines_facet.md)).
This value corresponds to the third directional derivative of the
smoothed input image in the direction perpendicular to the line.

For the choice of the thresholds *`High`* and *`Low`* one
has to keep in mind that the third directional derivative depends on
the amplitude and width of the line as well as the choice of
*`Sigma`*. The value of the third derivative depends linearly
on the amplitude, i.e., the larger the amplitude, the larger the
response. For the width of the line there is an inverse dependence:
The wider the line is, the smaller the response gets. This holds
analogously for the dependence on *`Sigma`*: The larger
*`Sigma`* is chosen, the smaller the second derivative will be.
This means that for larger smoothing correspondingly smaller values
for *`High`* and *`Low`* should be chosen.

The extracted lines are returned in a topologically sound data
structure in *`Lines`*. This means that lines are correctly
split at junction points.

`lines_color` defines the following attributes for each
line point if *`ExtractWidth`* was set to *'false'*:

- *'angle'* The angle of the direction perpendicular
  to the line (oriented such that the normal
  vectors point to the right side of the
  line as the line is traversed from
  start to end point; the angles are given
  with respect to the row axis of the
  image.)
- *'response'*: The magnitude of the second derivative

If *`ExtractWidth`* was set to *'true'*, additionally
the following attributes are defined:

- *'width_left'*: The line width to the left of the line
- *'width_right'*: The line width to the right of the line

Use [`get_contour_attrib_xld`](get_contour_attrib_xld.md) to obtain attribute values.
See the operator reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further
information about contour attributes.

## Attention

In general, but in particular if the line width is to be extracted,
$\Sigma \geq \omega / \sqrt{3}$ ![figure](../assets/c6d84e4b87a01a5d.svg)
should be selected, where w is the width (half the diameter) of
the lines in the image. As the lowest allowable value
$\texttt{Sigma}\ge w/2.5$
*must* be selected. If, for example, lines with a width of
4 pixels (diameter 8 pixels) are to be extracted, $\texttt{Sigma}\ge2.3$ should be selected. If it is
expected that staircase lines are present in at least one channel,
and if such lines should be extracted, in addition to the above
restriction, $\texttt{Sigma}\le w$ should
be selected. This is necessary because staircase lines turn into
normal step edges for large amounts of smoothing, and therefore no
longer appear as dark lines in the amplitude image of the color edge
filter.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / uint2)

Input image.

**`Lines`** (output_object)  xld_cont-array `→` object

Extracted lines.

**`Sigma`** (input_control)  number `→`  (real / integer)

Amount of Gaussian smoothing to be applied.

Default:
1.5

Suggested values:
1, 1.2, 1.5, 1.8, 2, 2.5, 3, 4, 5

Recommended increment:
0.1

Restriction:
`Sigma > 0.0`

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

**`ExtractWidth`** (input_control)  string `→`  (string)

Should the line width be extracted?

Default:
'true'

List of values:
'false', 'true'

**`CompleteJunctions`** (input_control)  string `→`  (string)

Should junctions be added where they cannot be
extracted?

Default:
'true'

List of values:
'false', 'true'

## Complexity

The amount of temporary memory required is dependent on the height H
of the domain of *`Image`*.

## Result

`lines_color` returns 2 (
H_MSG_TRUE)
if all parameters are correct and
no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Successors

`gen_polygons_xld`

## Alternatives

`lines_gauss`,
`lines_facet`

## See also

`edges_color`,
`edges_color_sub_pix`

## References

C. Steger: “Subpixel-Precise Extraction of Lines and Edges”;
International Archives of Photogrammetry and Remote Sensing,
vol. XXXIII, part B3; pp. 141-156; 2000.
  
C. Steger: “An Unbiased Detector of Curvilinear Structures”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; vol. 20,
no. 2; pp. 113-125; 1998.
  
C. Steger: “Unbiased Extraction of Curvilinear Structures from 2D
and 3D Images”; Herbert Utz Verlag, München; 1998.

## Module

2D Metrology
