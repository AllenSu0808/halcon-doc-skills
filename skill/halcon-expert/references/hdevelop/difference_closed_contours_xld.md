# difference_closed_contours_xld (Operator)

## Name

`difference_closed_contours_xld` — Compute the difference of closed contours.

## Signature

`difference_closed_contours_xld(Contours, Sub : ContoursDifference : : )`

## Description

The operator `difference_closed_contours_xld` calculates the difference
of the regions enclosed by the contours *`Contours`* and *`Sub`*.
The boundaries of this difference are returned in
*`ContoursDifference`*.

If the individual input contours are not closed, they are closed
automatically by connecting their start and end points.

Internally, first, the regions enclosed by each set of contours
(*`Contours`* and *`Sub`*, respectively) are determined as
described below. Then, the difference of these two regions is calculated.

In the following, the two sets of input contours are referred to as
*boundary sets*. A boundary set consists of an arbitrary number of
boundaries (the individual contours of *`Contours`* and *`Sub`*,
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

The resulting boundaries *`ContoursDifference`* are automatically
classified into boundaries that enclose regions and boundaries that enclose
holes. This information is stored in the global contour attribute
*'is_hole'*.
For further information about global contour attributes see
[`get_contour_global_attrib_xld`](get_contour_global_attrib_xld.md).

Note that subsequent points whose row and column coordinates differ by
less than 1e-06 pixels are considered as one point.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Contours enclosing the region from which the second
region is subtracted.

**`Sub`** (input_object)  xld_cont(-array) `→` object

Contours enclosing the region that is subtracted from
the first region.

**`ContoursDifference`** (output_object)  xld_cont(-array) `→` object

Contours enclosing the difference.

## Result

`difference_closed_contours_xld` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`gen_contour_region_xld`,
`zero_crossing_sub_pix`,
`threshold_sub_pix`

## Alternatives

`difference`

## See also

`intersection_closed_contours_xld`,
`symm_difference_closed_contours_xld`,
`union2_closed_contours_xld`,
`difference_closed_polygons_xld`

## Module

Foundation
