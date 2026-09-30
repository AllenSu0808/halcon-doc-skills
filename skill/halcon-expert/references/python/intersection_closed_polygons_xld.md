# intersection_closed_polygons_xld (Operator)

## Name

`intersection_closed_polygons_xld` — Intersect closed polygons.

## Signature

`def intersection_closed_polygons_xld(polygons_1: HObject, polygons_2: HObject) -> HObject`

## Description

The operator `intersection_closed_polygons_xld` calculates the
intersection of the regions enclosed by the polygons *`polygons_1`* and
*`polygons_2`*. The boundaries of this intersection are returned in
*`polygons_intersection`*.

If the individual input polygons are not closed, they are closed
automatically by connecting their start and end points.

Internally, first, the regions enclosed by each set of polygons
(*`polygons_1`* and *`polygons_2`*, respectively) are determined as
described below. Then, the intersection of these two regions is calculated.

In the following, the two sets of input polygons are referred to as
*boundary sets*. A boundary set consists of an arbitrary number of
boundaries (the individual polygons of *`polygons_1`* and
*`polygons_2`*, respectively). Each boundary may be convex or concave and
self-intersecting. Internal holes may be formed by the nesting of boundaries.

The region enclosed by such a boundary set is defined by the so-called
Even-Odd-Rule. Thus, it consists of all points with the following property:
The line constructed by connecting the point with another reference point
that lies outside of the region has an odd number of intersections with
boundaries.

More descriptive, this means that a boundary defines a hole in the region
enclosed by another boundary if it lies completely inside that region.
Similarly, the overlapping area of two separate boundaries of one boundary
set is taken as a "hole", i.e., it does not belong to the region enclosed by
the two boundaries. Note that the region enclosed by a boundary does not
depend on the orientation of the boundary.

A self-intersecting boundary may be split at the intersection
point or it is reordered such that it touches itself at the intersection
point. The resulting boundaries are treated as separate boundaries.

## Attention

The resulting polygons *`polygons_intersection`* contain no references to
the XLD contours that are possibly referenced by *`polygons_1`* and
*`polygons_2`*. Hence, operators that access the contours associated with
a polygon, e.g., [`split_contours_xld`](split_contours_xld.md) will not work correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons_1`** (input_object)  xld_poly(-array) `→` HObject

Polygons enclosing the first region to be intersected.

**`polygons_2`** (input_object)  xld_poly(-array) `→` HObject

Polygons enclosing the second region to be
intersected.

**`polygons_intersection`** (output_object)  xld_poly(-array) `→` HObject

Polygons enclosing the intersection.

## Result

`intersection_closed_polygons_xld` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`gen_polygons_xld`

## Alternatives

`intersection`

## See also

`difference_closed_polygons_xld`,
`symm_difference_closed_polygons_xld`,
`union2_closed_polygons_xld`,
`intersection_closed_contours_xld`

## Module

Foundation
