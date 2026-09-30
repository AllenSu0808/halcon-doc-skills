# ReadOcrClassMlp (Operator)

## Name

`ReadOcrClassMlp` — Read an OCR classifier from a file.

## Signature

`static void HOperatorSet.ReadOcrClassMlp(HTuple fileName, out HTuple OCRHandle)`

`public HOCRMlp(string fileName)`

`void HOCRMlp.ReadOcrClassMlp(string fileName)`

## Description

`ReadOcrClassMlp` reads an OCR classifier that has been
stored with [`WriteOcrClassMlp`](write_ocr_class_mlp.md). Since the training of an
OCR classifier can consume a relatively long time, the classifier is
typically trained in an offline process and written to a file with
[`WriteOcrClassMlp`](write_ocr_class_mlp.md). In the online process the classifier
is read with `ReadOcrClassMlp` and subsequently used for
classification with [`DoOcrSingleClassMlp`](do_ocr_single_class_mlp.md) or
[`DoOcrMultiClassMlp`](do_ocr_multi_class_mlp.md).

HALCON provides a number of pretrained OCR classifiers (see the
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

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

Suggested values:
"Document_0-9_NoRej.omc", "Document_0-9_Rej.omc", "Document_0-9A-Z_NoRej.omc", "Document_0-9A-Z_Rej.omc", "Document_A-Z+_NoRej.omc", "Document_A-Z+_Rej.omc", "Document_NoRej.omc", "Document_Rej.omc", "DotPrint_0-9_NoRej.omc", "DotPrint_0-9_Rej.omc", "DotPrint_0-9+_NoRej.omc", "DotPrint_0-9+_Rej.omc", "DotPrint_0-9A-Z_NoRej.omc", "DotPrint_0-9A-Z_Rej.omc", "DotPrint_A-Z+_NoRej.omc", "DotPrint_A-Z+_Rej.omc", "DotPrint_NoRej.omc", "DotPrint_Rej.omc", "HandWritten_0-9_NoRej.omc", "HandWritten_0-9_Rej.omc", "Industrial_0-9_NoRej.omc", "Industrial_0-9_Rej.omc", "Industrial_0-9+_NoRej.omc", "Industrial_0-9+_Rej.omc", "Industrial_0-9A-Z_NoRej.omc", "Industrial_0-9A-Z_Rej.omc", "Industrial_A-Z+_NoRej.omc", "Industrial_A-Z+_Rej.omc", "Industrial_NoRej.omc", "Industrial_Rej.omc", "OCRA_0-9_NoRej.omc", "OCRA_0-9_Rej.omc", "OCRA_0-9A-Z_NoRej.omc", "OCRA_0-9A-Z_Rej.omc", "OCRA_A-Z+_NoRej.omc", "OCRA_A-Z+_Rej.omc", "OCRA_NoRej.omc", "OCRA_Rej.omc", "OCRB_0-9_NoRej.omc", "OCRB_0-9_Rej.omc", "OCRB_0-9A-Z_NoRej.omc", "OCRB_0-9A-Z_Rej.omc", "OCRB_A-Z+_NoRej.omc", "OCRB_A-Z+_Rej.omc", "OCRB_NoRej.omc", "OCRB_passport_NoRej.omc", "OCRB_passport_Rej.omc", "OCRB_Rej.omc", "Pharma_0-9_NoRej.omc", "Pharma_0-9_Rej.omc", "Pharma_0-9+_NoRej.omc", "Pharma_0-9+_Rej.omc", "Pharma_0-9A-Z_NoRej.omc", "Pharma_0-9A-Z_Rej.omc", "Pharma_NoRej.omc", "Pharma_Rej.omc", "SEMI_NoRej.omc", "SEMI_Rej.omc"

File extension:
.`omc`, .`fnt`

**`OCRHandle`** (output_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator `ReadOcrClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`DoOcrSingleClassMlp`,
`DoOcrMultiClassMlp`

## See also

`CreateOcrClassMlp`,
`WriteOcrClassMlp`,
`ReadClassMlp`,
`WriteClassMlp`

## Module

OCR/OCV
