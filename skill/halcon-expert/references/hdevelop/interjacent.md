# interjacent (Operator)

## Name

`interjacent` — Partition the image plane using given regions.

## Warning

**`interjacent` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`interjacent(Region : RegionInterjacent : Mode : )`

## Description

`interjacent` partitions the image plane using the regions
given in *`Region`*. The result is a region containing the
extracted separating lines. The following modes of operation can be
used:

- ***'medial_axis'*** —

  This mode is used for regions that do not touch or overlap.
  The operator will find separating lines between the regions
  which partition the background evenly between the input
  regions. This corresponds to the following calls:

  - **Example:** —

    `complement('full',Region,Tmp)`

    `skeleton(Tmp,Result)`
- ***'border'*** —

  If the input regions do not touch or overlap this mode is
  equivalent to `boundary(Region,Result)`, i.e., it
  replaces each region by its boundary. If regions are touching
  they are aggregated into one region. The corresponding output
  region then contains the boundary of the aggregated region, as
  well as the one pixel wide separating line between the
  original regions. This corresponds to the following calls:

  - **Example:** —

    `boundary(Region,Tmp1,'inner')`

    `union1(Tmp1,Tmp2)`

    `skeleton(Tmp2,Result)`
- ***'mixed'*** —

  In this mode the operator behaves like the mode *'medial_axis'*
  for non-overlapping regions. If regions touch or overlap,
  again separating lines between the input regions are generated
  on output, but this time including the “touching line”
  between regions, i.e., touching regions are separated by a
  line in the output region. This corresponds to the following
  calls:

  - **Example:** —

    `erosion1(Region,Mask,Tmp1,1)`

    `union1(Tmp1,Tmp2)`

    `complement(full,Tmp2,Tmp3)`

    `skeleton(Tmp3,Result)`

  where Mask denotes the following “cross mask”:
  ![figure](../assets/2523cea1067b8be5.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions for which the separating lines are to be
determined.

**`RegionInterjacent`** (output_object)  region `→` object

Output region containing the separating lines.

**`Mode`** (input_control)  string `→`  (string)

Mode of operation.

Default:
'mixed'

List of values:
'border', 'medial_axis', 'mixed'

## Example (HDevelop)

```
read_image(Image,'forest_air1')
mean_image(Image,Mean,31,31)
dyn_threshold(Image,Mean,Seg,20,'light')
interjacent(Seg,Graph,'medial_axis')
dev_display(Graph)
```

## Result

`interjacent` always returns the value 2 (
H_MSG_TRUE)
. The behavior
in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## See also

`expand_region`,
`junctions_skeleton`,
`boundary`

## Module

Foundation
