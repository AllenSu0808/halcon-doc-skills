# select_matching_lines (Operator)

## Name

`select_matching_lines` — Select those lines from a set of lines (in HNF) which
fit best into a region.

## Signature

`def select_matching_lines(region_in: HObject, angle_in: MaybeSequence[float], dist_in: MaybeSequence[float], line_width: int, thresh: int) -> Tuple[HObject, Sequence[float], Sequence[float]]`

`def select_matching_lines_s(region_in: HObject, angle_in: MaybeSequence[float], dist_in: MaybeSequence[float], line_width: int, thresh: int) -> Tuple[HObject, float, float]`

## Description

Lines which fit best into a region can be selected from a set of lines which
are available in HNF with the help of the operator
`select_matching_lines`; the region itself is also transmitted
as a parameter (*`region_in`*). The width of the lines can be
indicated by the parameter *`line_width`*. The selected lines will
be returned in HNF and as regions (*`region_lines`*).

The lines are selected iteratively in a loop: At first, the line showing
the greatest overlap with the input region is selected from the set of
input lines. This line will then be taken over into the output set whereby
all points belonging to that line will not be considered in the further
steps determining overlaps. The loop will be left when the maximum overlap
value of the region and the lines falls below a certain threshold value
(*`thresh`*). The selected lines will be returned
as regions as well as in HNF.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_in`** (input_object)  region `→` HObject

Region in which the lines are to be matched.

**`region_lines`** (output_object)  region(-array) `→` HObject

Region array containing the matched lines.

**`angle_in`** (input_control)  hesseline.angle.rad(-array) `→` MaybeSequence[float]

Angles (in radians) of the normal vectors of the
input lines.

Value range:
`-1.5707963
≤
angle_in
≤
3.1415927`

**`dist_in`** (input_control)  hesseline.distance(-array) `→` MaybeSequence[float]

Distances of the input lines form the origin.

Number of elements:
DistIn == AngleIn

**`line_width`** (input_control)  integer `→` int

Widths of the lines.

Default:
7

Value range:
`1
≤
line_width`

**`thresh`** (input_control)  integer `→` int

Threshold value for the number of line points in
the region.

Default:
100

Value range:
`1
≤
thresh`

**`angle_out`** (output_control)  hesseline.angle.rad(-array) `→` Sequence[float]

Angles (in radians) of the normal vectors of the
selected
lines.

Number of elements:
AngleOut <= AngleIn

Value range:
`-1.5707963
≤
angle_out
≤
3.1415927`

**`dist_out`** (output_control)  hesseline.distance(-array) `→` Sequence[float]

Distances of the selected lines from the origin.

Number of elements:
DistOut == AngleOut

Value range:
`0
≤
dist_out`

## Result

The operator `select_matching_lines` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`hough_lines`

## Module

Foundation
