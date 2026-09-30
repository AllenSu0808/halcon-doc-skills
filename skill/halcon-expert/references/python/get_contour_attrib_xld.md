# get_contour_attrib_xld (Operator)

## Name

`get_contour_attrib_xld` — Return point attribute values of an XLD contour.

## Signature

`def get_contour_attrib_xld(contour: HObject, name: str) -> Sequence[float]`

## Description

`get_contour_attrib_xld` returns the values of the
attribute *`name`* of the XLD contour *`contour`* in
*`attrib`*. Contour point attributes are additional values defined for
each contour point and describe local features.
[`query_contour_attribs_xld`](query_contour_attribs_xld.md) can be used to query which
attributes are set for a particular contour.

The following list contains information about the different contour point
attributes and the operators that add them to XLD contours (for exceptions
see the respective operator references):

- ***"angle"*** —

  The direction of the normal vectors of the contour is
  described by *"angle"* [rad] (see image below).
  It is oriented such that the normal vectors point to the right
  side of the contour as the contour is traversed from start to end point
  (the angles are defined counterclockwise with respect to the row
  axis of the image).

  The attribute *"angle"* is added by the following
  operators:

  [`edges_color_sub_pix`](edges_color_sub_pix.md), [`edges_sub_pix`](edges_sub_pix.md),
  [`lines_color`](lines_color.md), [`lines_facet`](lines_facet.md), [`lines_gauss`](lines_gauss.md)
- ***"response"*** —

  *"response"* contains the magnitude of the edge gradient
  (see image below).

  The attribute *"response"* is added by the following
  operators:

  [`edges_color_sub_pix`](edges_color_sub_pix.md), [`edges_sub_pix`](edges_sub_pix.md),
  [`lines_color`](lines_color.md), [`lines_facet`](lines_facet.md), [`lines_gauss`](lines_gauss.md)
- ***"width_right"*** —

  The line width to the right of the line (as the contour is
  traversed from start to end point) is described by
  *"width_right"* [px] (see image below).

  The attribute *"width_right"* is added by the following
  operators:

  [`lines_color`](lines_color.md), [`lines_gauss`](lines_gauss.md)
- ***"width_left"*** —

  The line width to the left of the line (as the contour is
  traversed from start to end point) is described by
  *"width_left"* [px] (see image below).

  The attribute *"width_left"* is added by the following
  operators:

  [`lines_color`](lines_color.md), [`lines_gauss`](lines_gauss.md)

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/fdf250b77833af98.svg) | ![figure](../assets/9bba03e68693948c.svg) | ![figure](../assets/f4d799dc3ac28bcb.svg) |
  | ( 1) | ( 2) | ( 3) |

  Visualization of different point attributes of a contour
  (red). The starting point of the contour is marked with a
  white cross.
  (1) Vectors (yellow), plotted at *"angle"* (with respect
  to the row axis), representing the normal for every point
  of the contour,
  (2) behavior of the attribute *"response"* along a
  contour, and
  (3) visualization of the calculated attributes
  *"width_right"* (yellow) and *"width_left"*
  (green).
- ***"edge_direction"*** —

  Gives the direction of the edge (not of the XLD contour), calculated
  from image gradients in direction of rows and columns.
  The angles are given with respect to the column axis of the image.

  The attribute *"edge_direction"* [rad] is added by the following
  operators:

  [`edges_color_sub_pix`](edges_color_sub_pix.md), [`edges_sub_pix`](edges_sub_pix.md)

  ![figure](../assets/6ab0f6a8a91b72ec.svg)

  Vectors plotted in *"edge_direction"* (yellow) for every
  point of a contour (red).
- ***"asymmetry"*** —

  The contour attribute *"asymmetry"* describes the image gradient
  on both sides of the edge. It is positive if the asymmetric part, i.e.,
  the part with the weaker gradient, is on the right side of the line,
  while it is negative if the asymmetric part is on the left side of
  the line (see image below).

  The attribute *"asymmetry"* is added by the following operator:

  [`lines_gauss`](lines_gauss.md)
- ***"contrast"*** —

  The contrast of a contour describes the difference between the gray
  values of the line and the gray values of the local background.
  It is positive if bright lines are extracted, while it is negative for
  dark lines (see image below).

  The attribute *"contrast"* is added by the following operator:

  [`lines_gauss`](lines_gauss.md)

  |  |
  | --- |
  | ![figure](../assets/60866ef3561a87f1.svg) |
  | ( 1) |
  | ![figure](../assets/eb38b5d4e23e4ecf.svg) |
  | ( 2) |

  behavior of the attributes (1) *"asymmetry"* and (2)
  *"contrast"* for a contour along an image structure (the
  starting point of the contour is marked with a white cross).
- ***"distance"*** —

  The minimum distance to any point or segment of the reference
  contour (depending on the mode chosen for the calculation) is given
  in the attribute *"distance"* [px] for all points of a contour.

  The attribute *"distance"* is added by the following
  operators:

  [`apply_distance_transform_xld`](apply_distance_transform_xld.md), [`distance_contours_xld`](distance_contours_xld.md)

  |  |  |
  | --- | --- |
  | ![figure](../assets/b055b9ae305e2e0e.svg) | ![figure](../assets/c9e9b219bc578757.svg) |
  | ( 1) | ( 2) |

  (1) *"distance"* of a contour (red) to the
  points of a reference contour (green) and
  (2) *"distance"* to any segment of a reference contour
  (green).

For information about global contour attributes see the operator reference
of [`get_contour_global_attrib_xld`](get_contour_global_attrib_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input XLD contour.

**`name`** (input_control)  string `→` str

Name of the attribute.

Default:
"angle"

Suggested values:
"angle", "edge_direction", "width_right", "width_left", "response", "contrast", "asymmetry", "distance"

**`attrib`** (output_control)  real-array `→` Sequence[float]

Attribute values.

## Possible Predecessors

`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`distance_contours_xld`,
`apply_distance_transform_xld`

## See also

`query_contour_attribs_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`

## Module

Foundation
