# runlength_distribution (Operator)

## Name

`runlength_distribution` — Distribution of runs needed for runlength encoding of a region.

## Signature

`def runlength_distribution(region: HObject) -> Tuple[Sequence[int], Sequence[int]]`

## Description

The operator `runlength_distribution` calculates the
distribution of the runs of a region of the fore- and
background. The frequency of the occurrence of a certain
length is calculated. Runs of infinite length are not counted.
Therefore the background are the holes of the region.
As many values are passed as set by the maximum
length of fore- or background, respectively.
The length of both tuples usually differs.
The first entry of the tuples is always 0
(no runs of the length 0).
If there are no blanks the empty tuple is passed
at *`background`*.
Analogously the empty tuple is passed in case
of an empty region at *`foreground`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Region to be examined.

**`foreground`** (output_control)  integer-array `→` Sequence[int]

Length distribution of the region (foreground).

**`background`** (output_control)  integer-array `→` Sequence[int]

Length distribution of the background.

## Complexity

If n is the number of runs of the region the runtime
complexity is O(n).

## Result

The operator `runlength_distribution` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If more than one region is passed an exception is raised.

## Possible Predecessors

`threshold`,
`select_obj`

## Alternatives

`runlength_features`

## See also

`runlength_features`

## Module

Foundation
