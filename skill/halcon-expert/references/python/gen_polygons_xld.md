# gen_polygons_xld (Operator)

## Name

`gen_polygons_xld` — Approximate XLD contours by polygons.

## Signature

`def gen_polygons_xld(contours: HObject, type: str, alpha: Union[float, int]) -> HObject`

## Description

`gen_polygons_xld` approximates XLD contours
(*`contours`*) by polygons. The type of the approximation
can be set by *`type`*. The threshold for the approximation
is set via *`alpha`*. The procedure is able to process open
as well as closed contours. The resulting approximating XLD
polygons are returned in *`polygons`*.

Contours can be approximated by the algorithm of Ramer, which
approximates contours such that the Euclidean distance of the
approximating polygon to the contour is at most *`alpha`* pixel
units.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Contours to be approximated.

**`polygons`** (output_object)  xld_poly-array `→` HObject

Approximating polygons.

**`type`** (input_control)  string `→` str

Type of approximation.

Default:
"ramer"

List of values:
"ramer"

**`alpha`** (input_control)  number `→` Union[float, int]

Threshold for the approximation.

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 3.0, 4.0

Restriction:
`Alpha > 0.0`

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Possible Successors

`gen_parallels_xld`,
`split_contours_xld`

## See also

`get_region_polygon`

## Module

Foundation
