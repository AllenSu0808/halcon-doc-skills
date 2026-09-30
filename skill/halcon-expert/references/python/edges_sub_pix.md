# edges_sub_pix (Operator)

## Name

`edges_sub_pix` — Extract sub-pixel precise edges using Deriche, Lanser, Shen, or Canny
filters.

## Signature

`def edges_sub_pix(image: HObject, filter: str, alpha: float, low: Union[int, float], high: Union[int, float]) -> HObject`

## Description

`edges_sub_pix` detects step edges using recursively implemented
filters (according to Deriche, Lanser and Shen) or the conventionally
implemented “derivative of Gaussian” filter (using filter masks)
proposed by Canny. Thus, the following edge operators are
available for *`filter`*:

*"deriche1"*, *"lanser1"*, *"deriche2"*,
*"lanser2"*, *"shen"*, *"mshen"*, *"canny"*,
*"sobel"* and *"sobel_fast"*.

The extracted edges are returned as sub-pixel precise XLD contours
in *`edges`*. For all edge operators except
*"sobel_fast"*, the following attributes are defined for each
edge point (see [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further details):

- ***"edge_direction"*:** —

  Gives the direction of the edge (not of
  the XLD contour), calculated from the image
  gradients in horizontal and vertical
  direction. The angles [rad] are given with
  respect to the column axis of the image.
- ***"angle"*:** —

  Direction of the normal vectors to the contour in
  radians (oriented such that the normal vectors point to
  the right side of the contour as the contour is
  traversed from start to end point; the angles
  are given with respect to the row axis of the
  image).
- ***"response"*:** —

  Edge amplitude (gradient magnitude).

The “filter width” (i.e., the amount of smoothing) can be chosen
arbitrarily for all edge operators except *"sobel"* and
*"sobel_fast"*, and can be estimated by calling
[`info_edges`](info_edges.md) for concrete values of the parameter
*`alpha`*. For all filters (Deriche, Lanser and Shen filters), the
“filter width” decreases for increasing *`alpha`*. The only exception
is the Canny filter, where an increasing *`alpha`* also causes an
increase of the “filter width”. “Wide” filters exhibit a larger
invariance to noise, but also a decreased ability to detect small
details. Non-recursive filters, such as the Canny filter, are
realized using filter masks, and thus the execution time increases
for increasing filter width. In contrast, the execution time for
recursive filters does not depend on the filter width. Thus,
arbitrary filter widths are possible using the Deriche, Lanser and
Shen filters without increasing the run time of the operator. The
resulting advantage in speed compared to the Canny operator
naturally increases for larger filter widths. As border treatment,
the recursive operators assume that the images to be zero outside of
the image, while the Canny operator repeats the gray value at the
image's border. The signal-noise-ratio of the filters is
comparable for the following choices of *`alpha`*:
Alpha('lanser1') = Alpha('deriche1'),
Alpha('deriche2') = Alpha('deriche1') / 2,
Alpha('lanser2') = Alpha('deriche2'),
Alpha('shen') = Alpha('deriche1') / 2,
Alpha('mshen') = Alpha('shen'),
Alpha('canny') = 1.77 / Alpha('deriche1').
The originally proposed recursive filters (*"deriche1"*,
*"deriche2"*, *"shen"*) return a biased estimate of the
amplitude of diagonal edges.
This bias is removed in the corresponding modified version
of the operators (*"lanser1"*, *"lanser2"* and
*"mshen"*), while maintaining the same execution speed.

For relatively small filter widths (11 x 11),
i.e., for *`alpha`* (*"lanser2"* = *0.5*), all filters
yield similar results.
Only for “wider” filters differences begin to appear:
the Shen filters begin to yield qualitatively inferior results.
However, they are the fastest of the implemented operators that
support arbitrary mask sizes, closely followed by the Deriche
operators. The two Sobel filters, which use a fixed mask size of
(3 x 3), are faster than the other filters. Of
these two, the filter *"sobel_fast"* is significantly faster
than *"sobel"*.

`edges_sub_pix` links the edge points into edges by using
an algorithm similar to a hysteresis threshold operation, which is
also used in [`lines_gauss`](lines_gauss.md). Points with an amplitude
larger than *`high`* are immediately accepted as belonging to
an edge, while points with an amplitude smaller than *`low`*
are rejected. All other points are accepted as edges if they are
connected to accepted edge points (see also [`lines_gauss`](lines_gauss.md)
and [`hysteresis_threshold`](hysteresis_threshold.md)).

Because edge extractors are often unable to extract certain
junctions, a mode that tries to extract these missing junctions by
different means can be selected by appending *"_junctions"*
to the values of *`filter`* that are described above. This
mode is analogous to the mode for completing junctions that is
available in [`lines_gauss`](lines_gauss.md).

The edge operator *"sobel_fast"* has the same semantics as
all the other edge operators. Internally, however, it is based on
significantly simplified variants of the individual processing steps
(hysteresis thresholding, edge point linking, and extraction of the
subpixel edge positions). Therefore, *"sobel_fast"* in some
cases may return slightly less accurate edge positions and may
select different edge parts.

`edges_sub_pix` can be executed on OpenCL devices for the filter
types *"canny"* and *"sobel_fast"*. This will require
up to width*height*29 bytes of pinned memory. Since allocating memory
is an expensive operation, it would make sense to set the pinned memory
cache to at least this size (using [`set_compute_device_param`](set_compute_device_param.md) for
parameter *"pinned_mem_cache_capacity"*, or to disable pinned memory
completely (using [`set_compute_device_param`](set_compute_device_param.md) for parameter
*"alloc_pinned"*), in which case the normal memory cache is
used. Note that the results can vary from the CPU implementation.

## Attention

Since `edges_sub_pix` uses Gauss convolution internally for the
*"canny"* filter, the same limitations for OpenCL apply as for
[`derivate_gauss`](derivate_gauss.md): *`alpha`* must be chosen small enough that
the required filter mask is less than 129 pixels in size. Also,
`edges_sub_pix` is not available on OpenCL devices for HALCON XL, as
double precision floating point arithmetic would be required, but OpenCL
devices are optimized for single precision arithmetic.

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

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Input image.

**`edges`** (output_object)  xld_cont-array `→` HObject

Extracted edges.

**`filter`** (input_control)  string `→` str

Edge operator to be applied.

Default:
"canny"

List of values:
"canny", "canny_junctions", "deriche1", "deriche1_junctions", "deriche2", "deriche2_junctions", "lanser1", "lanser1_junctions", "lanser2", "lanser2_junctions", "mshen", "mshen_junctions", "shen", "shen_junctions", "sobel", "sobel_fast", "sobel_junctions"

List of values (for compute devices):
"canny", "sobel_fast"

**`alpha`** (input_control)  real `→` float

Filter parameter: small values result in strong
smoothing, and thus less detail (opposite for
'canny').

Default:
1.0

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.1

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Alpha > 0.0`

**`low`** (input_control)  integer `→` Union[int, float]

Lower threshold for the hysteresis threshold operation.

Default:
20

Suggested values:
5, 10, 15, 20, 25, 30, 40

Minimum increment:
1

Recommended increment:
5

Restriction:
`Low > 0`

**`high`** (input_control)  integer `→` Union[int, float]

Upper threshold for the hysteresis threshold operation.

Default:
40

Suggested values:
10, 15, 20, 25, 30, 40, 50, 60, 70

Minimum increment:
1

Recommended increment:
5

Restriction:
`High > 0 && High >= Low`

## Complexity

Let A be the number of pixels in the domain of *`image`*.
Then the runtime complexity is O(A**`alpha`*) for the Canny
filter and O(A) for the recursive Lanser, Deriche, and Shen
filters.

The amount of temporary memory required is dependent on the height H
of the domain of *`image`* and the width W of *`image`*.
Let S = W*H, then `edges_sub_pix` requires at least 60*S
bytes of temporary memory during execution for all edge operators
except *"sobel_fast"*. For *"sobel_fast"*, at least
9*S bytes of temporary memory are required.

## Result

`edges_sub_pix` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`segment_contours_xld`,
`gen_polygons_xld`,
`select_shape_xld`

## Alternatives

`sobel_dir`,
`frei_dir`,
`kirsch_dir`,
`prewitt_dir`,
`robinson_dir`,
`edges_image`

## See also

`info_edges`,
`hysteresis_threshold`,
`bandpass_image`,
`lines_gauss`,
`lines_facet`

## References

S.Lanser, W.Eckstein: “Eine Modifikation des Deriche-Verfahrens zur
Kantendetektion”; 13. DAGM-Symposium, München; Informatik
Fachberichte 290; Seite 151 - 158; Springer-Verlag; 1991.
  
S.Lanser: “Detektion von Stufenkanten mittels rekursiver Filter
nach Deriche”; Diplomarbeit; Technische Universität München,
Institut für Informatik, Lehrstuhl Prof. Radig; 1991.
  
J.Canny: “Finding Edges and Lines in Images”; Report, AI-TR-720;
M.I.T. Artificial Intelligence Lab., Cambridge; 1983.
  
J.Canny: “A Computational Approach to Edge Detection”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-8,
vol. 6; S. 679-698; 1986.
  
R.Deriche: “Using Canny's Criteria to Derive a Recursively
Implemented Optimal Edge Detector”; International Journal of
Computer Vision; vol. 1, no. 2; S. 167-187; 1987.
  
R.Deriche: “Optimal Edge Detection Using Recursive Filtering”;
Proc. of the First International Conference on Computer Vision,
London; S. 501-505; 1987.
  
R.Deriche: “Fast Algorithms for Low-Level Vision”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-12,
no. 1; S. 78-87; 1990.
  
S.Castan, J.Zhao und J.Shen: “Optimal Filter for Edge Detection
Methods and Results”; Proc. of the First European Conference on
Computer Vision, Antibes; Lecture Notes on computer Science;
no. 427; S. 12-17; Springer-Verlag; 1990.

## Module

2D Metrology
