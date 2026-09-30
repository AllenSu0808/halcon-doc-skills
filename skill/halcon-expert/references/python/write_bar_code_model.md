# write_bar_code_model (Operator)

## Name

`write_bar_code_model` — Write a bar code model to a file.

## Signature

`def write_bar_code_model(bar_code_handle: HHandle, file_name: str) -> None`

## Description

The operator `write_bar_code_model` writes the bar code model
*`bar_code_handle`* to the file *`file_name`*. The model
can be read again with [`read_bar_code_model`](read_bar_code_model.md).
The stored data contains all generic and all specific model parameters
(see [`set_bar_code_param`](set_bar_code_param.md) and [`set_bar_code_param_specific`](set_bar_code_param_specific.md),
respectively). If the model is in training mode (see
[`set_bar_code_param`](set_bar_code_param.md) with parameter *"train"*), the current
training state is stored as well. After restoring the model, the training
can be proceeded.

Besides the training state no other results of [`find_bar_code`](find_bar_code.md) are
stored in the file.

The default HALCON file extension for bar code model is 'bcm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`bar_code_handle`** (input_control)  barcode `→` HHandle

Handle of the bar code model.

**`file_name`** (input_control)  filename.write `→` str

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

The operator `write_bar_code_model` returns the value 2 (
H_MSG_TRUE)
if the passed handle is valid and if the model can be written into
the named file.
Otherwise, an exception is raised.

## Possible Predecessors

`create_bar_code_model`,
`set_bar_code_param`

## See also

`create_bar_code_model`,
`set_bar_code_param`,
`find_bar_code`

## Module

Bar Code
