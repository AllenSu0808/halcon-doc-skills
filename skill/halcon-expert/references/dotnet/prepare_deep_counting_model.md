# PrepareDeepCountingModel (Operator)

## Name

`PrepareDeepCountingModel` — Set templates of a Deep Counting model.

## Signature

`static void HOperatorSet.PrepareDeepCountingModel(HObject templates, HTuple deepCountingHandle)`

`void HDlModelCounting.PrepareDeepCountingModel(HImage templates)`

## Description

`PrepareDeepCountingModel` sets the templates of the objects that
should be counted by the Deep Counting model *`deepCountingHandle`*.
When applying the Deep Counting model using [`ApplyDeepCountingModel`](apply_deep_counting_model.md),
objects in the search images that are similar to the provided templates
are detected and counted.
Note that this operator overwrites any previously set templates.

To also count scaled and rotated variants of the provided templates,
an automatic augmentation of the templates can be enabled by setting
the parameters *"angle_start"*, *"angle_end"*,
*"angle_step"*, *"scale_min"*, *"scale_max"*, and
*"scale_step"* using [`CreateDeepCountingModel`](create_deep_counting_model.md) or
[`SetDeepCountingModelParam`](set_deep_counting_model_param.md) before calling
[`ApplyDeepCountingModel`](apply_deep_counting_model.md).

When changing parameters of the Deep Counting model that influence the
template creation, `PrepareDeepCountingModel` must be re-run
before [`ApplyDeepCountingModel`](apply_deep_counting_model.md).
The list of such parameters is provided in [`GetDeepCountingModelParam`](get_deep_counting_model_param.md).

## Attention

System requirements:
To run this operator on GPU (see [`GetDeepCountingModelParam`](get_deep_counting_model_param.md)),
cuDNN and cuBLAS are required.
For further details, please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.
Alternatively, this operator can also be run on CPU.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- deepCountingHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`templates`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / real)

Template image(s) with regions.

**`deepCountingHandle`** (input_control, state is modified)  deep_counting `→` [HDlModelCounting](HDlModelCounting.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the Deep Counting model.

## Result

If the handle of the model is valid, the operator
`PrepareDeepCountingModel` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateDeepCountingModel`,
`SetDeepCountingModelParam`,
`GetDeepCountingModelParam`,
`ReadDeepCountingModel`

## Possible Successors

`ApplyDeepCountingModel`

## Alternatives

`ReadDeepCountingModel`

## See also

`ApplyDeepCountingModel`

## Module

Matching
