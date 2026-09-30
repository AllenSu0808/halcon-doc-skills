# SelectFeatureSetTrainfSvmProtected (Operator)

## Name

`SelectFeatureSetTrainfSvmProtected` — Select an optimal combination of features to classify OCR data
from a (protected) training file.

## Signature

`static void HOperatorSet.SelectFeatureSetTrainfSvmProtected(HTuple trainingFile, HTuple password, HTuple featureList, HTuple selectionMethod, HTuple width, HTuple height, HTuple genParamName, HTuple genParamValue, out HTuple OCRHandle, out HTuple featureSet, out HTuple score)`

`HTuple HOCRSvm.SelectFeatureSetTrainfSvmProtected(HTuple trainingFile, HTuple password, HTuple featureList, string selectionMethod, int width, int height, HTuple genParamName, HTuple genParamValue, out HTuple score)`

`HTuple HOCRSvm.SelectFeatureSetTrainfSvmProtected(string trainingFile, string password, string featureList, string selectionMethod, int width, int height, HTuple genParamName, HTuple genParamValue, out HTuple score)`

## Description

`SelectFeatureSetTrainfSvmProtected` selects an optimal
combination of features to classify the data given in the training files
*`trainingFile`* with a support vector machine (SVM). Its functionality
corresponds to the functionality of [`SelectFeatureSetTrainfSvm`](select_feature_set_trainf_svm.md),
with the addition that `SelectFeatureSetTrainfSvmProtected`
can process unprotected and protected training files. Protected
training files can be used only with the correct user password
*`password`*. If the number of passwords *`password`*
equals 1, then every input file *`trainingFile`* is checked
with that password, otherwise the number of passwords has to be
equal to the number of input files and the input file at position
n is checked with the password at position n. For unprotected
training files the passwords are ignored.

For a more detailed description of the operator's functionality see
[`SelectFeatureSetTrainfSvm`](select_feature_set_trainf_svm.md). The concept of protecting OCR
training data in HALCON is described in [`ProtectOcrTrainf`](protect_ocr_trainf.md).

## Attention

This operator may take considerable time, depending on the size of the
data set in the training file, and the number of features.

Please note, that this operator should not be called, if only a small
set of training data is available. Due to the risk of overfitting the
operator `SelectFeatureSetTrainfSvmProtected` may deliver a
classifier with a very high score. However, the classifier may perform
poorly when tested.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`trainingFile`** (input_control)  filename.read(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`password`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Passwords for protected training files.

**`featureList`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

List of features that should be considered for selection.

Default:
["zoom_factor","ratio","width","height","foreground","foreground_grid_9","foreground_grid_16","anisometry","compactness","convexity","moments_region_2nd_invar","moments_region_2nd_rel_invar","moments_region_3rd_invar","moments_central","phi","num_connect","num_holes","projection_horizontal","projection_vertical","projection_horizontal_invar","projection_vertical_invar","chord_histo","num_runs","pixel","pixel_invar","pixel_binary","gradient_8dir","cooc","moments_gray_plane"]

List of values:
"anisometry", "chord_histo", "compactness", "convexity", "cooc", "default", "foreground", "foreground_grid_16", "foreground_grid_9", "gradient_8dir", "height", "moments_central", "moments_gray_plane", "moments_region_2nd_invar", "moments_region_2nd_rel_invar", "moments_region_3rd_invar", "num_connect", "num_holes", "num_runs", "phi", "pixel", "pixel_binary", "pixel_invar", "projection_horizontal", "projection_horizontal_invar", "projection_vertical", "projection_vertical_invar", "ratio", "width", "zoom_factor"

**`selectionMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method to perform the selection.

Default:
"greedy"

List of values:
"greedy", "greedy_oscillating"

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
15

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
16

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of generic parameters to configure the selection
process and the classifier.

Default:
[]

List of values:
"gamma", "nu"

**`genParamValue`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of generic parameters to configure the selection
process and the classifier.

Default:
[]

Suggested values:
"auto", "0.1", "0.3"

**`OCRHandle`** (output_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Trained OCR-SVM Classifier.

**`featureSet`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Selected feature set, contains only entries from
*`featureList`*.

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Achieved score using tow-fold cross-validation.

## Result

If the parameters are valid, the operator
`SelectFeatureSetTrainfSvmProtected` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ProtectOcrTrainf`

## Alternatives

`SelectFeatureSetTrainfMlpProtected`

## See also

`SelectFeatureSetTrainfSvm`,
`SelectFeatureSetSvm`

## Module

OCR/OCV
