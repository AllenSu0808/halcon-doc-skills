# read_ocr_class_cnn (Operator)

## Name

`read_ocr_class_cnn` — Read an CNN-based OCR classifier from a file.

## Signature

`def read_ocr_class_cnn(file_name: str) -> HHandle`

## Description

`read_ocr_class_cnn` reads a pretrained OCR classifier based on a
convolutional neural network (CNN).

The CNN-based OCR classifier is read with `read_ocr_class_cnn` and
subsequently used for classification with either
[`do_ocr_single_class_cnn`](do_ocr_single_class_cnn.md), [`do_ocr_multi_class_cnn`](do_ocr_multi_class_cnn.md), or
[`do_ocr_word_cnn`](do_ocr_word_cnn.md).

HALCON provides a number of pretrained OCR classifiers (see
`“Solution Guide I”`, chapter 'OCR', section 'Pretrained OCR
Fonts'). These pretrained OCR
classifiers make it possible to read a wide variety of different fonts
without the need to train an OCR classifier. Note that the pretrained OCR
classifiers were trained with symbols that are printed dark on light.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

Default:
"Universal_Rej.occ"

Suggested values:
"Universal_NoRej.occ", "Universal_Rej.occ", "Universal_0-9_NoRej.occ", "Universal_0-9_Rej.occ", "Universal_0-9+_NoRej.occ", "Universal_0-9+_Rej.occ", "Universal_0-9A-Z_NoRej.occ", "Universal_0-9A-Z_Rej.occ", "Universal_0-9A-Z+_NoRej.occ", "Universal_0-9A-Z+_Rej.occ", "Universal_A-Z+_NoRej.occ", "Universal_A-Z+_Rej.occ"

File extension:
.`occ`, .`fnt`

**`ocrhandle`** (output_control)  ocr_cnn `→` HHandle

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator `read_ocr_class_cnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`do_ocr_single_class_cnn`,
`do_ocr_multi_class_cnn`,
`do_ocr_word_cnn`

## See also

`get_params_ocr_class_cnn`

## Module

OCR/OCV
