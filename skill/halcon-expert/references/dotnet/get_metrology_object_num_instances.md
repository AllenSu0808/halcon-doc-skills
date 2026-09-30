# GetMetrologyObjectNumInstances (Operator)

## Name

`GetMetrologyObjectNumInstances` — Get the number of instances of the metrology objects of a metrology model.

## Signature

`static void HOperatorSet.GetMetrologyObjectNumInstances(HTuple metrologyHandle, HTuple index, out HTuple numInstances)`

`HTuple HMetrologyModel.GetMetrologyObjectNumInstances(HTuple index)`

`double HMetrologyModel.GetMetrologyObjectNumInstances(int index)`

## Description

`GetMetrologyObjectNumInstances` allows to access the number of
instances (results) of measurements applied by [`ApplyMetrologyModel`](apply_metrology_model.md)
for the metrology objects. Note that by default, the maximum number of
instances of each metrology object is set to *1*. Thus, by default,
the result of `GetMetrologyObjectNumInstances` will typically be
*1* as well. To allow more instances, before applying the measurement
with [`ApplyMetrologyModel`](apply_metrology_model.md) you have to explicitly set the parameter
*"num_instances"* to a higher value or to *"all"* using
[`SetMetrologyObjectParam`](set_metrology_object_param.md).

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrologyHandle`*. The
parameter *`index`* specifies for which metrology object the instances
are queried. For *`index`* set to *"all"*, the number of
instances of all metrology objects are returned. The number of instances is
returned in *`numInstances`* for each metrology object that was passed
in *`index`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`metrologyHandle`** (input_control)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Index of the metrology objects.

Default:
0

Suggested values:
"all", 0, 1, 2

**`numInstances`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Number of Instances of the metrology objects.

## Result

If the parameters are valid, the operator
`GetMetrologyObjectNumInstances` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ApplyMetrologyModel`

## Possible Successors

`ClearMetrologyModel`

## See also

`GetMetrologyObjectIndices`

## Module

2D Metrology
