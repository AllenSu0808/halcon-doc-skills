# trainf_ocr_class_box (Operator)

## Name

`trainf_ocr_class_box` — Train an OCR classifier with the help of a training file.

## Warning

**`trainf_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`trainf_ocr_class_box( : : OcrHandle, TrainingFile : AvgConfidence)`

## Description

The operator `trainf_ocr_class_box` trains the classifier
*`OcrHandle`* via the indicated training files.
Any number of files can be indicated. The parameter *`AvgConfidence`*
provides information about the success of the training: It contains
the average confidence of the trained characters measured by a
re-classification. The confidence of mismatched characters
is set to 0 (thus, the average confidence will be decreased significantly).
Please, note that training characters that have no corresponding class in the
classifier *`OcrHandle`* are discarded.

## Attention

The names of the characters in the file must fit the
network.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OcrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OcrHandle`** (input_control, state is modified)  ocr_box `→`  (handle)

ID of the desired OCR-network.

**`TrainingFile`** (input_control)  filename.read(-array) `→`  (string)

Names of the training files.

Default:
'train_ocr'

File extension:
.`trf`, .`otr`

**`AvgConfidence`** (output_control)  real `→`  (real)

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
