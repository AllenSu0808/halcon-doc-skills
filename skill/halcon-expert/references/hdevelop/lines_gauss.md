# lines_gauss (Operator)

## Name

`lines_gauss` — Detect lines and their width.

## Signature

`lines_gauss(Image : Lines : Sigma, Low, High, LightDark, ExtractWidth, LineModel, CompleteJunctions : )`

## Description

The operator `lines_gauss` can be used to extract lines
(curvilinear structures) from the image *`Image`*. The
extracted lines are returned in *`Lines`* as subpixel precise
XLD-contours.

The parameter *`LightDark`* determines, whether
bright (*'light'*) or dark (*'dark'*) lines are extracted.

If *`ExtractWidth`* is set to *'true'* the line width
is extracted for each line point.

*`LineModel`* determines if and how the position and width of
asymmetric lines (lines having different contrast on each side of
the line) should be compensated. The following values can be set
for *`LineModel`*:

- ***'bar-shaped'*:** —

  Bar-shaped line model. Covers most
  use cases.
- ***'parabolic'*:** —

  Parabolic line model. Can be used for the
  extraction of backlit tubular objects (e.g., blood vessels
  in X-ray images) where the lines appear very sharp.
- ***'gaussian'*:** —

  Gaussian line model. Can be used for the
  extraction of backlit tubular objects (e.g., blood vessels
  in X-ray images) where the lines appear less sharp.
- ***'none'*:** —

  The effects of asymmetric lines are not compensated.

The parameter *`LineModel`* is only effective if
*`ExtractWidth`*=*'true'*.

Because the line extractor is unable to extract certain junctions
because of differential geometric reasons, it tries to extract these by
different means if *`CompleteJunctions`* is set to *'true'*.

The extraction is done by using partial derivatives of a Gaussian
smoothing kernel to determine the parameters of a quadratic
polynomial in x and y for each point of the image. The parameter
*`Sigma`* determines the amount of smoothing to be performed.
Larger values of *`Sigma`* lead to a larger smoothing of the
image, but can lead to worse localization of the line. Generally,
the localization will be much better than that of lines returned by
[`lines_facet`](lines_facet.md) with comparable parameters. The parameters of
the polynomial are used to calculate the line direction for each
pixel. Pixels which exhibit a local maximum in the second
directional derivative perpendicular to the line direction are
marked as line points. The line points found in this manner are
then linked to contours. This is done by immediately accepting line
points that have a second derivative larger than *`High`*.
Points that have a second derivative smaller than *`Low`* are
rejected. All other line points are accepted if they are connected
to accepted points by a connected path. This is similar to a
hysteresis threshold operation with infinite path length (see
[`hysteresis_threshold`](hysteresis_threshold.md)), here, however contours are extracted
with subpixel precision.

For the choice of the thresholds *`High`* and *`Low`*
one has to keep in mind that the second directional derivative
depends on the amplitude and width of the line as well as the choice
of *`Sigma`*. The value of the second derivative depends
linearly on the amplitude, i.e., the larger the amplitude, the
larger the response. For the width of the line there is an
approximately inverse exponential dependence: The wider the line is,
the smaller the response gets. This holds analogously for the
dependence on *`Sigma`*: The larger *`Sigma`* is
chosen, the smaller the second derivative will be. This means that
for larger smoothing correspondingly smaller values for
*`High`* and *`Low`* have to be chosen. Two examples
help to illustrate this: If 5 pixel wide lines with an amplitude
larger than 100 are to be extracted from an image with a smoothing
of *`Sigma`* = 1.5, *`High`* should be chosen larger
than 14. If, on the other hand, 10 pixel wide lines with an
amplitude larger than 100 and a *`Sigma`* = 3 are to be
detected, *`High`* should be chosen larger than 3.5. For the
choice of *`Low`* values between 0.25 *`High`* and 0.5
*`High`* are appropriate.

The parameters *`Low`* and *`High`* can be calculated from
the respective gray value contrast of the lines to be extracted
($ContrastLow$ and $ContrastHigh$)
and from the chosen value for *`Sigma`* with the following formula:

$$\left(\text{Low}\n\text{High}\right) = \left| -2 \cdot \left( \text{ContrastLow} \over \text{ContrastHigh} \right) \cdot \dfrac{w}{\sqrt{2\pi} \cdot \text{Sigma}^3} \cdot e^{-\dfrac{w^2}{2 \cdot \text{Sigma}^2}} \right|$$ ![figure](../assets/74e850d0ccb97a07.svg)
where $w$ is the width (half the diameter) of
the lines in the image. $ContrastLow$ and
$ContrastHigh$ determine the gray value range the lines
are expected to differ from the background.
Suitable values for *`Low`* and *`High`* can be calculated using
the procedure `calculate_lines_gauss_parameters`.

The extracted lines are returned in a topologically sound data
structure in *`Lines`*. This means that lines are correctly
split at junction points.

`lines_gauss` defines the following attributes for each
line point if *`ExtractWidth`* was set to *'false'*:

- ***'angle'*:** —

  The angle of the direction perpendicular
  to the line
- ***'response'*:** —

  The magnitude of the second derivative

If *`ExtractWidth`* was set to *'true'*, the following
attributes are defined in addition to *'angle'* and
*'response'*:

- ***'width_left'*:** —

  The line width to the left of the line
