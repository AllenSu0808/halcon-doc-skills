# close_contours_xld (Operator)

## Name

`close_contours_xld` — Close an XLD contour.

## Signature

`def close_contours_xld(contours: HObject) -> HObject`

## Description

`close_contours_xld` closes all XLD contours given in
*`contours`*. The resulting contours are returned in
*`closed_contours`*. To obtain meaningful results, it is strongly
recommended to select contours with [`select_contours_xld`](select_contours_xld.md) that have end
points that are not further apart than a certain maximum distance before
passing them to `close_contours_xld`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Contours to be closed.

**`closed_contours`** (output_object)  xld_cont(-array) `→` HObject

Closed contours.

## Possible Predecessors

`select_contours_xld`

## Possible Successors

`area_center_xld`,
`circularity_xld`,
`compactness_xld`,
`convexity_xld`,
`eccentricity_xld`,
`elliptic_axis_xld`,
`moments_xld`,
`moments_any_xld`,
`orientation_xld`,
`select_shape_xld`,
`test_xld_point`

## Module

Foundation
