# DeserializeDlModel (Operator)

## Name

`DeserializeDlModel` — Deserialize a deep learning model.

## Signature

`static void HOperatorSet.DeserializeDlModel(HTuple serializedItemHandle, out HTuple DLModelHandle)`

`void HDlModel.DeserializeDlModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeDlModel` deserializes the deep learning model defined
by the handle *`serializedItemHandle`* and previously serialized by
[`SerializeDlModel`](serialize_dl_model.md).

The operator acts the same as [`ReadDlModel`](read_dl_model.md) except that the input
is a serialized item instead of a file.
For a detailed description please refer to the documentation of
[`ReadDlModel`](read_dl_model.md).

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`DLModelHandle`** (output_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

## Result

If the parameters are valid, the operator `DeserializeDlModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeDlModel`

## Possible Successors

`ApplyDlModel`,
`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`,
`SetDlModelParam`,
`GetDlModelParam`

## See also

`SerializeDlModel`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
