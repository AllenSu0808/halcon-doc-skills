# info_ocr_class_box (Operator)

## Name

`info_ocr_class_box` — Get information about an OCR classifier.

## Warning

**`info_ocr_class_box` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def info_ocr_class_box(ocr_handle: HHandle) -> Tuple[int, int, int, int, int, Sequence[str], Sequence[str]]`

## Description

The operator `info_ocr_class_box` returns some information
about an OCR classifier.
The parameters are equivalent to those of [`create_ocr_class_box`](create_ocr_class_box.md).
The parameters *`width_max_char`* and *`height_max_char`*
indicate the extension of the largest trained character.
These values can be used to control the segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the OCR classifier.

**`width_pattern`** (output_control)  integer `→` int

Width of the scaled characters.

**`height_pattern`** (output_control)  integer `→` int

Height of the scaled characters.

**`interpolation`** (output_control)  integer `→` int

Interpolation mode for scaling the characters.

**`width_max_char`** (output_control)  integer `→` int

Width of the largest trained character.

**`height_max_char`** (output_control)  integer `→` int

Height of the largest trained character.

**`features`** (output_control)  string-array `→` Sequence[str]

Used features.

**`characters`** (output_control)  string-array `→` Sequence[str]

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
