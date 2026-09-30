# DifferenceClosedPolygonsXld (Operator)

## Name

`DifferenceClosedPolygonsXld` — Compute the difference of closed polygons.

## Signature

`static void HOperatorSet.DifferenceClosedPolygonsXld(HObject polygons, HObject sub, out HObject polygonsDifference)`

`HXLDPoly HXLDPoly.DifferenceClosedPolygonsXld(HXLDPoly sub)`

## Description

The operator `DifferenceClosedPolygonsXld` calculates the difference
of the regions enclosed by the polygons *`polygons`* and *`sub`*.
The boundaries of this difference are returned in
*`polygonsDifference`*.

If the individual input polygons are not closed, they are closed
automatically by connecting their start and end points.

Internally, first, the regions enclosed by each set of polygons
(*`polygons`* and *`sub`*, respectively) are determined as
described below. Then, the difference of these two regions is calculated.

In the following, the two sets of input polygons are referred to as
*boundary sets*. A boundary set consists of an arbitrary number of
boundaries (the individual polygons of *`polygons`* and *`sub`*,
respectively). Each boundary may be convex or concave and self-intersecting.
Internal holes may be formed by the nesting of boundaries.

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

The resulting polygons *`polygonsDifference`* contain no references to
the XLD contours that are possibly referenced by *`polygons`* and
*`sub`*. Hence, operators that access the contours associated with
a polygon, e.g., [`SplitContoursXld`](split_contours_xld.md) will not work correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Polygons enclosing the region from which the second
region is subtracted.

**`sub`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Polygons enclosing the region that is subtracted from
the first region.

**`polygonsDifference`** (output_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Polygons enclosing the difference.

## Result

`DifferenceClosedPolygonsXld` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`GenPolygonsXld`

## Alternatives

`Difference`

## See also

`IntersectionClosedPolygonsXld`,
`SymmDifferenceClosedPolygonsXld`,
`Union2ClosedPolygonsXld`,
`DifferenceClosedContoursXld`

## Module

Foundation
