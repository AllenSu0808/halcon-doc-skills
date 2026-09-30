# ProtectOcrTrainf (Operator)

## Name

`ProtectOcrTrainf` — Protection of training data.

## Signature

`static void HOperatorSet.ProtectOcrTrainf(HTuple trainingFile, HTuple password, HTuple trainingFileProtected)`

`static void HRegion.ProtectOcrTrainf(string trainingFile, HTuple password, string trainingFileProtected)`

`static void HRegion.ProtectOcrTrainf(string trainingFile, string password, string trainingFileProtected)`

## Description

Obtaining training data for an OCR classifier can be a complicated and
time consuming activity. Thus, training data is valuable and there
might be the necessity to protect its usage. The general idea
is to prevent protected OCR training data from being
reviewed or modified in any way and to ensure that its usage, e.g.,
training an OCR classifier, is restricted by a user password.

The approach in HALCON is to obtain OCR training data in the usual way,
then write it to an unprotected OCR training file using, e.g.,
[`WriteOcrTrainf`](write_ocr_trainf.md), and afterwards create a new file containing
the OCR training data protected with a user password. Protected training
files can be used with a set of special operators
that also require the correct password in order to be able to process the
data, e.g., for training an OCR classifier.

It is important to keep in mind that data in a protected OCR training
file cannot be reviewed or modified in any way, thus it is important to
keep the original, unprotected, training data files.

Protected OCR training data can be used for training of multilayer
perceptron (MLP) classifiers and support vector machine (SVM) classifiers.

`ProtectOcrTrainf` protects the OCR training data contained
in the file *`trainingFile`* and writes it to
the protected training data file *`trainingFileProtected`*.
The protection is done with the user password *`password`*. The
same password has to be used afterwards in order to use the protected
OCR training data, e.g., by the operators
[`TrainfOcrClassMlpProtected`](trainf_ocr_class_mlp_protected.md) or
[`ReadOcrTrainfNamesProtected`](read_ocr_trainf_names_protected.md). Empty passwords (or passwords
containing the empty string) are not allowed. If the number of passwords
*`password`* equals 1, then every output file
*`trainingFileProtected`* is protected with that password,
otherwise the number of passwords has to be equal to the number of
input and output files and the output file at position n is protected
with the password at position n.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`trainingFile`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Names of the training files.

Default:
""

File extension:
.`trf`, .`otr`

**`password`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Passwords for protecting the training files.

**`trainingFileProtected`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Names of the protected training files.

File extension:
.`trf`

## Result

If the parameters are correct, the operator
`ProtectOcrTrainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`WriteOcrTrainf`,
`AppendOcrTrainf`,
`ConcatOcrTrainf`

## Possible Successors

`ReadOcrTrainfNamesProtected`,
`TrainfOcrClassMlpProtected`,
`TrainfOcrClassSvmProtected`,
`SelectFeatureSetTrainfMlpProtected`,
`SelectFeatureSetTrainfSvmProtected`

## See also

`SelectFeatureSetTrainfMlp`

## Module

OCR/OCV
