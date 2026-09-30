# RunlengthFeatures (Operator)

## Name

`RunlengthFeatures` — Characteristic values for runlength coding of regions.

## Signature

`static void HOperatorSet.RunlengthFeatures(HObject regions, out HTuple numRuns, out HTuple KFactor, out HTuple LFactor, out HTuple meanLength, out HTuple bytes)`

`HTuple HRegion.RunlengthFeatures(out HTuple KFactor, out HTuple LFactor, out HTuple meanLength, out HTuple bytes)`

`int HRegion.RunlengthFeatures(out double KFactor, out double LFactor, out double meanLength, out int bytes)`

## Description

The operator `RunlengthFeatures` calculates for every input region
from *`regions`* the number of runs necessary for storing
this region with the aid of runlength coding.
Furthermore the so-called “K-factor” is determined, which indicates
by how much the number of runs differs from the ideal of the square
in which this value is 1.0.

The K-factor (*`KFactor`*) is calculated according to the formula:
$$KFactor = \frac{NumRuns}{\sqrt{Area}}$$ ![figure](../assets/759bfd3afe0bc5f5.svg)
wherein Area indicates the area of the region.
It should be noted that the K-factor can be smaller than 1.0
(in case of long horizontal regions).

The L-factor (*`LFactor`*) indicates the mean number of runs
for each line index occurring in the region.

*`meanLength`* indicates the mean length of the runs.
The parameter *`bytes`* indicates how many bytes are
necessary for coding the region with runlengths.

## Attention

All features calculated by the operator `RunlengthFeatures` are not
rotation invariant because the runlength coding depends on the direction.
The operator `RunlengthFeatures` does not serve for calculating shape
features but for controlling and analyzing the efficiency of the
runlength coding.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`numRuns`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of runs.

Assertion:
`0 <= NumRuns`

**`KFactor`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Storing factor in relation to a square.

Assertion:
`0 <= KFactor`

**`LFactor`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Mean number of runs per line.

Assertion:
`0 <= LFactor`

**`meanLength`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Mean length of runs.

Assertion:
`0 <= MeanLength`

**`bytes`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of bytes necessary for coding the region.

Assertion:
`0 <= Bytes`

## Complexity

The mean runtime complexity is O(1).

## Result

The operator `RunlengthFeatures` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## See also

`RunlengthDistribution`

## Module

Foundation
