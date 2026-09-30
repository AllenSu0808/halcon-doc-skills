# TrainfOcrClassBox (Operator)

## Name

`TrainfOcrClassBox` — Train an OCR classifier with the help of a training file.

## Warning

**`TrainfOcrClassBox` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.TrainfOcrClassBox(HTuple ocrHandle, HTuple trainingFile, out HTuple avgConfidence)`

`double HOCRBox.TrainfOcrClassBox(HTuple trainingFile)`

`double HOCRBox.TrainfOcrClassBox(string trainingFile)`

## Description

The operator `TrainfOcrClassBox` trains the classifier
*`ocrHandle`* via the indicated training files.
Any number of files can be indicated. The parameter *`avgConfidence`*
provides information about the success of the training: It contains
the average confidence of the trained characters measured by a
re-classification. The confidence of mismatched characters
is set to 0 (thus, the average confidence will be decreased significantly).
Please, note that training characters that have no corresponding class in the
classifier *`ocrHandle`* are discarded.

## Attention

The names of the characters in the file must fit the
network.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrHandle`** (input_control, state is modified)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the desired OCR-network.

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
"train_ocr"

File extension:
.`trf`, .`otr`

**`avgConfidence`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Average confidence during a re-classification
of the trained characters.

## Result

If the file name is correct and the data fit the network,
the operator `TrainfOcrClassBox` returns the value
2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`CreateOcrClassBox`,
`ReadOcr`

## Possible Successors

`TraindOcrClassBox`,
`WriteOcr`,
`DoOcrMulti`,
`DoOcrSingle`

## Alternatives

`TraindOcrClassBox`

## Module

OCR/OCV
