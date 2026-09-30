# prepare_deep_counting_model (Operator)

## Name

`prepare_deep_counting_model` — Set templates of a Deep Counting model.

## Signature

`prepare_deep_counting_model(Templates : : DeepCountingHandle : )`

## Description

`prepare_deep_counting_model` sets the templates of the objects that
should be counted by the Deep Counting model *`DeepCountingHandle`*.
When applying the Deep Counting model using [`apply_deep_counting_model`](apply_deep_counting_model.md),
objects in the search images that are similar to the provided templates
are detected and counted.
Note that this operator overwrites any previously set templates.

To also count scaled and rotated variants of the provided templates,
an automatic augmentation of the templates can be enabled by setting
the parameters *'angle_start'*, *'angle_end'*,
*'angle_step'*, *'scale_min'*, *'scale_max'*, and
*'scale_step'* using [`create_deep_counting_model`](create_deep_counting_model.md) or
[`set_deep_counting_model_param`](set_deep_counting_model_param.md) before calling
[`apply_deep_counting_model`](apply_deep_counting_model.md).

When changing parameters of the Deep Counting model that influence the
template creation, `prepare_deep_counting_model` must be re-run
before [`apply_deep_counting_model`](apply_deep_counting_model.md).
The list of such parameters is provided in [`get_deep_counting_model_param`](get_deep_counting_model_param.md).

## Attention

System requirements:
To run this operator on GPU (see [`get_deep_counting_model_param`](get_deep_counting_model_param.md)),
cuDNN and cuBLAS are required.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.
Alternatively, this operator can also be run on CPU.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- DeepCountingHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Templates`** (input_object)  (multichannel-)image(-array) `→` object (byte / real)

Template image(s) with regions.

**`DeepCountingHandle`** (input_control, state is modified)  deep_counting `→`  (handle)

Handle of the Deep Counting model.

## Result

If the handle of the model is valid, the operator
`prepare_deep_counting_model` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_deep_counting_model`,
`set_deep_counting_model_param`,
`get_deep_counting_model_param`,
`read_deep_counting_model`

## Possible Successors

`apply_deep_counting_model`

## Alternatives

`read_deep_counting_model`

## See also

`apply_deep_counting_model`

## Module

Matching
