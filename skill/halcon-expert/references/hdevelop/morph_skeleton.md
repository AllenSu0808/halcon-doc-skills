# morph_skeleton (Operator)

## Name

`morph_skeleton` — Compute the morphological skeleton of a region.

## Warning

**`morph_skeleton` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`morph_skeleton(Region : RegionSkeleton : : )`

## Description

`morph_skeleton` computes the skeleton of the input
regions (*`Region`*) using morphological transformations.
The computation yields a disconnected skeleton (gaps in the
diagonals) having a width of one or two pixels. The calculation
uses the Golay element 'h', i.e., an 8-neighborhood. This is
equivalent to the maximum-norm.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`RegionSkeleton`** (output_object)  region(-array) `→` object

Resulting morphological skeleton.

## Result

`morph_skeleton` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

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

`skeleton`,
`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`skeleton`

## Module

Foundation
