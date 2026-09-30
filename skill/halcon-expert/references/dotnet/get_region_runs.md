# GetRegionRuns (Operator)

## Name

`GetRegionRuns` — Access the runlength coding of a region.

## Signature

`static void HOperatorSet.GetRegionRuns(HObject region, out HTuple row, out HTuple columnBegin, out HTuple columnEnd)`

`void HRegion.GetRegionRuns(out HTuple row, out HTuple columnBegin, out HTuple columnEnd)`

## Description

The operator `GetRegionRuns` returns the region data in the form of chord
tuples. The chord representation is caused by examining a region line by line with
ascending line number (= from “top” to “bottom”).
Every line is passed from left to right (ascending column number);
storing all starting and ending points of region segments (= chords).
Thus a region can be described by a sequence of chords, a chord being defined
by line number, starting and ending points (column number).
The operator `GetRegionRuns` returns the three components of the chords
in the form of tuples. In case of an empty region three empty tuples are returned.

## Attention

Only one region may be passed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Output region.

**`row`** (output_control)  chord.y-array `→` [HTuple](HTuple.md) (*int* / long)

Line numbers of the chords.

**`columnBegin`** (output_control)  chord.x1-array `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of the starting points of the chords.

Number of elements:
ColumnBegin == Row

**`columnEnd`** (output_control)  chord.x2-array `→` [HTuple](HTuple.md) (*int* / long)

Column numbers of the ending points of the chords.

Number of elements:
ColumnEnd == Row

## Result

The operator `GetRegionRuns` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one region is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`Threshold`,
`Connection`

## Alternatives

`GetRegionPoints`

## See also

`CopyObj`,
`GenRegionRuns`

## Module

Foundation
