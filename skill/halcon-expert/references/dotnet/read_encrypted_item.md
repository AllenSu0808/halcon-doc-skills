# ReadEncryptedItem (Operator)

## Name

`ReadEncryptedItem` — Read an encrypted item from a file.

## Signature

`static void HOperatorSet.ReadEncryptedItem(HTuple fileName, out HTuple encryptedItemHandle)`

`public HEncryptedItem(string fileName)`

`void HEncryptedItem.ReadEncryptedItem(string fileName)`

## Description

The operator `ReadEncryptedItem` reads the file *`fileName`* and
creates a new encrypted item in *`encryptedItemHandle`* that is an
identical copy of the saved item. The file *`fileName`* must have been
created by the operator [`WriteEncryptedItem`](write_encrypted_item.md).

The default HALCON file extension for encrypted item is '.henc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the file.

Default:
"encrypted_item.henc"

File extension:
.`bin`

**`encryptedItemHandle`** (output_control)  encrypted_item `→` [HEncryptedItem](HEncryptedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the encrypted item.

## Result

The operator `ReadEncryptedItem` returns the value 2 (
H_MSG_TRUE)
if the
named file was found and correctly read. Otherwise, an exception is raised.

## Possible Successors

`DecryptSerializedItem`

## See also

`WriteEncryptedItem`,
`EncryptSerializedItem`

## Module

Foundation
