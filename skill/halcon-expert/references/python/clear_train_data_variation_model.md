# clear_train_data_variation_model (Operator)

## Name

`clear_train_data_variation_model` — Free the memory of the training data of a variation model.

## Signature

`def clear_train_data_variation_model(model_id: HHandle) -> None`

## Description

`clear_train_data_variation_model` frees the memory of a
variation model that was created by [`create_variation_model`](create_variation_model.md).
`clear_train_data_variation_model` can be used to reduce the
amount of memory required for the variation model (in main memory as
well as when writing the model to file with
[`write_variation_model`](write_variation_model.md)).
`clear_train_data_variation_model` can only be called if the
model has been prepared for comparison with an image with
[`prepare_variation_model`](prepare_variation_model.md). After the call to
`clear_train_data_variation_model` the variation model can
only be used for image comparison with
[`compare_variation_model`](compare_variation_model.md) or
[`compare_ext_variation_model`](compare_ext_variation_model.md). The model cannot be trained
any further. Furthermore, the images used for the image comparison
can no longer be read with [`get_variation_model`](get_variation_model.md). If they are
required, [`get_variation_model`](get_variation_model.md) must be called before
`clear_train_data_variation_model` is called.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`model_id`** (input_control, state is modified)  variation_model `→` HHandle

ID of the variation model.

## Result

`clear_train_data_variation_model` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`prepare_variation_model`

## Possible Successors

`compare_variation_model`,
`compare_ext_variation_model`,
`write_variation_model`

## Module

Matching
