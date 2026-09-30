# DifferenceClosedContoursXld (Operator)

## Name

`DifferenceClosedContoursXld` — Compute the difference of closed contours.

## Signature

`static void HOperatorSet.DifferenceClosedContoursXld(HObject contours, HObject sub, out HObject contoursDifference)`

`HXLDCont HXLDCont.DifferenceClosedContoursXld(HXLDCont sub)`

## Description

The operator `DifferenceClosedContoursXld` calculates the difference
of the regions enclosed by the contours *`contours`* and *`sub`*.
The boundaries of this difference are returned in
*`contoursDifference`*.

If the individual input contours are not closed, they are closed
automatically by connecting their start and end points.

Internally, first, the regions enclosed by each set of contours
(*`contours`* and *`sub`*, respectively) are determined as
described below. Then, the difference of these two regions is calculated.

In the following, the two sets of input contours are referred to as
*boundary sets*. A boundary set consists of an arbitrary number of
boundaries (the individual contours of *`contours`* and *`sub`*,
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

The resulting boundaries *`contoursDifference`* are automatically
classified into boundaries that enclose regions and boundaries that enclose
holes. This information is stored in the global contour attribute
*"is_hole"*.
For further information about global contour attributes see
[`GetContourGlobalAttribXld`](get_contour_global_attrib_xld.md).

Note that subsequent points whose row and column coordinates differ by
less than 1e-06 pixels are considered as one point.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours enclosing the region from which the second
region is subtracted.

**`sub`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours enclosing the region that is subtracted from
the first region.

**`contoursDifference`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours enclosing the difference.

## Result

`DifferenceClosedContoursXld` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`GenContourRegionXld`,
`ZeroCrossingSubPix`,
`ThresholdSubPix`

## Alternatives

`Difference`

## See also

`IntersectionClosedContoursXld`,
`SymmDifferenceClosedContoursXld`,
`Union2ClosedContoursXld`,
`DifferenceClosedPolygonsXld`

## Module

Foundation
