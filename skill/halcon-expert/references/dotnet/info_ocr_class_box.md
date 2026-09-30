# InfoOcrClassBox (Operator)

## Name

`InfoOcrClassBox` — Get information about an OCR classifier.

## Warning

**`InfoOcrClassBox` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.InfoOcrClassBox(HTuple ocrHandle, out HTuple widthPattern, out HTuple heightPattern, out HTuple interpolation, out HTuple widthMaxChar, out HTuple heightMaxChar, out HTuple features, out HTuple characters)`

`void HOCRBox.InfoOcrClassBox(out int widthPattern, out int heightPattern, out int interpolation, out int widthMaxChar, out int heightMaxChar, out HTuple features, out HTuple characters)`

## Description

The operator `InfoOcrClassBox` returns some information
about an OCR classifier.
The parameters are equivalent to those of [`CreateOcrClassBox`](create_ocr_class_box.md).
The parameters *`widthMaxChar`* and *`heightMaxChar`*
indicate the extension of the largest trained character.
These values can be used to control the segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier.

**`widthPattern`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the scaled characters.

**`heightPattern`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the scaled characters.

**`interpolation`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Interpolation mode for scaling the characters.

**`widthMaxChar`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the largest trained character.

**`heightMaxChar`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the largest trained character.

**`features`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Used features.

**`characters`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

All characters of the set.

## Result

The operator `InfoOcrClassBox` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`ReadOcr`,
`CreateOcrClassBox`

## Possible Successors

`WriteOcr`

## Module

OCR/OCV