- ***'width_right'*:** —

  The line width to the right of the line

If *`ExtractWidth`* was set to *'true'* and
*`LineModel`* to a value different from *'none'*, the
following attributes are defined in addition to *'angle'*,
*'response'*, *'width_left'*, and
*'width_right'*:

- ***'asymmetry'*:** —

  The asymmetry of the line point
- ***'contrast'*:** —

  The contrast of the line point

Here, the asymmetry is positive if the asymmetric part, i.e., the
part with the weaker gradient, is on the right side of the line,
while it is negative if the asymmetric part is on the left side of
the line.

The contrast results from the difference between the gray value
of the line and the gray value of the background.
The contrast is positive if bright lines are extracted, while it
is negative if dark lines are extracted.
The returned contrast may be larger than the maximum gray value the input
image type is able to represent, especially if the line model specified by
*`LineModel`* is not present in the image. For example, for byte images,
the contrast may be greater than 255.

Use [`get_contour_attrib_xld`](get_contour_attrib_xld.md) to obtain attribute values.
See the operator reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further
information about contour attributes.

`lines_gauss` can be executed on OpenCL devices.

## Attention

In general, but in particular if the line width is to be extracted,
$\Sigma \geq \omega / \sqrt{3}$ ![figure](../assets/c6d84e4b87a01a5d.svg)
should be selected, where $w$ is the width (half the diameter) of
the lines in the image. As the lowest allowable value
$\texttt{Sigma}\ge w/2.5$
must be selected. If, for example, lines with a width of
4 pixels (diameter 8 pixels) are to be extracted, $\texttt{Sigma}\ge2.3$ should be selected. Note that the
attributes *'width_left'*, *'width_right'*,
*'asymmetry'*, and *'contrast'* are set to zero if
*`Sigma`* is set too low.

`lines_gauss` uses a special implementation that is optimized
using SSE2 or AVX2 instructions, if the system parameters
*'sse2_enable'* or *'avx2_enable'* are set to *'true'*
(see [`set_system`](set_system.md)). These implementations are
slightly inaccurate compared to the pure C version due to numerical
issues. If you prefer accuracy over performance you can set
the respective system parameter to *'false'* (using
[`set_system`](set_system.md)) before you call `lines_gauss`. This way
`lines_gauss` does not use SSE2 or AVX2 accelerations. Don't forget
to set *'sse2_enable'* or *'avx2_enable'* back to
*'true'* afterwards.

When `lines_gauss` is run on OpenCL devices, the same limitations
apply as for [`derivate_gauss`](derivate_gauss.md): *`Sigma`* must be chosen so that
the required filter mask is smaller than 129 pixels. Also note that the
results can vary compared to the CPU implementation.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`Lines`** (output_object)  xld_cont-array `→` object

Extracted lines.

**`Sigma`** (input_control)  number `→`  (real / integer)

Amount of Gaussian smoothing to be applied.

Default:
1.5

Suggested values:
1, 1.2, 1.5, 1.8, 2, 2.5, 3, 4, 5

Value range:
`0
≤
Sigma`

Recommended increment:
0.1

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

**`ExtractWidth`** (input_control)  string `→`  (string)

Should the line width be extracted?

Default:
'true'

List of values:
'false', 'true'

**`LineModel`** (input_control)  string `→`  (string)

Line model used to correct the line position and width.

Default:
'bar-shaped'

List of values:
'bar-shaped', 'gaussian', 'none', 'parabolic'

**`CompleteJunctions`** (input_control)  string `→`  (string)

Should junctions be added where they cannot be
extracted?

Default:
'true'

List of values:
'false', 'true'

## Example (HDevelop)

```
* Detection of lines in an aerial image
read_image(Image,'mreut4_3')
lines_gauss(Image,Lines,1.5,3,8,'light','true','bar-shaped','true')
dev_display(Lines)
```

## Complexity

Let A be the number of pixels in the domain of *`Image`*.
Then the runtime complexity is O(A**`Sigma`*).

The amount of temporary memory required is dependent on the height
H of the domain of *`Image`* and the width W of
*`Image`*. Let S = W*H, then `lines_gauss` requires at
least 55*S bytes of temporary memory during execution.

## Result

`lines_gauss` returns 2 (
H_MSG_TRUE)
if all parameters are correct and
no error occurs during execution. If the input is empty the
behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Successors

`gen_polygons_xld`

## Alternatives

`lines_facet`

## See also

`bandpass_image`,
`dyn_threshold`,
`topographic_sketch`

## References

C. Steger: “Extracting Curvilinear Structures: A Differential
Geometric Approach”. In B. Buxton, R. Cipolla, eds., “Fourth
European Conference on Computer Vision”, Lecture Notes in Computer
Science, Volume 1064, Springer Verlag, pp. 630-641, 1996.
  
C. Steger: “Extraction of Curved Lines from Images”. In “13th
International Conference on Pattern Recognition”, Volume II,
pp. 251-255, 1996.
  
C. Steger: “An Unbiased Detector of Curvilinear Structures”.
IEEE Transactions on Pattern Analysis and Machine Intelligence,
vol. 20, no. 2, pp. 113-125, 1998.
  
C. Steger: “Unbiased extraction of lines with parabolic and
Gaussian profiles”. Computer Vision and Image Understanding,
vol. 117, no. 2, pp. 97-112, 2013.

## Module

2D Metrology
