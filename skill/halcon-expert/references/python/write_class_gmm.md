# write_class_gmm (Operator)

## Name

`write_class_gmm` — Write a Gaussian Mixture Model to a file.

## Signature

`def write_class_gmm(gmmhandle: HHandle, file_name: str) -> None`

## Description

`write_class_gmm` writes the Gaussian Mixture Model (GMM)
*`gmmhandle`* to the file given by *`file_name`*.
The default HALCON file extension for the GMM classifier is 'ggc'.
`write_class_gmm` is typically called after the GMM has been
trained with [`train_class_gmm`](train_class_gmm.md). The GMM can be read with
[`read_class_gmm`](read_class_gmm.md). `write_class_gmm` does *not*
write any training samples that possibly have been stored in the
GMM. For this purpose, [`write_samples_class_gmm`](write_samples_class_gmm.md) should be
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gmmhandle`** (input_control)  class_gmm `→` HHandle

GMM handle.

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`ggc`

## Result

If the parameters are valid, the operator `write_class_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`train_class_gmm`

## Possible Successors

`clear_class_gmm`

## See also

`create_class_gmm`,
`read_class_gmm`,
`write_samples_class_gmm`

## Module

Foundation
