# info_ocr_class_box (Operator)

## Name

`info_ocr_class_box` — Get information about an OCR classifier.

## Warning

**`info_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`info_ocr_class_box( : : OcrHandle : WidthPattern, HeightPattern, Interpolation, WidthMaxChar, HeightMaxChar, Features, Characters)`

## Description

The operator `info_ocr_class_box` returns some information
about an OCR classifier.
The parameters are equivalent to those of [`create_ocr_class_box`](create_ocr_class_box.md).
The parameters *`WidthMaxChar`* and *`HeightMaxChar`*
indicate the extension of the largest trained character.
These values can be used to control the segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OcrHandle`** (input_control)  ocr_box `→`  (handle)

ID of the OCR classifier.

**`WidthPattern`** (output_control)  integer `→`  (integer)

Width of the scaled characters.

**`HeightPattern`** (output_control)  integer `→`  (integer)

Height of the scaled characters.

**`Interpolation`** (output_control)  integer `→`  (integer)

Interpolation mode for scaling the characters.

**`WidthMaxChar`** (output_control)  integer `→`  (integer)

Width of the largest trained character.

**`HeightMaxChar`** (output_control)  integer `→`  (integer)

Height of the largest trained character.

**`Features`** (output_control)  string-array `→`  (string)

Used features.

**`Characters`** (output_control)  string-array `→`  (string)

All characters of the set.

## Result

The operator `info_ocr_class_box` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`read_ocr`,
`create_ocr_class_box`

## Possible Successors

`write_ocr`

## Module

OCR/OCV
