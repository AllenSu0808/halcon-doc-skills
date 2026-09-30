# EncryptSerializedItem (Operator)

## Name

`EncryptSerializedItem` — Encrypt a serialized item.

## Signature

`static void HOperatorSet.EncryptSerializedItem(HTuple serializedItemHandle, HTuple encryptionParam, out HTuple encryptedItemHandle)`

## Description

The operator `EncryptSerializedItem` encrypts the serialized item
*`serializedItemHandle`* to the encrypted item
*`encryptedItemHandle`* using the secret in the dictionary
*`encryptionParam`*. The secret must be passed in the form of a password
string in the dictionary key 'password'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Serialized item handle.

**`encryptionParam`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Parameters for the encryption.

Default:
[]

**`encryptedItemHandle`** (output_control)  encrypted_item `→` [HEncryptedItem](HEncryptedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Encrypted item handle.

## Result

The operator `EncryptSerializedItem` returns the value 2 (
H_MSG_TRUE)
if the
passed handles and the parameters are valid. Otherwise, an exception is
raised.

## Possible Predecessors

`SerializeHandle`

## Possible Successors

`WriteEncryptedItem`,
`DecryptSerializedItem`

## Module

Foundation
