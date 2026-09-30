# get_metrology_object_num_instances (Operator)

## Name

`get_metrology_object_num_instances` — Get the number of instances of the metrology objects of a metrology model.

## Signature

`def get_metrology_object_num_instances(metrology_handle: HHandle, index: MaybeSequence[Union[int, str]]) -> Sequence[Union[int, float]]`

`def get_metrology_object_num_instances_s(metrology_handle: HHandle, index: MaybeSequence[Union[int, str]]) -> Union[int, float]`

## Description

`get_metrology_object_num_instances` allows to access the number of
instances (results) of measurements applied by [`apply_metrology_model`](apply_metrology_model.md)
for the metrology objects. Note that by default, the maximum number of
instances of each metrology object is set to *1*. Thus, by default,
the result of `get_metrology_object_num_instances` will typically be
*1* as well. To allow more instances, before applying the measurement
with [`apply_metrology_model`](apply_metrology_model.md) you have to explicitly set the parameter
*"num_instances"* to a higher value or to *"all"* using
[`set_metrology_object_param`](set_metrology_object_param.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrology_handle`*. The
parameter *`index`* specifies for which metrology object the instances
are queried. For *`index`* set to *"all"*, the number of
instances of all metrology objects are returned. The number of instances is
returned in *`num_instances`* for each metrology object that was passed
in *`index`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Index of the metrology objects.

Default:
0

Suggested values:
"all", 0, 1, 2

**`num_instances`** (output_control)  integer(-array) `→` Sequence[Union[int, float]]

Number of Instances of the metrology objects.

## Result

If the parameters are valid, the operator
`get_metrology_object_num_instances` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`apply_metrology_model`

## Possible Successors

`clear_metrology_model`

## See also

`get_metrology_object_indices`

## Module

2D Metrology
