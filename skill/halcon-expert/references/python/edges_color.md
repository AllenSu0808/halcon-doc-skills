# edges_color (Operator)

## Name

`edges_color` — Extract color edges using Canny, Deriche, or Shen filters.

## Signature

`def edges_color(image: HObject, filter: str, alpha: float, nms: str, low: int, high: int) -> Tuple[HObject, HObject]`

## Description

`edges_color` extracts color edges from the input image
*`image`*. To define color edges, the multi-channel image
*`image`* is regarded as a mapping $f:\\ R^{2} \\rightarrow R^{n}$ ![figure](../assets/24ef73bf6dc5c243.svg), where $n$ is the number of channels in
*`image`*. For such functions, there is a natural extension of
the gradient: the metric tensor $G$, which can be used to
calculate for every direction, given by the direction vector
$v$, the rate of change of $f$ in the direction $v$. For
notational convenience, $G$ will be regarded as a
two-dimensional matrix. Thus, the rate of change of the function
$f$ in the direction $v$ is given by $v^{T}Gv$,
where
$$G =\left(\begin{array}{cc} f_x^T f_x & f_x^T f_y \\ f_y^T f_x & f_y^T f_y \end{array}\right) =\left(\begin{array}{cc} \sum_{i=1}^{n} \frac{\partial f_i}{\partial x} \frac{\partial f_i}{\partial x} & \sum_{i=1}^{n} \frac{\partial f_i}{\partial x} \frac{\partial f_i}{\partial y} \\\ \sum_{i=1}^{n} \frac{\partial f_i}{\partial x} \frac{\partial f_i}{\partial x} & \sum_{i=1}^{n} \frac{\partial f_i}{\partial y} \frac{\partial f_i}{\partial y} \end{array}\right) .$$ ![figure](../assets/02e553137b18b009.svg)
The partial derivatives of the images, which are necessary to
calculate the metric tensor, are calculated with the corresponding
edge filters, analogously to [`edges_image`](edges_image.md). For
*`filter`* = *"canny"*, the partial derivatives of the
Gaussian smoothing masks are used (see [`derivate_gauss`](derivate_gauss.md)), for
*"deriche1"* and *`filter`* = *"deriche2"* the
corresponding Deriche filters, for *`filter`* = *"shen"*
the corresponding Shen filters, and for *`filter`* =
*"sobel_fast"* the Sobel filter. Analogously to
single-channel images, the gradient direction is defined by the
vector $v$ in which the rate of change $f$ is maximum.
The vector $v$ is given by the eigenvector corresponding to
the largest eigenvalue of $G$. The square root of the
eigenvalue is the equivalent of the gradient magnitude (the
amplitude) for single-channel images, and is returned in
*`ima_amp`*. For single-channel images, both definitions are
equivalent. Since the gradient magnitude may be larger than what
can be represented in the input image data type (byte or uint2), it
is stored in the next larger data type (uint2 or int4) in
*`ima_amp`*. The eigenvector also is used to define the edge
direction. In contrast to single-channel images, the edge direction
can only be defined modulo 180 degrees. Like in the output of
[`edges_image`](edges_image.md), the edge directions are stored in 2-degree
steps, and are returned in *`ima_dir`*. Points with edge
amplitude 0 are assigned the edge direction 255 (undefined
direction). For speed reasons, the edge directions are not computed
explicitly for *`filter`* = *"sobel_fast"*. Therefore,
*`ima_dir`* is an empty object in this case.

The “filter width” (i.e., the amount of smoothing) can be chosen
arbitrarily for all filters except *"sobel_fast"* (where the
filter width is 3x3 and *`alpha`* is
ignored), and can be estimated by calling [`info_edges`](info_edges.md) for
concrete values of the parameter *`alpha`*. It decreases for
increasing *`alpha`* for the Deriche and Shen filters and
increases for the Canny filter, where it is the standard deviation
of the Gaussian on which the Canny operator is based. “Wide”
filters exhibit a larger invariance to noise, but also a decreased
ability to detect small details. Non-recursive filters, such as the
Canny filter, are realized using filter masks, and thus the
execution time increases for increasing filter width. In contrast,
the execution time for recursive filters does not depend on the
filter width. Thus, arbitrary filter widths are possible using the
Deriche and Shen filters without increasing the run time of the
operator. The resulting advantage in speed compared to the Canny
operator naturally increases for larger filter widths. As border
treatment, the recursive operators assume that the images are zero
outside of the image, while the Canny operator mirrors the gray
value at the image border. The signal-noise-ratio of the filters is
comparable for the following choices of *`alpha`*:
Alpha('deriche2') = Alpha('deriche1') / 2,
Alpha('shen') = Alpha('deriche1') / 2,
Alpha('canny') = 1.77 / Alpha('deriche1').

