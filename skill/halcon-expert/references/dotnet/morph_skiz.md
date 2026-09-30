# MorphSkiz (Operator)

## Name

`MorphSkiz` — Thinning of a region.

## Warning

**`MorphSkiz` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.MorphSkiz(HObject region, out HObject regionSkiz, HTuple iterations1, HTuple iterations2)`

`HRegion HRegion.MorphSkiz(HTuple iterations1, HTuple iterations2)`

`HRegion HRegion.MorphSkiz(int iterations1, int iterations2)`

## Description

`MorphSkiz` first performs a sequential thinning
([`ThinningSeq`](thinning_seq.md)) of the input region with the element 'l'
of the Golay alphabet. The number of iterations is determined by
the parameter *`iterations1`*. Then a sequential thinning of
the resulting region with the element 'e' of the Golay alphabet is
carried out. The number of iterations for this step is determined
by the parameter *`iterations2`*. The skiz operation serves
to compute a kind of skeleton of the input regions, and to prune the
branches of the resulting skeleton. If the skiz operation is
applied to the complement of the region, the region and the
resulting skeleton are separated.

If very large values or 'maximal' are passed for
*`iterations1`* or *`iterations2`*, the processing
stops if no more changes occur.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be thinned.

**`regionSkiz`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the skiz operator.

**`iterations1`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Number of iterations for the sequential thinning
with the element 'l' of the Golay alphabet.

Default:
100

Suggested values:
"maximal", 0, 1, 2, 3, 5, 7, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200, 300, 400

Value range:
`0
≤
iterations1` (lin)

Minimum increment:
1

Recommended increment:
1

**`iterations2`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Number of iterations for the sequential thinning
with the element 'e' of the Golay alphabet.

Default:
1

Suggested values:
"maximal", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

Value range:
`0
≤
iterations2` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F be the area of the input region. Then the runtime
complexity for one region is
$$O\bigl(Iterations1 + Iterations2\bigr) \cdot 3 \cdot \sqrt{F}$$ ![figure](../assets/549663cb1a0a7244.svg)

## Result

`MorphSkiz` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`

## Possible Successors

`Pruning`,
`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`,
`BackgroundSeg`,
`Complement`

## Alternatives

`Skeleton`,
`ThinningSeq`,
`MorphSkeleton`,
`Interjacent`

## See also

`Thinning`,
`HitOrMissSeq`,
`Difference`

## Module

Foundation
