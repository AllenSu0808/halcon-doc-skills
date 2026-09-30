# Fitting (Operator)

## Name

`Fitting` — Perform a closing after an opening with multiple structuring elements.

## Warning

**`Fitting` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.Fitting(HObject region, HObject structElements, out HObject regionFitted)`

`HRegion HRegion.Fitting(HRegion structElements)`

## Description

`Fitting` performs an [`Opening`](opening.md) and a
[`Closing`](closing.md) successively on the input regions. The eight
structuring elements normally used for this operation can be
generated with the operator [`GenStructElements`](gen_struct_elements.md). However,
other user-defined structuring elements can also be used. Let
R be the input region(s) and let $M_{i}$ denote the
structuring elements. Furthermore, let P be the result of the
opening and Q be the final result. Then the operator can be
formalized as follows:
$$P = \bigcup_{i=1}^{n}(R_{i}M_{i}) \\\nQ = \bigcap_{i=1}^{n}(P \cdot M_{i})$$ ![figure](../assets/cecf07cd39307ffd.svg)
Regions larger than the structuring elements are preserved, while
small gaps are closed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`structElements`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Structuring elements.

**`regionFitted`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Fitted regions.

## Result

`Fitting` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`GenStructElements`,
`GenRegionPoints`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Opening`,
`Closing`,
`Connection`,
`SelectShape`

## Module

Foundation
