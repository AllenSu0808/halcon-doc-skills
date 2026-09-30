# EdgesColorSubPix (Operator)

## Name

`EdgesColorSubPix` — Extract subpixel precise color edges using Deriche, Shen, or Canny filters.

## Signature

`static void HOperatorSet.EdgesColorSubPix(HObject image, out HObject edges, HTuple filter, HTuple alpha, HTuple low, HTuple high)`

`HXLDCont HImage.EdgesColorSubPix(string filter, double alpha, HTuple low, HTuple high)`

`HXLDCont HImage.EdgesColorSubPix(string filter, double alpha, double low, double high)`

## Description

`EdgesColorSubPix` extracts subpixel precise color edges
from the input image *`image`*. The definition of color edges
is given in the description of [`EdgesColor`](edges_color.md). The same edge
filters as in [`EdgesColor`](edges_color.md) can be selected: *"canny"*,
*"deriche1"*, *"deriche2"*, and *"shen"*. In
addition, a fast Sobel filter can be selected with
*"sobel_fast"*. The filters are specified by the parameter
*`filter`*.

The “filter width” (i.e., the amount of smoothing) can be chosen
arbitrarily. For a detailed description of this parameter see
[`EdgesColor`](edges_color.md). This parameter is ignored for *`filter`*
= *"sobel_fast"*.

The extracted edges are returned as subpixel precise XLD contours in
*`edges`*. For all edge operators except for
*"sobel_fast"*, the following attributes are defined for each
edge point (see [`GetContourAttribXld`](get_contour_attrib_xld.md) for further information):

- *"edge_direction"*: Gives the direction of the edge (not of
  the XLD contour), calculated from the image gradients in horizontal and
  vertical direction.
  The angles [rad] are given with respect to the column axis of the image.
- *"angle"*: Direction of the normal vectors to the contour in
  radians (oriented such that the normal vectors point to the right side of
  the contour as the contour is traversed from start to end point;
  the angles are given with respect to the row axis of the image).
- *"response"*: Edge amplitude (gradient magnitude).

`EdgesColorSubPix` links the edge points into edges by
using an algorithm similar to a hysteresis threshold operation,
which is also used in [`EdgesSubPix`](edges_sub_pix.md) and [`LinesGauss`](lines_gauss.md).
Points with an amplitude larger than *`high`* are immediately
accepted as belonging to an edge, while points with an amplitude
smaller than *`low`* are rejected. All other points are
accepted as edges if they are connected to accepted edge points (see
also [`LinesGauss`](lines_gauss.md) and [`HysteresisThreshold`](hysteresis_threshold.md)).

Because edge extractors are often unable to extract certain
junctions, a mode that tries to extract these missing junctions by
different means can be selected by appending *"_junctions"*
to the values of *`filter`* that are described above. This
mode is analogous to the mode for completing junctions that is
available in [`EdgesSubPix`](edges_sub_pix.md) and [`LinesGauss`](lines_gauss.md).

The edge operator *"sobel_fast"* has the same semantics as
all the other edge operators. Internally, however, it is based on
significantly simplified variants of the individual processing steps
(hysteresis thresholding, edge point linking, and extraction of the
subpixel edge positions). Therefore, *"sobel_fast"* in some
cases may return slightly less accurate edge positions and may
select different edge parts.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`edges`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Extracted edges.

**`filter`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Edge operator to be applied.

Default:
"canny"

List of values:
"canny", "canny_junctions", "deriche1", "deriche1_junctions", "deriche2", "deriche2_junctions", "shen", "shen_junctions", "sobel_fast"

**`alpha`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

**`low`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Lower threshold for the hysteresis threshold operation.

Default:
20

Suggested values:
5, 10, 15, 20, 25, 30, 40

Value range:
`0
≤
low`

Minimum increment:
1

Recommended increment:
5

Restriction:
`Low > 0`

**`high`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Upper threshold for the hysteresis threshold operation.

Default:
40

Suggested values:
10, 15, 20, 25, 30, 40, 50, 60, 70

Value range:
`0
≤
high`

Minimum increment:
1

Recommended increment:
5

Restriction:
`High > 0 && High >= Low`

## Complexity

The amount of temporary memory required is dependent on the height H
of the domain of *`image`*.

## Result

`EdgesColorSubPix` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and no error occurs during execution. If the input is empty
the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Alternatives

`EdgesColor`

## See also

`EdgesImage`,
`EdgesSubPix`,
`InfoEdges`,
`HysteresisThreshold`,
`LinesGauss`,
`LinesFacet`

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

2D Metrology
