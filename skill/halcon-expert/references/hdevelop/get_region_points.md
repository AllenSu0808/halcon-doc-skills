# get_region_points (Operator)

## Name

`get_region_points` — Access the pixels of a region.

## Signature

`get_region_points(Region : : : Rows, Columns)`

## Description

The operator `get_region_points` returns the region data in the form
of coordinate lists. The coordinates are sorted in the following
order:

$$(r_{1},c_{1})\le(r_{2},c_{2}):=(r_{1}<r_{2})\vee(r_{1}=r_{2})\wedge(c1\le c2)$$
`get_region_points` returns the coordinates in the form of tuples.
An empty region is passed as empty tuple.

## Attention

Only one region may be passed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

This region is accessed.

**`Rows`** (output_control)  coordinates.y-array `→`  (integer)

Line numbers of the pixels in the region

**`Columns`** (output_control)  coordinates.x-array `→`  (integer)

Column numbers of the pixels in the region.

Number of elements:
Columns == Rows

## Result

The operator `get_region_points` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one connection component is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`sobel_amp`,
`threshold`,
`connection`

## Alternatives

`get_region_runs`

## See also

`copy_obj`,
`gen_region_points`

## Module

Foundation
