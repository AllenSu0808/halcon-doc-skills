# WriteDlModel (Operator)

## Name

`WriteDlModel` — Write a deep learning model in a file.

## Signature

`static void HOperatorSet.WriteDlModel(HTuple DLModelHandle, HTuple fileName)`

`void HDlModel.WriteDlModel(string fileName)`

## Description

`WriteDlModel` writes the deep learning model
*`DLModelHandle`* to the file given by *`fileName`*.
Please note that the values of the runtime specific parameters *"gpu"*,
*"runtime"*, and *"runtime_init"* are not written.

The default HALCON file extension for deep learning models is
`'.hdl'`.

The model can be read with [`ReadDlModel`](read_dl_model.md).

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep learning model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Filename

File extension:
.`hdl`

## Result

If the parameters are valid, the operator `WriteDlModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`ReadDlModel`,
`TrainDlModelBatch`,
`TrainDlModelAnomalyDataset`,
`SetDlModelParam`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
