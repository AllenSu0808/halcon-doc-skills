# ClearDlModel (Operator)

## Name

`ClearDlModel` — Clear a deep learning model.

## Signature

`static void HOperatorSet.ClearDlModel(HTuple DLModelHandle)`

`static void HDlModel.ClearDlModel(HDlModel[] DLModelHandle)`

`void HDlModel.ClearDlModel()`

## Description

`ClearDlModel` clears the handle of the deep learning model given
by *`DLModelHandle`* and frees all memory required for the model.
After calling `ClearDlModel`, the model can no longer be used
and the handle *`DLModelHandle`* becomes invalid.

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- DLModelHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`DLModelHandle`** (input_control, state is modified)  dl_model(-array) `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

## Result

If the parameters are valid, the operator `ClearDlModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`ReadDlModel`,
`ApplyDlModel`,
`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
