# SymmDifferenceClosedPolygonsXld (Operator)

## Name

`SymmDifferenceClosedPolygonsXld` — Compute the symmetric difference of closed polygons.

## Signature

`static void HOperatorSet.SymmDifferenceClosedPolygonsXld(HObject polygons1, HObject polygons2, out HObject polygonsDifference)`

`HXLDPoly HXLDPoly.SymmDifferenceClosedPolygonsXld(HXLDPoly polygons2)`

## Description

The operator `SymmDifferenceClosedPolygonsXld` calculates the
symmetric difference of the regions enclosed by the polygons
*`polygons1`* and *`polygons2`*. The boundaries of this symmetric
difference are returned in *`polygonsDifference`*.

If the individual input polygons are not closed, they are closed
automatically by connecting their start and end points.

Internally, first, the regions enclosed by each set of polygons
(*`polygons1`* and *`polygons2`*, respectively) are determined as
described below. Then, the symmetric difference of these two regions is
calculated.

In the following, the two sets of input polygons are referred to as
*boundary sets*. A boundary set consists of an arbitrary number of
boundaries (the individual polygons of *`polygons1`* and
*`polygons2`*, respectively). Each boundary may be convex or concave and
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

The resulting polygons *`polygonsDifference`* contain no references to
the XLD contours that are possibly referenced by *`polygons1`* and
*`polygons2`*. Hence, operators that access the contours associated with
a polygon, e.g., [`SplitContoursXld`](split_contours_xld.md) will not work correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons1`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Polygons enclosing the first region.

**`polygons2`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Polygons enclosing the second region.

**`polygonsDifference`** (output_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Polygons enclosing the symmetric difference.

## Result

`SymmDifferenceClosedPolygonsXld` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`GenPolygonsXld`

## Alternatives

`SymmDifference`

## See also

`IntersectionClosedPolygonsXld`,
`DifferenceClosedPolygonsXld`,
`Union2ClosedPolygonsXld`,
`SymmDifferenceClosedContoursXld`

## Module

Foundation
