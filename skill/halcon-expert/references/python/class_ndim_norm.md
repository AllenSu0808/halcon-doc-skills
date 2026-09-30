# class_ndim_norm (Operator)

## Name

`class_ndim_norm` — Classify pixels using hyper-spheres or hyper-cubes.

## Signature

`def class_ndim_norm(multi_channel_image: HObject, metric: str, single_multiple: str, radius: MaybeSequence[Union[int, float]], center: MaybeSequence[Union[int, float]]) -> HObject`

## Description

`class_ndim_norm` classifies the pixels of the multi-channel
image given in *`multi_channel_image`*. The result is returned
in *`regions`* as one region per classification object. The
metric used (*"euclid"* or *"maximum"*) is determined by
*`metric`*. This parameter must be set to the same value used
in [`learn_ndim_norm`](learn_ndim_norm.md). The parameter *`single_multiple`*
determines whether one region (*"single"*) or multiples regions
(*"multiple"*) are generated for each cluster.
*`radius`* determines the
radii or half edge length of the clusters, respectively.
*`center`* determines their centers.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`multi_channel_image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte)

Multi channel input image.

**`regions`** (output_object)  region-array `→` HObject

Classification result.

**`metric`** (input_control)  string `→` str

Metric to be used.

Default:
"euclid"

List of values:
"euclid", "maximum"

**`single_multiple`** (input_control)  string `→` str

Return one region or one region for each cluster.

Default:
"single"

List of values:
"multiple", "single"

**`radius`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Cluster radii or half edge lengths (returned by
[`learn_ndim_norm`](learn_ndim_norm.md)).

**`center`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Coordinates of the cluster centers (returned by
[`learn_ndim_norm`](learn_ndim_norm.md)).

## Complexity

Let N be the number of clusters and A be the area of the input
region. Then the runtime complexity is O(N,A).

## Result

`class_ndim_norm` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`learn_ndim_norm`,
`compose2`,
`compose3`,
`compose4`,
`compose5`,
`compose6`,
`compose7`

## Possible Successors

`connection`,
`select_shape`,
`reduce_domain`,
`select_gray`

## Alternatives

`class_2dim_sup`,
`class_2dim_unsup`

## Module

Foundation
