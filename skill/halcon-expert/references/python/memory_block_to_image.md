# memory_block_to_image (Operator)

## Name

`memory_block_to_image` — Read an image from a memory block with different file formats.

## Signature

`def memory_block_to_image(memory_block_handle: HHandle) -> HObject`

## Description

The operator `memory_block_to_image` reads image data from the indicated
memory block *`memory_block_handle`* and generates the image
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
channels in the usual fashion, [`invert_image`](invert_image.md) must be called after
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

**`image`** (output_object)  image `→` HObject (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Read image.

**`memory_block_handle`** (input_control)  memory_block `→` HHandle

Memory block handle.

## Result

If the parameters are correct the operator `memory_block_to_image`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`read_memory_block`,
`deserialize_tuple`

## Possible Successors

`disp_image`,
`threshold`,
`regiongrowing`,
`count_channels`,
`decompose3`,
`class_ndim_norm`,
`gauss_filter`,
`fill_interlace`,
`zoom_image_size`,
`zoom_image_factor`,
`crop_part`,
`write_image`,
`rgb1_to_gray`

## See also

`image_to_memory_block`

## Module

Foundation
