# fitting (Operator)

## Name

`fitting` — Perform a closing after an opening with multiple structuring elements.

## Warning

**`fitting` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def fitting(region: HObject, struct_elements: HObject) -> HObject`

## Description

`fitting` performs an [`opening`](opening.md) and a
[`closing`](closing.md) successively on the input regions. The eight
structuring elements normally used for this operation can be
generated with the operator [`gen_struct_elements`](gen_struct_elements.md). However,
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

**`region`** (input_object)  region(-array) `→` HObject

Regions to be processed.

**`struct_elements`** (input_object)  region(-array) `→` HObject

Structuring elements.

**`region_fitted`** (output_object)  region(-array) `→` HObject

Fitted regions.

## Result

`fitting` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`gen_struct_elements`,
`gen_region_points`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`opening`,
`closing`,
`connection`,
`select_shape`

## Module

Foundation
