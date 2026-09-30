# serialize_dl_model (Operator)

## Name

`serialize_dl_model` — Serialize a deep learning model.

## Signature

`def serialize_dl_model(dlmodel_handle: HHandle) -> HHandle`

## Description

`serialize_dl_model` serializes the deep learning model
defined by the handle *`dlmodel_handle`*.
The serialized model is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_dl_model`](deserialize_dl_model.md).
See [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization.

The operator acts the same as [`write_dl_model`](write_dl_model.md) except that the output
is a serialized item instead of a file.
For a detailed description please refer to the documentation of
[`write_dl_model`](write_dl_model.md).

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of the deep learning model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator `serialize_dl_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`

## Possible Successors

`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`,
`fwrite_serialized_item`,
`send_serialized_item`

## See also

`deserialize_dl_model`,
`apply_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
