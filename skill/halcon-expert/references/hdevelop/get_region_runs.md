# get_region_runs (Operator)

## Name

`get_region_runs` — Access the runlength coding of a region.

## Signature

`get_region_runs(Region : : : Row, ColumnBegin, ColumnEnd)`

## Description

The operator `get_region_runs` returns the region data in the form of chord
tuples. The chord representation is caused by examining a region line by line with
ascending line number (= from “top” to “bottom”).
Every line is passed from left to right (ascending column number);
storing all starting and ending points of region segments (= chords).
Thus a region can be described by a sequence of chords, a chord being defined
by line number, starting and ending points (column number).
The operator `get_region_runs` returns the three components of the chords
in the form of tuples. In case of an empty region three empty tuples are returned.

## Attention

Only one region may be passed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

Output region.

**`Row`** (output_control)  chord.y-array `→`  (integer)

Line numbers of the chords.

**`ColumnBegin`** (output_control)  chord.x1-array `→`  (integer)

Column numbers of the starting points of the chords.

Number of elements:
ColumnBegin == Row

**`ColumnEnd`** (output_control)  chord.x2-array `→`  (integer)

Column numbers of the ending points of the chords.

Number of elements:
ColumnEnd == Row

## Result

The operator `get_region_runs` normally returns the value 2 (
H_MSG_TRUE)
.
If more than one region is passed an exception is raised.
The behavior in case of empty input (no input regions available) is set via
the operator `set_system('no_object_result',<Result>)`.

## Possible Predecessors

`threshold`,
`connection`

## Alternatives

`get_region_points`

## See also

`copy_obj`,
`gen_region_runs`

## Module

Foundation
