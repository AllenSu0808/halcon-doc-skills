# WriteBarCodeModel (Operator)

## Name

`WriteBarCodeModel` — Write a bar code model to a file.

## Signature

`static void HOperatorSet.WriteBarCodeModel(HTuple barCodeHandle, HTuple fileName)`

`void HBarCode.WriteBarCodeModel(string fileName)`

## Description

The operator `WriteBarCodeModel` writes the bar code model
*`barCodeHandle`* to the file *`fileName`*. The model
can be read again with [`ReadBarCodeModel`](read_bar_code_model.md).
The stored data contains all generic and all specific model parameters
(see [`SetBarCodeParam`](set_bar_code_param.md) and [`SetBarCodeParamSpecific`](set_bar_code_param_specific.md),
respectively). If the model is in training mode (see
[`SetBarCodeParam`](set_bar_code_param.md) with parameter *"train"*), the current
training state is stored as well. After restoring the model, the training
can be proceeded.

Besides the training state no other results of [`FindBarCode`](find_bar_code.md) are
stored in the file.

The default HALCON file extension for bar code model is 'bcm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barCodeHandle`** (input_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the bar code model file.

Default:
"bar_code_model.bcm"

File extension:
.`bcm`

## Example (HDevelop)

```
*
* Create the bar code model in the training mode
create_bar_code_model ('train', 'all', BarCodeHandle)
*
* Set all additional, non-trained parameters in advance:
* Here, we specify that the training images have check characters
set_bar_code_param (BarCodeHandle, 'check_char', 'present')
*
* Train the model with several images
for I := 1 to 7 by 1
    FileName := 'barcode/25interleaved/25interleaved' + I$'.02'
    read_image (Image, FileName)
    *
    * Apply the training
    find_bar_code (Image, SymbolRegion, BarCodeHandle, '2/5 Interleaved', \
                   DecodedDataStrings)
endfor
*
* The training may be interrupted and the intermediate state
* of the model can be stored in a file
write_bar_code_model (BarCodeHandle, 'bar_code_model.bcm')
*
* RESTORE TRAINING:
* Later, when, e.g., new images are available, the training
* may be restored
read_bar_code_model ('bar_code_model.bcm', BarCodeHandle)
FileName := 'barcode/25interleaved/25interleaved08'
read_image (Image, FileName)
*
* Apply the training to the new image
find_bar_code (Image, SymbolRegion, BarCodeHandle, '2/5 Interleaved', \
               DecodedDataStrings)
*
* Finally, the training can be completed
set_bar_code_param (BarCodeHandle, 'train', '~all')
*
* The trained model can be stored for ONLINE use
write_bar_code_model (BarCodeHandle, 'trained_bar_code_model.bcm')
*
* ONLINE USE:
read_bar_code_model ('trained_bar_code_model.bcm', BarCodeHandle)
* ...
```

## Result

The operator `WriteBarCodeModel` returns the value 2 (
H_MSG_TRUE)
if the passed handle is valid and if the model can be written into
the named file.
Otherwise, an exception is raised.

## Possible Predecessors

`CreateBarCodeModel`,
`SetBarCodeParam`

## See also

`CreateBarCodeModel`,
`SetBarCodeParam`,
`FindBarCode`

## Module

Bar Code
