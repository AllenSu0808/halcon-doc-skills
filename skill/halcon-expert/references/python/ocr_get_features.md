# ocr_get_features (Operator)

## Name

`ocr_get_features` — Access the features which correspond to a character.

## Warning

**`ocr_get_features` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def ocr_get_features(character: HObject, ocr_handle: HHandle) -> Sequence[float]`

## Description

The operator `ocr_get_features` calculates the features for
the given *`character`*. The type and number of features is
determined by the classifier *`ocr_handle`*.
*`feature_vector`* contains the same values which are used
inside operators like [`traind_ocr_class_box`](traind_ocr_class_box.md) or
[`trainf_ocr_class_box`](trainf_ocr_class_box.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Characters to be trained.

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the desired OCR-classifier.

**`feature_vector`** (output_control)  real-array `→` Sequence[float]

Feature vector.

## Result

If the parameters are correct, the operator
`ocr_get_features` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`read_ocr`,
`reduce_domain`,
`threshold`,
`connection`

## See also

`trainf_ocr_class_box`,
`traind_ocr_class_box`

## Module

OCR/OCV
