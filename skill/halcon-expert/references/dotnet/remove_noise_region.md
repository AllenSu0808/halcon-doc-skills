# RemoveNoiseRegion (Operator)

## Name

`RemoveNoiseRegion` — Remove noise from a region.

## Signature

`static void HOperatorSet.RemoveNoiseRegion(HObject inputRegion, out HObject outputRegion, HTuple type)`

`HRegion HRegion.RemoveNoiseRegion(string type)`

## Description

`RemoveNoiseRegion` removes noise from a region.
Depending on *`type`* one of the following structuring elements
will be used:

- ***"n_4"*** —

  A structuring element consisting of the four
  4-neighbors of a point is being used:
  .X.
  X.X
  .X.
- ***"n_8"*** —

  A structuring element consisting of the four
  8-neighbors of a point is being used:
  X.X
  ...
  X.X
- ***"n_48"*** —

  A structuring element consisting of the four
  4-neighbors and the four 8-neighbors of a point is being used:
  XXX
  X.X
  XXX

A dilation with this structuring element is
performed and the intersection of the result and the input region
is calculated. Thus, all pixels having no according neighbors are
removed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`inputRegion`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be modified.

**`outputRegion`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Less noisy regions.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of noise removal.

Default:
"n_4"

List of values:
"n_4", "n_48", "n_8"

## Complexity

Let F be the area of the input region. Then the runtime
complexity is $O\left(\sqrt{F}\ast 4\right).$ ![figure](../assets/d884bd007d29a388.svg)

## Result

`RemoveNoiseRegion` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Connection`,
`Regiongrowing`,
`Pouring`,
`ClassNdimNorm`

## Possible Successors

`SelectShape`

## See also

`Dilation1`,
`Intersection`,
`GenRegionPoints`

## Module

Foundation
