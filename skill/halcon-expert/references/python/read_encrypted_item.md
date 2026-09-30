# read_encrypted_item (Operator)

## Name

`read_encrypted_item` — Read an encrypted item from a file.

## Signature

`def read_encrypted_item(file_name: str) -> HHandle`

## Description

The operator `read_encrypted_item` reads the file *`file_name`* and
creates a new encrypted item in *`encrypted_item_handle`* that is an
identical copy of the saved item. The file *`file_name`* must have been
created by the operator [`write_encrypted_item`](write_encrypted_item.md).

The default HALCON file extension for encrypted item is '.henc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the file.

Default:
"encrypted_item.henc"

File extension:
.`bin`

**`encrypted_item_handle`** (output_control)  encrypted_item `→` HHandle

Handle of the encrypted item.

## Result

The operator `read_encrypted_item` returns the value 2 (
H_MSG_TRUE)
if the
named file was found and correctly read. Otherwise, an exception is raised.

## Possible Successors

`decrypt_serialized_item`

## See also

`write_encrypted_item`,
`encrypt_serialized_item`

## Module

Foundation
