# traind_ocr_class_box (Operator)

## Name

`traind_ocr_class_box` — Train an OCR classifier by the input of regions.

## Warning

**`traind_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def traind_ocr_class_box(character: HObject, image: HObject, ocr_handle: HHandle, class_val: MaybeSequence[str]) -> float`

## Description

The operator `traind_ocr_class_box` trains the classifier
directly via the input of regions in an image.
Any number of regions of an image can be passed.
For each character (region) in *`character`* the
corresponding name (class) *`class`* must be
specified. The gray values are passed in *`image`*.
When the procedure has finished the parameter *`avg_confidence`*
provides information about the success of the training: It contains
the average confidence of the trained characters measured by a
re-classification. The confidence of mismatched characters
is set to 0 (thus, the average confidence will be decreased significantly).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocr_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`character`** (input_object)  region(-array) `→` HObject

Characters to be trained.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values for the characters.

**`ocr_handle`** (input_control, state is modified)  ocr_box `→` HHandle

ID of the desired OCR-classifier.

**`class`** (input_control)  string(-array) `→` MaybeSequence[str]

Class (name) of the characters.

Default:
"a"

**`avg_confidence`** (output_control)  real `→` float

Average confidence during a re-classification
of the trained characters.

## Result

If the parameters are correct, the operator
`traind_ocr_class_box` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`create_ocr_class_box`,
`read_ocr`

## Possible Successors

`write_ocr`,
`do_ocr_multi`,
`do_ocr_single`

## Alternatives

`trainf_ocr_class_box`

## Module

OCR/OCV
