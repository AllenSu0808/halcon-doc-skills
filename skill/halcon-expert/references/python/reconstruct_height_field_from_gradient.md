# reconstruct_height_field_from_gradient (Operator)

## Name

`reconstruct_height_field_from_gradient` — Reconstruct a surface from surface gradients.

## Signature

`def reconstruct_height_field_from_gradient(gradient: HObject, reconstruction_method: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HObject`

## Description

`reconstruct_height_field_from_gradient` reconstructs a surface from
the surface gradients that are given in *`gradient`*. The surface
is returned as a height field, i.e., an image in which the gray value of each
image point corresponds to a relative height.

The reconstruction is done by integrating the gradients by different
algorithms that can be selected in the parameter
*`reconstruction_method`*. Because gradient fields are typically
non-integrable due to noise, the various algorithms return a solution in a
least-squares sense. The algorithms differ in the way how they model the
boundary condition. Currently three algorithms are supported:
*"fft_cyclic"*, *"rft_cyclic"* and *"poisson"*.

**Reconstruction with Fast Fourier transforms**

The variants *"fft_cyclic"* and *"rft_cyclic"* assume that the
image function is cyclic at the boundaries. Note that due to the assumed
cyclic image function artifacts may occur at the image boundaries. Thus, in
most cases, we recommend to use the *"poisson"* algorithm instead.

The difference between *"fft_cyclic"* and *"rft_cyclic"* is that
the rft version has faster processing times and requires less memory than
the fft version. While theoretically fft and rft should return the same
result, the fft version is numerically slightly more accurate. As
`reconstruct_height_field_from_gradient` internally uses a fast Fourier
transform, the run time of the operator can be influenced by a previous call
to [`optimize_fft_speed`](optimize_fft_speed.md) or [`optimize_rft_speed`](optimize_rft_speed.md), respectively.

**Reconstruction according to Poisson**

The *"poisson"* algorithm assumes that the image has constant gradients
at the image border. In most cases, it is the recommended reconstruction
method for `reconstruct_height_field_from_gradient`. Its run time can
only be optimized by setting *`gen_param_name`* to *"optimize_speed"*
and *`gen_param_value`* to *"standard"*, *"patient"*, or
*"exhaustive"*. These parameters are described in more detail with the
description of [`optimize_fft_speed`](optimize_fft_speed.md).

Note that by default, the *"poisson"* algorithm uses a cache that
depends on the image size and that speeds up the reconstruction
significantly, provided that all images have the same size. The cache is
allocated at the first time when the *"poisson"* algorithm is
called. Therefore the first call always takes longer than subsequent
calls. The additionally needed memory corresponds to the memory needed for
the specific size of one image. Please note that when calling the operator
with different image sizes, the cache needs to be reallocated, which leads to
a longer processing time. In this case it may be preferable to not use the
cache. To switch off the caching, you must set the parameter
*`gen_param_name`* to *"caching"* and the parameter
*`gen_param_value`* to *"no_cache"*. The cache can explicitly be
deallocated by setting *`gen_param_name`* to *"caching"* and
*`gen_param_value`* to *"free_cache"*. However, in the majority of
cases, we recommend to use the cache, i.e., to use the default setting for
the parameter *"caching"*.

**Saving and loading optimization parameters**

The optimization parameters for all algorithms can be saved and loaded by
[`write_fft_optimization_data`](write_fft_optimization_data.md) and [`read_fft_optimization_data`](read_fft_optimization_data.md).

**Non obvious applications**

Please note that the operator `reconstruct_height_field_from_gradient`
has various non-obvious applications, especially in the field called gradient
domain manipulation technique. In many applications, the gradient values that
are passed as input to the operator do not have the semantics of surface
gradients (i.e., the first derivatives of the height values), but are rather
the first derivatives of other kinds of parameters, typically gray values
(then, the gradients have the semantics of gray value edges). When processing
these gradient images by various means, e.g., by adding or subtracting
images, or by a filtering, the original gradient values are altered and the
subsequent call to `reconstruct_height_field_from_gradient` delivers a
modified image, in which, e.g., unwanted edges are removed or the contrast
has been changed locally. Typical applications are noise removal, seamless
fusion of images, or high dynamic range compression.

## Attention

`reconstruct_height_field_from_gradient` takes into account the values
of all pixels in *`gradient`*, not only the values within its domain.
If *`gradient`* does not have a full domain, one could cut out the
relevant square part of the gradient field and generate a
smaller image with full domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`gradient`** (input_object)  singlechannelimage `→` HObject (vector_field)

The gradient field of the image.

**`height_field`** (output_object)  image `→` HObject (real)

Reconstructed height field.

**`reconstruction_method`** (input_control)  string `→` str

Type of the reconstruction method.

Default:
"poisson"

List of values:
"fft_cyclic", "poisson", "rft_cyclic"

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"caching", "optimize_speed"

**`gen_param_value`** (input_control)  integer-array `→` Sequence[Union[int, float, str]]

Values of the generic parameters.

Default:
[]

List of values:
"exhaustive", "free_cache", "no_cache", "patient", "standard", "use_cache"

## Result

If the parameters are valid `reconstruct_height_field_from_gradient`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## References

M. Kazhdan, M. Bolitho, and H. Hoppe: “Poisson Surface Reconstruction.”
Symposium on Geometry Processing (June 2006).

## Module

3D Metrology
