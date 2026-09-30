# write_dl_model (Operator)

## Name

`write_dl_model` — Write a deep learning model in a file.

## Signature

`def write_dl_model(dlmodel_handle: HHandle, file_name: str) -> None`

## Description

`write_dl_model` writes the deep learning model
*`dlmodel_handle`* to the file given by *`file_name`*.
Please note that the values of the runtime specific parameters *"gpu"*,
*"runtime"*, and *"runtime_init"* are not written.

The default HALCON file extension for deep learning models is
`'.hdl'`.

The model can be read with [`read_dl_model`](read_dl_model.md).

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of the deep learning model.

**`file_name`** (input_control)  filename.write `→` str

Filename

File extension:
.`hdl`

## Result

If the parameters are valid, the operator `write_dl_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`read_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`,
`set_dl_model_param`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
