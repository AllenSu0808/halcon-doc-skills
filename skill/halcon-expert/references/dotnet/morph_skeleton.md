# MorphSkeleton (Operator)

## Name

`MorphSkeleton` — Compute the morphological skeleton of a region.

## Warning

**`MorphSkeleton` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.MorphSkeleton(HObject region, out HObject regionSkeleton)`

`HRegion HRegion.MorphSkeleton()`

## Description

`MorphSkeleton` computes the skeleton of the input
regions (*`region`*) using morphological transformations.
The computation yields a disconnected skeleton (gaps in the
diagonals) having a width of one or two pixels. The calculation
uses the Golay element 'h', i.e., an 8-neighborhood. This is
equivalent to the maximum-norm.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be processed.

**`regionSkeleton`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Resulting morphological skeleton.

## Result

`MorphSkeleton` returns 2 (
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

`Threshold`,
`Regiongrowing`,
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`

## Possible Successors

`Skeleton`,
`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Skeleton`

## Module

Foundation
