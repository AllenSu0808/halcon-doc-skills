# MemoryBlockToImage (Operator)

## Name

`MemoryBlockToImage` — Read an image from a memory block with different file formats.

## Signature

`static void HOperatorSet.MemoryBlockToImage(out HObject image, HTuple memoryBlockHandle)`

`void HImage.MemoryBlockToImage(HMemoryBlock memoryBlockHandle)`

## Description

The operator `MemoryBlockToImage` reads image data from the indicated
memory block *`memoryBlockHandle`* and generates the image
*`image`*.

The formats JPEG and PNG can be read. The file formats are recognized by the
internal structure of the memory block. In case of colored images an image
with three color channels is created, the red channel being stored in the
first, the green channel in the second and the blue channel in the third
component (channel number).

For the PNG image format binary alpha channels are interpreted as domains.
Otherwise, the domain of the generated image object (all pixels of the matrix)
is chosen maximal.

## Attention

If CMYK or YCCK JPEG memory blocks are read, HALCON assumes that these follow
the Adobe Photoshop convention that the CMYK channels are stored inverted,
i.e., 0 represents 100% ink coverage, rather than 0% ink as one would
expect. The images are converted to RGB images using this convention. If the
JPEG memory block does not follow this convention, but stores the CMYK
channels in the usual fashion, [`InvertImage`](invert_image.md) must be called after
reading the image.

If PNG images that contain an alpha channel are read, the alpha channel is
returned as the second or fourth channel of the output image, unless the alpha
channel contains exactly two different gray values, in which case a one or
three channel image with a reduced domain is returned, in which the points in
the domain correspond to the points with the higher gray value in the alpha
channel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Read image.

**`memoryBlockHandle`** (input_control)  memory_block `→` [HMemoryBlock](HMemoryBlock.md), [HTuple](HTuple.md) (*IntPtr*)

Memory block handle.

## Result

If the parameters are correct the operator `MemoryBlockToImage`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`ReadMemoryBlock`,
`DeserializeTuple`

## Possible Successors

`DispImage`,
`Threshold`,
`Regiongrowing`,
`CountChannels`,
`Decompose3`,
`ClassNdimNorm`,
`GaussFilter`,
`FillInterlace`,
`ZoomImageSize`,
`ZoomImageFactor`,
`CropPart`,
`WriteImage`,
`Rgb1ToGray`

## See also

`ImageToMemoryBlock`

## Module

Foundation
