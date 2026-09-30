# trainf_ocr_class_box (Operator)

## Name

`trainf_ocr_class_box` — Train an OCR classifier with the help of a training file.

## Warning

**`trainf_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def trainf_ocr_class_box(ocr_handle: HHandle, training_file: MaybeSequence[str]) -> float`

## Description

The operator `trainf_ocr_class_box` trains the classifier
*`ocr_handle`* via the indicated training files.
Any number of files can be indicated. The parameter *`avg_confidence`*
provides information about the success of the training: It contains
the average confidence of the trained characters measured by a
re-classification. The confidence of mismatched characters
is set to 0 (thus, the average confidence will be decreased significantly).
Please, note that training characters that have no corresponding class in the
classifier *`ocr_handle`* are discarded.

## Attention

The names of the characters in the file must fit the
network.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocr_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocr_handle`** (input_control, state is modified)  ocr_box `→` HHandle

ID of the desired OCR-network.

**`training_file`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Names of the training files.

Default:
"train_ocr"

File extension:
.`trf`, .`otr`

**`avg_confidence`** (output_control)  real `→` float

Average confidence during a re-classification
of the trained characters.

## Result

If the file name is correct and the data fit the network,
the operator `trainf_ocr_class_box` returns the value
2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`create_ocr_class_box`,
`read_ocr`

## Possible Successors

`traind_ocr_class_box`,
`write_ocr`,
`do_ocr_multi`,
`do_ocr_single`

## Alternatives

`traind_ocr_class_box`

## Module

OCR/OCV
