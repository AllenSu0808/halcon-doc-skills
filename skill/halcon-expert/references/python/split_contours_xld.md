# split_contours_xld (Operator)

## Name

`split_contours_xld` — Split XLD contours at dominant points.

## Signature

`def split_contours_xld(polygons: HObject, mode: str, weight: int, smooth: int) -> HObject`

## Description

`split_contours_xld` splits the contours which were used
to generate the polygons *`polygons`* at prominent points.
If the mode *"polygon"* is selected, the contours are split
at the polygons' control points. In mode *"dominant"*, they
are split at dominant points, i.e., at points for which the
calculated change of direction is larger than the (empirically
determined) threshold $2\pi\texttt{Weight}/\textit{contour length}$, and for which
in the (empirically determined) neighborhood of
$\sqrt{Smooth} \ast \log\left(Contour\ length\right)$ ![figure](../assets/272e8b6257112faf.svg) points
no larger change of direction occurs. The contour direction is
determined from the direction of the regression line (i.e., the
least-squares approximating line) through all points in a
neighborhood of *`smooth`* points around a contour point.
The directions thus determined are smoothed with a Gaussian of width
*`smooth`*. *`weight`* is a weighting factor for the
sensitiveness of the operator. The larger *`weight`* is
selected, the less dominant points are found.

Each polygon needs a reference to a contour. If the reference is missing,
because the polygon is e.g., read from a DXF-File, `split_contours_xld`
returns an error.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons`** (input_object)  xld_poly(-array) `→` HObject

Polygons for which the corresponding contours
are to be split.

**`contours`** (output_object)  xld_cont(-array) `→` HObject

Split contours.

**`mode`** (input_control)  string `→` str

Mode for the splitting of the contours.

Default:
"polygon"

List of values:
"dominant", "polygon"

**`weight`** (input_control)  integer `→` int

Weight for the sensitiveness.

Default:
1

**`smooth`** (input_control)  integer `→` int

Width of the smoothing mask.

Default:
5

## Possible Predecessors

`gen_polygons_xld`

## Possible Successors

`regress_contours_xld`

## See also

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Module

Foundation
