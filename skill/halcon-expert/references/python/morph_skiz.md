# morph_skiz (Operator)

## Name

`morph_skiz` — Thinning of a region.

## Warning

**`morph_skiz` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def morph_skiz(region: HObject, iterations_1: Union[int, str], iterations_2: Union[int, str]) -> HObject`

## Description

`morph_skiz` first performs a sequential thinning
([`thinning_seq`](thinning_seq.md)) of the input region with the element 'l'
of the Golay alphabet. The number of iterations is determined by
the parameter *`iterations_1`*. Then a sequential thinning of
the resulting region with the element 'e' of the Golay alphabet is
carried out. The number of iterations for this step is determined
by the parameter *`iterations_2`*. The skiz operation serves
to compute a kind of skeleton of the input regions, and to prune the
branches of the resulting skeleton. If the skiz operation is
applied to the complement of the region, the region and the
resulting skeleton are separated.

If very large values or 'maximal' are passed for
*`iterations_1`* or *`iterations_2`*, the processing
stops if no more changes occur.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be thinned.

**`region_skiz`** (output_object)  region(-array) `→` HObject

Result of the skiz operator.

**`iterations_1`** (input_control)  integer `→` Union[int, str]

Number of iterations for the sequential thinning
with the element 'l' of the Golay alphabet.

Default:
100

Suggested values:
"maximal", 0, 1, 2, 3, 5, 7, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200, 300, 400

Value range:
`0
≤
iterations_1` (lin)

Minimum increment:
1

Recommended increment:
1

**`iterations_2`** (input_control)  integer `→` Union[int, str]

Number of iterations for the sequential thinning
with the element 'e' of the Golay alphabet.

Default:
1

Suggested values:
"maximal", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

Value range:
`0
≤
iterations_2` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F be the area of the input region. Then the runtime
complexity for one region is
$$O\bigl(Iterations1 + Iterations2\bigr) \cdot 3 \cdot \sqrt{F}$$ ![figure](../assets/549663cb1a0a7244.svg)

## Result

`morph_skiz` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`pruning`,
`reduce_domain`,
`select_shape`,
`area_center`,
`connection`,
`background_seg`,
`complement`

## Alternatives

`skeleton`,
`thinning_seq`,
`morph_skeleton`,
`interjacent`

## See also

`thinning`,
`hit_or_miss_seq`,
`difference`

## Module

Foundation
