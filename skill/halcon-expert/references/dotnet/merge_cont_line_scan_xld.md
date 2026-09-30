# MergeContLineScanXld (Operator)

## Name

`MergeContLineScanXld` — Merge XLD contours from successive line scan images.

## Signature

`static void HOperatorSet.MergeContLineScanXld(HObject currConts, HObject prevConts, out HObject currMergedConts, out HObject prevMergedConts, HTuple imageHeight, HTuple margin, HTuple mergeBorder, HTuple maxImagesCont)`

`HXLDCont HXLDCont.MergeContLineScanXld(HXLDCont prevConts, out HXLDCont prevMergedConts, int imageHeight, HTuple margin, string mergeBorder, int maxImagesCont)`

`HXLDCont HXLDCont.MergeContLineScanXld(HXLDCont prevConts, out HXLDCont prevMergedConts, int imageHeight, double margin, string mergeBorder, int maxImagesCont)`

## Description

The operator `MergeContLineScanXld` connects adjacent XLD
contours, which were extracted from adjacent images with the height
*`imageHeight`*. This operator was especially designed to
connect contours that were extracted from images grabbed by a
line scan camera. *`currConts`* contains the contours from the
current image and *`prevConts`* the contours from the previous
one.

With the help of the parameter *`mergeBorder`* two cases can be
distinguished: If the top (first) line of the current image touches
the bottom (last) line of the previous image, *`mergeBorder`*
must be set to *"top"*, otherwise set *`mergeBorder`* to
*"bottom"*. *`mergeBorder`* defines a margin to the
border. Only those end points of the contours which are inside this
margin are considered for the following merging process.

If the operator `MergeContLineScanXld` is used
recursively, the parameter *`maxImagesCont`* determines the
maximum number of images which are covered by a merged contour. All
points of the merged contour from an older image are removed.

The operator `MergeContLineScanXld` returns two contour
arrays. *`prevMergedConts`* contains all those contours from the
previous input contours *`prevConts`*, which could not be merged
with a current contour. *`currMergedConts`* collects all current
contours together with the merged parts from the previous images.
Merged contours will exceed the original image, because the previous
contours are moved upward (*`mergeBorder`*=*"top"*) or
downward (*`mergeBorder`*=*"bottom"*) according to the
image height.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`currConts`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Current input contours.

**`prevConts`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Merged contours from the previous iteration.

**`currMergedConts`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Current contours, merged with old ones where applicable.

**`prevMergedConts`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours from the previous iteration which could not be
merged with the current ones.

**`imageHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the line scan images.

Default:
512

Suggested values:
240, 480, 512

**`margin`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum distance of contours from the image border.

Default:
0.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0

**`mergeBorder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Image line of the current image, which touches the
previous image.

Default:
"top"

List of values:
"bottom", "top"

**`maxImagesCont`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of images covered by one contour.

Default:
3

Suggested values:
1, 2, 3, 4, 5

## Result

The operator `MergeContLineScanXld` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

Foundation
