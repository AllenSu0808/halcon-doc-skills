# TransToRgb (Operator)

## Name

`TransToRgb` — Transform an image from an arbitrary color space to the RGB color space.

## Signature

`static void HOperatorSet.TransToRgb(HObject imageInput1, HObject imageInput2, HObject imageInput3, out HObject imageRed, out HObject imageGreen, out HObject imageBlue, HTuple colorSpace)`

`HImage HImage.TransToRgb(HImage imageInput2, HImage imageInput3, out HImage imageGreen, out HImage imageBlue, string colorSpace)`

## Description

`TransToRgb` transforms an image from an arbitrary color
space (*`colorSpace`*) to the RGB color space. The three
channels of the image are passed as three separate images on input
and output.

The operator `TransToRgb` supports the image types `byte`,
`uint2`, `int4`, and `real`.
The domain of the input images must match the
domain provided by a corresponding transformation with
[`TransFromRgb`](trans_from_rgb.md). If not, the results of the transformation may not
be reasonable.

This includes some scalings in the case of certain image types and
transformations:

- Considering `byte` and `uint2` images, the domain
  of color space values is expected to be spread to the full
  domain of [0..255] or [0..65535], respectively.
  This includes a shift in the case of signed values, such that
  the origin of signed values (e.g., CIELab) may not be at the
  center of the domain.
