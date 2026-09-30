# runlength_features (Operator)

## Name

`runlength_features` — Characteristic values for runlength coding of regions.

## Signature

`runlength_features(Regions : : : NumRuns, KFactor, LFactor, MeanLength, Bytes)`

## Description

The operator `runlength_features` calculates for every input region
from *`Regions`* the number of runs necessary for storing
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

*`MeanLength`* indicates the mean length of the runs.
The parameter *`Bytes`* indicates how many bytes are
necessary for coding the region with runlengths.

## Attention

All features calculated by the operator `runlength_features` are not
rotation invariant because the runlength coding depends on the direction.
The operator `runlength_features` does not serve for calculating shape
features but for controlling and analyzing the efficiency of the
runlength coding.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`NumRuns`** (output_control)  integer(-array) `→`  (integer)

Number of runs.

Assertion:
`0 <= NumRuns`

**`KFactor`** (output_control)  real(-array) `→`  (real)

Storing factor in relation to a square.

Assertion:
`0 <= KFactor`

**`LFactor`** (output_control)  real(-array) `→`  (real)

Mean number of runs per line.

Assertion:
`0 <= LFactor`

**`MeanLength`** (output_control)  real(-array) `→`  (real)

Mean length of runs.

Assertion:
`0 <= MeanLength`

**`Bytes`** (output_control)  integer(-array) `→`  (integer)

Number of bytes necessary for coding the region.

Assertion:
`0 <= Bytes`

## Complexity

The mean runtime complexity is O(1).

## Result

The operator `runlength_features` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## See also

`runlength_distribution`

## Module

Foundation
