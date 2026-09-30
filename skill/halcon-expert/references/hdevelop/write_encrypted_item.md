# write_encrypted_item (Operator)

## Name

`write_encrypted_item` — Write an encrypted item to a file.

## Signature

`write_encrypted_item( : : EncryptedItemHandle, FileName : )`

## Description

The operator `write_encrypted_item` writes the encrypted item
*`EncryptedItemHandle`* to the file *`FileName`*. The item can be
read again with [`read_encrypted_item`](read_encrypted_item.md).

The default HALCON file extension for encrypted item is '.henc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EncryptedItemHandle`** (input_control)  encrypted_item `→`  (handle)

Handle of the encrypted item.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file.

Default:
'encrypted_item.henc'

File extension:
.`bin`

## Result

The operator `write_encrypted_item` returns the value 2 (
H_MSG_TRUE)
if the
passed handle is valid and if the encrypted item can be written into the named
file. Otherwise, an exception is raised.

## Possible Predecessors

`encrypt_serialized_item`

## See also

`read_encrypted_item`,
`decrypt_serialized_item`

## Module

Foundation