- Hue values are represented by angles of [0..2$\pi$[
  and are coded for the particular image types differently:

  - `byte`-images map the angle domain on
    [0..255].
  - `uint2`/`int4`-images are coded in
    minutes of arc [0..21600[, except for the transformations
    *"cielchab"* and *"cielchuv"* for
    `int4`-images, where they are coded in
    seconds of arc [0..1296000[.
  - `real`-images are coded in radians
    [0..2$\pi$[, except for the transformations
    *"cielchab"* and *"cielchuv"*, where the
    standards ISO 11664-4:2008 and ISO 11664-5:2009 require the
    hue to be specified in degrees.
- Saturation values are represented by percentages of [0..100]
  and are coded for the particular image type differently:

  - `byte`-images map the saturation values
    to [0..255].
  - `uint2`/`int4`-images map the
    saturation values to [0..10000].
  - `real`-images map the saturation values
    to [0..1].

Supported are the transformations listed below.
Note, all domains are based on RGB values scaled to [0; 1]. To
obtain the domain of a certain image type, they must be
scaled accordingly with the value range.
Due to different precision the values obtained using the given equations
may slightly differ from the values returned by the operator.

- **'yiq'** —

  $$\begin{pmatrix}R \\ G \\ B\end{pmatrix} = \begin{pmatrix}1.0 & 0.946882217 & 0.623556582 \\ 1.0 & -0.267024956 & -0.649523352 \\ 1.0 & -1.108545035 & 1.709006928\end{pmatrix} \begin{pmatrix}Y \\ I \\ Q\end{pmatrix}$$ ![figure](../assets/2af0c8a3f9bc5b86.svg)

  Value range:
  $Y\in[0;1]$,
  $I\in[-0.59947;0.59947]$,
  $Q\in[-0.52243;0.52243]$
- **'yuv'** —

  $$R = Y + \frac{1.0}{0.877} V \\ G = Y - \frac{0.114}{0.493*0.587} U - \frac{0.299}{0.877*0.587} V \\ B = Y + \frac{1.0}{0.493} U$$ ![figure](../assets/668db292fdcf2b74.svg)
  Note, this implies that $Y$, $U$, and $V$ are not
  independent of each other.

  Value range:
  $Y\in[0.0;1.0]$
  $U\in[-0.436798;0.436798]$
  $V\in[-0.614777;0.614777]$
- **'argyb'** —

  $$\begin{pmatrix} R \\ G \\ B \\end{pmatrix} = \begin{pmatrix} 1.00 & 1.29 & 0.22 \\ 1.00 & -0.71 & 0.22 \\ 1.00 & 0.29 & -1.78 \\end{pmatrix} \begin{pmatrix} A \\ Rg \\ Yb \\end{pmatrix}$$ ![figure](../assets/9a683709621c959f.svg)

  Value range:
  $A\in[0;1]$,
  $Rg\in[-0.5;0.5]$,
  $Yb\in[-0.5;0.5]$
- **'ciexyz'** —

  $$\left(\begin{matrix}R\\G\\B\end{matrix}\right) = \left(\begin{matrix}3.240479 & -1.53715 & -0.498535 \\ -0.969256 & 1.875991 & 0.041556 \\ 0.055648 & -0.204043 & 1.057311\end{matrix}\right) \left(\begin{matrix}X\\Y\\Z\end{matrix}\right)$$ ![figure](../assets/0f46076a72863590.svg)

  Value range:
  $X\in[0;0.950456]$
  $Y\in[0;1]$
  $Z\in[0;1.088754]$
- **'cielab'** —

  $$f_y = (L + 16)/116 f_x = a/500 + f_y f_z = b/200 - f_y X = \begin{cases} X_w * f_x^3, & \text{if } f_x > 6/29 \\ (f_x - \tfrac{4}{29}) * X_w * \tfrac{108}{841}, & \text{otherwise} \end{cases} Y = \begin{cases} Y_w * f_y^3, & \text{if } f_y > 6/29 \\ (f_y - \tfrac{4}{29}) * Y_w * \tfrac{108}{841}, & \text{otherwise} \end{cases} Z = \begin{cases} Z_w * f_z^3, & \text{if } f_z > 6/29 \\ (f_z - \tfrac{4}{29}) * Z_w * \tfrac{108}{841}, & \text{otherwise} \end{cases} \begin{pmatrix} R \\ G \\ B \end{pmatrix} = \begin{pmatrix} 3.240479 & -1.53715 & -0.498535 \\\ -0.969256 & 1.875991 & 0.041556 \\\ 0.055648 & -0.204043 & 1.057311 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}$$ ![figure](../assets/7f1aedc74335447c.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $a\in[-86.1813;98.2352]$,
  $b\in[-107.8617;94.4758]$
  (`byte` and `uint2`:
  scaled to the maximum gray value.
  `int4`:
  $L$ is scaled to the maximum gray value,
  $a$ and $b$ is scaled to the minimum gray value,
  such that the origin stays at 0.)
- **'cielchab'** —

  $$a = C_{ab} cos h_{ab}\ b = C_{ab} sin h_{ab}\ f_y = (L + 16)/116\ f_x = a/500 + f_y\ f_z = b/200 - f_y\ X = { \begin{cases} X_w * f^3_x , & \text{if } f_x > \frac{6}{29} \\ (f_x - \frac{4}{29}) * X_w * \frac{108}{841}, & \text{otherwise} \end{cases} \} Y = { \begin{cases} Y_w * f^3_y , & \text{if } f_y > \frac{6}{29} \\ (f_y - \frac{4}{29}) * Y_w * \frac{108}{841}, & \text{otherwise} \end{cases} Z = { \begin{cases} Z_w * f^3_z , & \text{if } f_z > \frac{6}{29} \\ (f_z - \frac{4}{29}) * Z_w * \frac{108}{841}, & \text{otherwise} \end{cases} \begin{pmatrix} R \\ G \\ B \end{pmatrix} = \begin{pmatrix} 3.240479 & -1.537515 & -0.498535 \\ -0.969256 & 1.875991 & 0.041556 \\ 0.055648 & -0.204043 & 1.057311 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}$$ ![figure](../assets/bbc253316a4ff648.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $C\in[0;133.8086]$,
  $h\in[0;360[$
  (`byte`:
  scaled to the maximum gray value.
  `uint2`:
  $L$ and $C$ are scaled to the maximum gray value,
  $h$ is given in minutes of arc.
  `int4`:
  $L$ and $C$ are scaled to the maximum gray value,
  $h$ is given in seconds of arc.)
- **'cieluv'** —

  $$f_y = (L + 16)/116 Y = {\begin{cases} Y_w * f_y^3, &\text{if } f_y > \frac{6}{29}\\ (f_y - \frac{4}{29}) * Y_w * \frac{108}{841}, &\text{otherwise} \end{cases}} u' = \frac{u}{13L} + u'_w v' = \frac{v}{13L} + v'_w x = \frac{u'}{6u' - 16v' +12} y = \frac{4v'}{6u' - 16v' +12} X = \frac{xY}{y} Z = (1 - x - y) \frac{Y}{y} \n( R \\ G \\ B ) = (\begin{pmatrix} 3.240479 & -1.53715 & -0.498535 \\ -0.969256 & 1.875991 & 0.041556 \\ 0.055648 & -0.204043 & 1.057311 \end{pmatrix}) ( X \\ Y \\ Z )$$ ![figure](../assets/80ad37b6bef975f4.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100]$,
  $u\in[-83.0774;175.0148]$,
  $v\in[-134.1008;107.3923]$
  (`byte` and `uint2`:
  scaled to the maximum gray value.
  `int4`:
  $L$ are scaled to the maximum gray value,
  $u$ and $v$ are scaled to the minimum gray value,
  such that the origin stays at 0.)
- **'cielchuv'** —

  $$u = C_{uv} cos h_{uv}\nv = C_{uv} sin h_{uv}\nf_y = (L + 16)/116\nY = \begin{cases} Y_w * f_y^3, & \text{if } f_y > 6/29 \\ (f_y - 4/29) * Y_w * 108/841, & \text{otherwise} \end{cases}\\nu' = \frac{u}{13L} + u'_w\\nv' = \frac{v}{13L} + v'_w\\nx = \frac{9u'}{6w' - 16v' +12}\\ny = \frac{6u' - 16v' +12}{6w' - 16v' +12}\\X = \frac{x}{y} Y \\Z = \left(1 - x - y\right) \frac{Y}{y} \\\\begin{pmatrix} R \\ G \\ B \end{pmatrix} = \begin{pmatrix} 3.240479 & -1.53715 & -0.498535 \\ -0.969256 & 1.875991 & 0.041556 \\ 0.055648 & -0.204043 & 1.057311 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}$$ ![figure](../assets/1c41c4912efd4e80.svg)

  Black point B: ($R_{B}$, $G_{B}$, $B_{B}$) =
  (0, 0, 0)

  White point W (according to image type):

  - `byte`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (255, 255, 255)
  - `uint2`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{16}-1$, $2^{16}-1$,
    $2^{16}-1$)
  - `int4`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    ($2^{31}-1$, $2^{31}-1$,
    $2^{31}-1$)
  - `real`: ($R_{W}$, $G_{W}$, $B_{W}$) =
    (1.0, 1.0, 1.0)

  Value range:
  $L\in[0;100][$,
  $C\in[0;179.0402]$,
  $h\in[0;360[$
  (`byte`:
  scaled to the maximum gray value.
  `uint2`:
  $L$ and $C$ are scaled to the maximum gray value,
  $h$ is given in minutes of arc.
  `int4`:
  $L$ and $C$ are scaled to the maximum gray value,
  $h$ is given in seconds of arc.)
- **'hls'** —

  ```
    Hi := floor(H/rad(60))
    Hf := H/rad(60) - Hi
    if (L <= 0.5)
       Max := L * (S + 1)
    else
       Max := L + S - (L * S)
    endif
    Min := 2 * L - Max
    if (S == 0)
       R := L
       G := L
       B := L
    else
      if (Hi == 0)
         R := Max
         G := Min + Hf * (Max - Min)
         B := Min
      elseif (Hi == 1)
         R := Min + (1 - Hf) * (Max - Min)
         G := Max
         B := Min
      elseif (Hi == 2)
         R := Min
         G := Max
         B := Min + Hf * (Max - Min)
      elseif (Hi == 3)
         R := Min
         G := Min + (1 - Hf) * (Max - Min)
         B := Max
      elseif (Hi == 4)
         R := Min + Hf * (Max - Min)
         G := Min
         B := Max
      elseif (Hi == 5)
         R := Max
         G := Min
         B := Min + (1 - Hf) * (Max - Min)
      endif
    endif
  ```

  Value range:
  $H\in[0;2\pi[$,
  $L\in[0;1]$,
  $S\in[0;1]$
- **'hsi'** —

  $$M1 = S * cos H M2 = S * sin H I1 = I * sqrt{3} ( R \\ G \\ B ) = ( (2/\sqrt{6}) (0) (1/\sqrt{3}) \\ ( -1/\sqrt{6}) (1/\sqrt{2}) (1/\sqrt{3}) \\ ( -1/\sqrt{6}) (-1/\sqrt{2}) (1/\sqrt{3}) ) ( M1 \\ M2 \\ I1 )$$ ![figure](../assets/f6b011c344997203.svg)

  Value range:
  $H\in[0;2\pi[$,
  $S \in [0; \sqrt{\frac{2}{3}}]$ ![figure](../assets/90ea807d5c621940.svg),
  $I\in[0;1]$
- **'hsv'** —

  ```
    if (S == 0)
       R := V
       G := V
       B := V
    else
       Hi := floor(H/rad(60))
       Hf := H/rad(60) - Hi
       if (Hi == 0)
          R := V
          G := V * (1 - (S * (1 - Hf)))
          B := V * (1 - S)
       elseif (Hi == 1)
          R := V * (1 - (S * Hf))
          G := V
          B := V * (1 - S)
       elseif (Hi == 2)
          R := V * (1 - S)
          G := V
          B := V * (1 - (S * (1 - Hf)))
       elseif (Hi == 3)
          R := V * (1 - S)
          G := V * (1 - (S * Hf))
          B := V
       elseif (Hi == 4)
          R := V * (1 - (S * (1 - Hf)))
          G := V * (1 - S)
          B := V
       elseif (Hi == 5)
          R := V
          G := V * (1 - S)
          B := V * (1 - (S * Hf))
       endif
    endif
  ```

  Value range:
  $H\in[0;2\pi[$,
  $S\in[0;1]$,
  $V\in[0;1]$
- **'ciexyz4'** —

  $$\begin{pmatrix} R \\ G \\ B \end{pmatrix} = \begin{pmatrix} 2.750 & -1.149 & -0.426 \\ -1.118 & 2.026 & 0.033 \\ 0.138 & -0.333 & 1.104 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix}$$ ![figure](../assets/24bd447c512ab3b0.svg)

  Value range:
  $X\in[0;0.95]$,
  $Y\in[0;1]$,
  $Z\in[0;1.09]$
- **'lms'** —

  $$\begin{pmatrix}R\\G\\B\end{pmatrix}=\begin{pmatrix}2.585334&-1.628721&-0.024820\\-0.210432&1.158402&0.000321\\-0.041894&-0.118163&1.068973\end{pmatrix}\begin{pmatrix}L\\M\\S\end{pmatrix}$$ ![figure](../assets/e8745b962c2e80bd.svg)

  Value range:
  $L\in[0;0.949280]$,
  $M\in[0;1.035401]$,
  $S\in[0;1.087132]$

## Attention

As the calculations are made with a different numerical precision, the
OpenCL implementation of the cielab transformation for images of type `int4`
is slightly less accurate than the pure C version.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`imageInput1`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Input image (channel 1).

**`imageInput2`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Input image (channel 2).

**`imageInput3`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Input image (channel 3).

**`imageRed`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Red channel.

**`imageGreen`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Green channel.

**`imageBlue`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Blue channel.

**`colorSpace`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Color space of the input image.

Default:
"hsv"

List of values:
"argyb", "cielab", "cielchab", "cielchuv", "cieluv", "ciexyz", "ciexyz4", "hls", "hsi", "hsv", "lms", "yiq", "yuv"

List of values (for compute devices):
"cielab", "cielchab", "cieluv", "cielchuv", "hsv", "hsi"

## Example (HDevelop)

```
* Transformation from rgb to hsv and conversely
read_image(Image,'patras')
dev_display(Image)
decompose3(Image, Image1, Image2, Image3)
trans_from_rgb(Image1,Image2,Image3,ImageH,ImageS,ImageV,'hsv')
trans_to_rgb(ImageH,ImageS,ImageV,ImageR,ImageG,ImageB,'hsv')
compose3(ImageR,ImageG,ImageB,Multichannel)
dev_display(Multichannel)
```

## Result

`TransToRgb` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result', <Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`Decompose3`

## Possible Successors

`Compose3`,
`DispColor`

## Alternatives

`LinearTransColor`

## See also

`Decompose3`,
`TransFromRgb`

## References

ITU-R BT.470-6: “Conventional Television Systems”, 1998.
  
ISO 11664-4:2008: “Colorimetry --- Part 4: CIE 1976 L*a*b* Colour
space”, 2008.
  
ISO 11664-5:2009: “Colorimetry --- Part 5: CIE 1976 L*u*v* Colour
space and u',v' uniform chromaticity scale diagram”, 2009.

## Module

Foundation
