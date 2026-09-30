# select_matching_lines (Operator)

## Name

`select_matching_lines` — Select those lines from a set of lines (in HNF) which
fit best into a region.

## Signature

`select_matching_lines(RegionIn : RegionLines : AngleIn, DistIn, LineWidth, Thresh : AngleOut, DistOut)`

## Description

Lines which fit best into a region can be selected from a set of lines which
are available in HNF with the help of the operator
`select_matching_lines`; the region itself is also transmitted
as a parameter (*`RegionIn`*). The width of the lines can be
indicated by the parameter *`LineWidth`*. The selected lines will
be returned in HNF and as regions (*`RegionLines`*).

The lines are selected iteratively in a loop: At first, the line showing
the greatest overlap with the input region is selected from the set of
input lines. This line will then be taken over into the output set whereby
all points belonging to that line will not be considered in the further
steps determining overlaps. The loop will be left when the maximum overlap
value of the region and the lines falls below a certain threshold value
(*`Thresh`*). The selected lines will be returned
as regions as well as in HNF.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RegionIn`** (input_object)  region `→` object

Region in which the lines are to be matched.

**`RegionLines`** (output_object)  region(-array) `→` object

Region array containing the matched lines.

**`AngleIn`** (input_control)  hesseline.angle.rad(-array) `→`  (real)

Angles (in radians) of the normal vectors of the
input lines.

Value range:
`-1.5707963
≤
AngleIn
≤
3.1415927`

**`DistIn`** (input_control)  hesseline.distance(-array) `→`  (real)

Distances of the input lines form the origin.

Number of elements:
DistIn == AngleIn

**`LineWidth`** (input_control)  integer `→`  (integer)

Widths of the lines.

Default:
7

Value range:
`1
≤
LineWidth`

**`Thresh`** (input_control)  integer `→`  (integer)

Threshold value for the number of line points in
the region.

Default:
100

Value range:
`1
≤
Thresh`

**`AngleOut`** (output_control)  hesseline.angle.rad(-array) `→`  (real)

Angles (in radians) of the normal vectors of the
selected
lines.

Number of elements:
AngleOut <= AngleIn

Value range:
`-1.5707963
≤
AngleOut
≤
3.1415927`

**`DistOut`** (output_control)  hesseline.distance(-array) `→`  (real)

Distances of the selected lines from the origin.

Number of elements:
DistOut == AngleOut

Value range:
`0
≤
DistOut`

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
