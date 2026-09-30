# encrypt_serialized_item (Operator)

## Name

`encrypt_serialized_item` — Encrypt a serialized item.

## Signature

`def encrypt_serialized_item(serialized_item_handle: HHandle, encryption_param: HHandle) -> HHandle`

## Description

The operator `encrypt_serialized_item` encrypts the serialized item
*`serialized_item_handle`* to the encrypted item
*`encrypted_item_handle`* using the secret in the dictionary
*`encryption_param`*. The secret must be passed in the form of a password
string in the dictionary key 'password'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Serialized item handle.

**`encryption_param`** (input_control)  dict `→` HHandle

Parameters for the encryption.

Default:
[]

**`encrypted_item_handle`** (output_control)  encrypted_item `→` HHandle

Encrypted item handle.

## Result

The operator `encrypt_serialized_item` returns the value 2 (
H_MSG_TRUE)
if the
passed handles and the parameters are valid. Otherwise, an exception is
raised.

## Possible Predecessors

`serialize_handle`

## Possible Successors

`write_encrypted_item`,
`decrypt_serialized_item`

## Module

Foundation
