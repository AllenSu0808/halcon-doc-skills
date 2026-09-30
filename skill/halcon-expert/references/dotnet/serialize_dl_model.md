# SerializeDlModel (Operator)

## Name

`SerializeDlModel` — Serialize a deep learning model.

## Signature

`static void HOperatorSet.SerializeDlModel(HTuple DLModelHandle, out HTuple serializedItemHandle)`

`HSerializedItem HDlModel.SerializeDlModel()`

## Description

`SerializeDlModel` serializes the deep learning model
defined by the handle *`DLModelHandle`*.
The serialized model is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeDlModel`](deserialize_dl_model.md).
See [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization.

The operator acts the same as [`WriteDlModel`](write_dl_model.md) except that the output
is a serialized item instead of a file.
For a detailed description please refer to the documentation of
[`WriteDlModel`](write_dl_model.md).

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator `SerializeDlModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`

## Possible Successors

`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`,
`FwriteSerializedItem`,
`SendSerializedItem`

## See also

`DeserializeDlModel`,
`ApplyDlModel`,
`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
