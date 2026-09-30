# WriteEncryptedItem (Operator)

## Name

`WriteEncryptedItem` — Write an encrypted item to a file.

## Signature

`static void HOperatorSet.WriteEncryptedItem(HTuple encryptedItemHandle, HTuple fileName)`

## Description

The operator `WriteEncryptedItem` writes the encrypted item
*`encryptedItemHandle`* to the file *`fileName`*. The item can be
read again with [`ReadEncryptedItem`](read_encrypted_item.md).

The default HALCON file extension for encrypted item is '.henc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`encryptedItemHandle`** (input_control)  encrypted_item `→` [HEncryptedItem](HEncryptedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the encrypted item.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file.

Default:
"encrypted_item.henc"

File extension:
.`bin`

## Result

The operator `WriteEncryptedItem` returns the value 2 (
H_MSG_TRUE)
if the
passed handle is valid and if the encrypted item can be written into the named
file. Otherwise, an exception is raised.

## Possible Predecessors

`EncryptSerializedItem`

## See also

`ReadEncryptedItem`,
`DecryptSerializedItem`

## Module

Foundation
