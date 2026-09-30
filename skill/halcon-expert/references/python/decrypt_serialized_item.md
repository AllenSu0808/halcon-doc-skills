# decrypt_serialized_item (Operator)

## Name

`decrypt_serialized_item` — Decrypt an encrypted item.

## Signature

`def decrypt_serialized_item(encrypted_item_handle: HHandle, decryption_param: HHandle) -> HHandle`

## Description

The operator `decrypt_serialized_item` decrypts the encrypted item
*`encrypted_item_handle`* to the serialized item
*`serialized_item_handle`* using the secret in the dictionary
*`decryption_param`*. The secret must be passed in the form of a password
string in the dictionary key 'password'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`encrypted_item_handle`** (input_control)  encrypted_item `→` HHandle

Encrypted item handle.

**`decryption_param`** (input_control)  dict `→` HHandle

Parameters for the decryption.

Default:
[]

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Serialized item handle.

## Result

The operator `decrypt_serialized_item` returns the value 2 (
H_MSG_TRUE)
if the
passed handles and the parameters are valid. Otherwise, an exception is
raised.

## Possible Predecessors

`encrypt_serialized_item`,
`read_encrypted_item`

## Possible Successors

`deserialize_handle`

## Module

Foundation