`edges_color` optionally offers to apply a
non-maximum-suppression (*`nms`* =
*"nms"*/*"inms"*/*"hvnms"*; *"none"* if
not desired) and hysteresis threshold operation
(*`low`*,*`high`*; at least one negative if not desired)
to the resulting edge image. Conceptually, this corresponds to the
following calls:

|  |
| --- |
| `nonmax_suppression_dir(...,NMS,...)` |
| `hysteresis_threshold(...,Low,High,1000,...)`. |

Note that the hysteresis threshold operation is not applied if
*`nms`* is set to *"none"*.

For *"sobel_fast"*, the same non-maximum-suppression is
performed for all values of *`nms`* except *"none"*.
Additionally, for *"sobel_fast"* the resulting edges are
thinned to a width of one pixel.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Input image.

**`ima_amp`** (output_object)  singlechannelimage(-array) `→` HObject (uint2 / int4)

Edge amplitude (gradient magnitude) image.

**`ima_dir`** (output_object)  singlechannelimage(-array) `→` HObject (direction)

Edge direction image.

**`filter`** (input_control)  string `→` str

Edge operator to be applied.

Default:
"canny"

List of values:
"canny", "deriche1", "deriche2", "shen", "sobel_fast"

**`alpha`** (input_control)  real `→` float

Filter parameter: small values result in strong
smoothing, and thus less detail (opposite for
'canny').

Default:
1.0

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 2.5, 3.0

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Alpha > 0.0`

**`nms`** (input_control)  string `→` str

Non-maximum suppression ('none', if not desired).

Default:
"nms"

List of values:
"hvnms", "inms", "nms", "none"

**`low`** (input_control)  integer `→` int

Lower threshold for the hysteresis threshold operation
(negative if no thresholding is desired).

Default:
20

Suggested values:
5, 10, 15, 20, 25, 30, 40

Minimum increment:
1

Recommended increment:
5

Restriction:
`Low >= 1 || Low < 0`

**`high`** (input_control)  integer `→` int

Upper threshold for the hysteresis threshold operation
(negative if no thresholding is desired).

Default:
40

Suggested values:
10, 15, 20, 25, 30, 40, 50, 60, 70

Minimum increment:
1

Recommended increment:
5

Restriction:
`High >= 1 || High < 0 && High >= Low`

## Result

`edges_color` returns 2 (
H_MSG_TRUE)
if all parameters are correct
and no error occurs during execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`threshold`

## Alternatives

`edges_color_sub_pix`

## See also

`edges_image`,
`edges_sub_pix`,
`info_edges`,
`nonmax_suppression_amp`,
`hysteresis_threshold`

## References

C. Steger: “Subpixel-Precise Extraction of Lines and Edges”;
International Archives of Photogrammetry and Remote Sensing,
vol. XXXIII, part B3; pp. 141-156; 2000.
  
C. Steger: “Unbiased Extraction of Curvilinear Structures from 2D
and 3D Images”; Herbert Utz Verlag, München; 1998.
  
S. Di Zenzo: “A Note on the Gradient of a Multi-Image”; Computer
Vision, Graphics, and Image Processing, vol. 33; pp. 116-125;
1986.
  
Aldo Cumani: “Edge Detection in Multispectral Images”; Computer
Vision, Graphics, and Image Processing: Graphical Models and Image
Processing, vol. 53, no. 1; pp. 40-51; 1991.
  
J.Canny: “Finding Edges and Lines in Images”; Report, AI-TR-720;
M.I.T. Artificial Intelligence Lab., Cambridge; 1983.
  
J.Canny: “A Computational Approach to Edge Detection”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-8,
vol. 6; pp. 679-698; 1986.
  
R.Deriche: “Using Canny's Criteria to Derive a Recursively
Implemented Optimal Edge Detector”; International Journal of
Computer Vision; vol. 1, no. 2; pp. 167-187; 1987.
  
R.Deriche: “Fast Algorithms for Low-Level Vision”; IEEE
Transactions on Pattern Analysis and Machine Intelligence; PAMI-12,
no. 1; pp. 78-87; 1990.
  
J. Shen, S. Castan: “An Optimal Linear Operator for Step Edge
Detection”; Computer Vision, Graphics, and Image Processing:
Graphical Models and Image Processing, vol. 54, no. 2;
pp. 112-133; 1992.

## Module

Foundation
