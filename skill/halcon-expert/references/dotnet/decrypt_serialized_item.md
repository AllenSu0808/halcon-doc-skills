# DecryptSerializedItem (Operator)

## Name

`DecryptSerializedItem` — Decrypt an encrypted item.

## Signature

`static void HOperatorSet.DecryptSerializedItem(HTuple encryptedItemHandle, HTuple decryptionParam, out HTuple serializedItemHandle)`

## Description

The operator `DecryptSerializedItem` decrypts the encrypted item
*`encryptedItemHandle`* to the serialized item
*`serializedItemHandle`* using the secret in the dictionary
*`decryptionParam`*. The secret must be passed in the form of a password
string in the dictionary key 'password'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`encryptedItemHandle`** (input_control)  encrypted_item `→` [HEncryptedItem](HEncryptedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Encrypted item handle.

**`decryptionParam`** (input_control)  dict `→` [HDict](HDict.md), [HTuple](HTuple.md) (*IntPtr*)

Parameters for the decryption.

Default:
[]

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Serialized item handle.

## Result

The operator `DecryptSerializedItem` returns the value 2 (
H_MSG_TRUE)
if the
passed handles and the parameters are valid. Otherwise, an exception is
raised.

## Possible Predecessors

`EncryptSerializedItem`,
`ReadEncryptedItem`

## Possible Successors

`DeserializeHandle`

## Module

Foundation
