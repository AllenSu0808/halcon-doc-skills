# encrypt_serialized_item (Operator)

## Name

`encrypt_serialized_item` — Encrypt a serialized item.

## Signature

`encrypt_serialized_item( : : SerializedItemHandle, EncryptionParam : EncryptedItemHandle)`

## Description

The operator `encrypt_serialized_item` encrypts the serialized item
*`SerializedItemHandle`* to the encrypted item
*`EncryptedItemHandle`* using the secret in the dictionary
*`EncryptionParam`*. The secret must be passed in the form of a password
string in the dictionary key 'password'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Serialized item handle.

**`EncryptionParam`** (input_control)  dict `→`  (handle)

Parameters for the encryption.

Default:
[]

**`EncryptedItemHandle`** (output_control)  encrypted_item `→`  (handle)

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
