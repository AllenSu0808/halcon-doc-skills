# clear_ocr_class_cnn (Operator)

## Name

`clear_ocr_class_cnn` — Clear an CNN-based OCR classifier.

## Signature

`clear_ocr_class_cnn( : : OCRHandle : )`

## Description

`clear_ocr_class_cnn` clears the OCR classifier given by
*`OCRHandle`* that was read with [`read_ocr_class_cnn`](read_ocr_class_cnn.md) and frees
all memory required for the classifier. After calling
`clear_ocr_class_cnn`, the classifier can no longer be used. The
handle *`OCRHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_cnn(-array) `→`  (handle)

Handle of the OCR classifier.

## Result

If *`OCRHandle`* is valid, the operator
`clear_ocr_class_cnn` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`do_ocr_single_class_cnn`,
`do_ocr_multi_class_cnn`,
`do_ocr_word_cnn`

## See also

`read_ocr_class_cnn`

## Module

OCR/OCV
