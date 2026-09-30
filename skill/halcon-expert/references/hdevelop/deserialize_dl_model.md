# deserialize_dl_model (Operator)

## Name

`deserialize_dl_model` — Deserialize a deep learning model.

## Signature

`deserialize_dl_model( : : SerializedItemHandle : DLModelHandle)`

## Description

`deserialize_dl_model` deserializes the deep learning model defined
by the handle *`SerializedItemHandle`* and previously serialized by
[`serialize_dl_model`](serialize_dl_model.md).

The operator acts the same as [`read_dl_model`](read_dl_model.md) except that the input
is a serialized item instead of a file.
For a detailed description please refer to the documentation of
[`read_dl_model`](read_dl_model.md).

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`DLModelHandle`** (output_control)  dl_model `→`  (handle)

Handle of the deep learning model.

## Result

If the parameters are valid, the operator `deserialize_dl_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_dl_model`

## Possible Successors

`apply_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`,
`set_dl_model_param`,
`get_dl_model_param`

## See also

`serialize_dl_model`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
