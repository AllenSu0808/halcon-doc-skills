# SelectMatchingLines (Operator)

## Name

`SelectMatchingLines` — Select those lines from a set of lines (in HNF) which
fit best into a region.

## Signature

`static void HOperatorSet.SelectMatchingLines(HObject regionIn, out HObject regionLines, HTuple angleIn, HTuple distIn, HTuple lineWidth, HTuple thresh, out HTuple angleOut, out HTuple distOut)`

`HRegion HRegion.SelectMatchingLines(HTuple angleIn, HTuple distIn, int lineWidth, int thresh, out HTuple angleOut, out HTuple distOut)`

`HRegion HRegion.SelectMatchingLines(double angleIn, double distIn, int lineWidth, int thresh, out double angleOut, out double distOut)`

## Description

Lines which fit best into a region can be selected from a set of lines which
are available in HNF with the help of the operator
`SelectMatchingLines`; the region itself is also transmitted
as a parameter (*`regionIn`*). The width of the lines can be
indicated by the parameter *`lineWidth`*. The selected lines will
be returned in HNF and as regions (*`regionLines`*).

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

**`regionIn`** (input_object)  region `→` [HRegion](HRegion.md)

Region in which the lines are to be matched.

**`regionLines`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Region array containing the matched lines.

**`angleIn`** (input_control)  hesseline.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angles (in radians) of the normal vectors of the
input lines.

Value range:
`-1.5707963
≤
angleIn
≤
3.1415927`

**`distIn`** (input_control)  hesseline.distance(-array) `→` [HTuple](HTuple.md) (*double*)

Distances of the input lines form the origin.

Number of elements:
DistIn == AngleIn

**`lineWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Widths of the lines.

Default:
7

Value range:
`1
≤
lineWidth`

**`thresh`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Threshold value for the number of line points in
the region.

Default:
100

Value range:
`1
≤
thresh`

**`angleOut`** (output_control)  hesseline.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angles (in radians) of the normal vectors of the
selected
lines.

Number of elements:
AngleOut <= AngleIn

Value range:
`-1.5707963
≤
angleOut
≤
3.1415927`

**`distOut`** (output_control)  hesseline.distance(-array) `→` [HTuple](HTuple.md) (*double*)

Distances of the selected lines from the origin.

Number of elements:
DistOut == AngleOut

Value range:
`0
≤
distOut`

## Result

The operator `SelectMatchingLines` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`HoughLines`

## Module

Foundation
