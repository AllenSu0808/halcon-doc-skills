# HImage (Class)

## Name

`HImage` — Represents an instance of an image object(-array).

## Base Class

`HObject` — Represents an instance of an iconic object(-array).
Base class for images, regions and XLDs

## Constructors

|  |  |  |
| --- | --- | --- |
| `GenImage1` |  | Create an image from a pointer to the pixels. |
| `GenImageConst` |  | Create an image with constant gray value. |
| `ReadImage` |  | Read an image with different file formats. |

## Finalizer

This operator is not available as a class member but will be called automatically when the resources of the object instances are to be released. This occurs in the finalization stage of garbage collection, or upon an explicit call of the Dispose() method.

|  |  |  |
| --- | --- | --- |
| `ClearObj` |  | Delete an iconic object from the database. |

## Methods

|  |  |  |
| --- | --- | --- |
| `AbsDiffImage` |  | Calculate the absolute difference of two images. |
| `AbsImage` |  | Calculate the absolute value (modulus) of an image. |
| `AccessChannel` |  | Access a channel of a multi-channel image. |
| `AcosImage` |  | Calculate the arccosine of an image. |
| `AddImage` |  | Add two images. |
| `AddImageBorder` |  | Add a border to an image. |
| `AddNoiseDistribution` |  | Add noise to an image. |
| `AddNoiseWhite` |  | Add noise to an image. |
| `AddSamplesImageClassGmm` |  | Add training samples from an image to the training data of a Gaussian Mixture Model. |
| `AddSamplesImageClassKnn` |  | Add training samples from an image to the training data of a k-Nearest-Neighbor classifier. |
| `AddSamplesImageClassMlp` |  | Add training samples from an image to the training data of a multilayer perceptron. |
| `AddSamplesImageClassSvm` |  | Add training samples from an image to the training data of a support vector machine. |
| `AddTextureInspectionModelImage` |  | Add training images to the texture inspection model. |
| `AdjustMosaicImages` |  | Apply an automatic color correction to panorama images. |
| `AffineTransImage` |  | Apply an arbitrary affine 2D transformation to images. |
| `AffineTransImageSize` |  | Apply an arbitrary affine 2D transformation to an image and specify the output image size. |
| `AnisotropicDiffusion` |  | Perform an anisotropic diffusion of an image. |
| `AppendChannel` |  | Append additional matrices (channels) to the image. |
| `ApplyColorTransLut` |  | Color space transformation using pre-generated look-up-table. |
| `ApplySheetOfLightCalibration` |  | Apply the calibration transformations to the input disparity image. |
| `ApplyTextureInspectionModel` |  | Inspection of the texture within an image. |
| `AreaCenterGray` |  | Compute the area and center of gravity of a region in a gray value image. |
| `AsinImage` |  | Calculate the arcsine of an image. |
| `Atan2Image` |  | Calculate the arctangent of two images. |
| `AtanImage` |  | Calculate the arctangent of an image. |
| `AutoThreshold` |  | Segment an image using thresholds determined from its histogram. |
| `BandpassImage` |  | Edge extraction using bandpass filters. |
| `BilateralFilter` |  | bilateral filtering of an image. |
| `BinThreshold` |  | Segment an image using an automatically determined threshold. |
| `BinaryThreshold` |  | Segment an image using binary thresholding. |
| `BinocularDisparity` |  | Compute the disparities of a rectified image pair using correlation techniques. |
| `BinocularDisparityMg` |  | Compute the disparities of a rectified stereo image pair using multigrid methods. |
| `BinocularDisparityMs` |  | Compute the disparities of a rectified stereo image pair using multi-scanline optimization. |
| `BinocularDistance` |  | Compute the distance values for a rectified stereo image pair using correlation techniques. |
| `BinocularDistanceMg` |  | Compute the distance values for a rectified stereo image pair using multigrid methods. |
| `BinocularDistanceMs` |  | Compute the distance values for a rectified stereo image pair using multi-scanline optimization. |
| `BinomialFilter` |  | Smooth an image using the binomial filter. |
| `BitAnd` |  | Bit-by-bit AND of all pixels of the input images. |
| `BitLshift` |  | Left shift of all pixels of the image. |
| `BitMask` |  | Logical “AND” of each pixel using a bit mask. |
| `BitNot` |  | Complement all bits of the pixels. |
| `BitOr` |  | Bit-by-bit OR of all pixels of the input images. |
| `BitRshift` |  | Right shift of all pixels of the image. |
| `BitSlice` |  | Extract a bit from the pixels. |
| `BitXor` |  | Bit-by-bit XOR of all pixels of the input images. |
| `CfaToRgb` |  | Convert a single-channel color filter array image into an RGB image. |
| `ChangeDomain` |  | Change definition domain of an image. |
| `ChangeFormat` |  | Change image size. |
| `ChangeRadialDistortionImage` |  | Change the radial distortion of an image. |
| `ChannelsToImage` |  | Convert one-channel images into a multi-channel image |
| `CharThreshold` |  | Perform a threshold segmentation for extracting characters. |
| `CheckDifference` |  | Compare two images pixel by pixel. |
| `Class2dimSup` |  | Segment an image using two-dimensional pixel classification. |
| `Class2dimUnsup` |  | Segment two images by clustering. |
| `ClassNdimNorm` |  | Classify pixels using hyper-spheres or hyper-cubes. |
| `ClassifyImageClassGmm` |  | Classify an image with a Gaussian Mixture Model. |
| `ClassifyImageClassKnn` |  | Classify an image with a k-Nearest-Neighbor classifier. |
| `ClassifyImageClassLut` |  | Classify a byte image using a look-up table. |
| `ClassifyImageClassMlp` |  | Classify an image with a multilayer perceptron. |
| `ClassifyImageClassSvm` |  | Classify an image with a support vector machine. |
| `ClearColorTransLut` |  | Release the look-up-table needed for color space transformation. |
| `ClusterModelComponents` |  | Adopt new parameters that are used to create the model components into the training result. |
| `CoherenceEnhancingDiff` |  | Perform a coherence enhancing diffusion of an image. |
| `CompareExtVariationModel` |  | Compare an image to a variation model. |
| `CompareObj` |  | Compare iconic objects regarding equality. |
| `CompareVariationModel` |  | Compare an image to a variation model. |
| `ComplexToReal` |  | Convert a complex image into two real images. |
| `Compose2` |  | Convert two images into a two-channel image. |
| `Compose3` |  | Convert 3 images into a three-channel image. |
| `Compose4` |  | Convert 4 images into a four-channel image. |
| `Compose5` |  | Convert 5 images into a five-channel image. |
| `Compose6` |  | Convert 6 images into a six-channel image. |
| `Compose7` |  | Convert 7 images into a seven-channel image. |
| `ConcatObj` |  | Concatenate two iconic object tuples. |
| `ConnectGridPoints` |  | Establish connections between the grid points of the rectification grid. |
| `ConvertImageType` |  | Convert the type of an image. |
| `ConvertMapType` |  | Convert image maps into other map types. |
| `ConvolChannels` |  | Perform a convolution along the channel dimension. |
| `ConvolFft` |  | Multiply an image with a filter image in the frequency domain. |
| `ConvolGabor` |  | Convolve an image with a Gabor filter in the frequency domain. |
| `ConvolImage` |  | Calculate the correlation between an image and an arbitrary filter mask |
| `CoocFeatureImage` |  | Calculate a co-occurrence matrix and derive gray value features thereof. |
| `CoocFeatureMatrix` |  | Calculate gray value features from a co-occurrence matrix. |
| `CopyImage` |  | Copy an image and allocate new memory for it. |
| `CopyObj` |  | Copy an iconic object in the database. |
| `CornerResponse` |  | Searching corners in images. |
| `CorrelationFft` |  | Multiply one image with the complex conjugate of another image in the frequency domain. |
| `CosImage` |  | Calculate the cosine of an image. |
| `CountChannels` |  | Count channels of image. |
| `CreateAnisoShapeModel` |  | Prepare an anisotropically scaled shape model for matching. |
| `CreateBgEsti` |  | Generate and initialize a data set for the background estimation. |
| `CreateCalibDescriptorModel` |  | Create a descriptor model for calibrated perspective matching. |
| `CreateColorTransLut` |  | Creates the look-up-table for transformation of an image from the RGB color space to an arbitrary color space. |
| `CreateComponentModel` |  | Prepare a component model for matching based on explicitly specified components and relations. |
| `CreateLocalDeformableModel` |  | Creates a deformable model for local, deformable matching. |
| `CreateNccModel` |  | Prepare an NCC model for matching. |
| `CreatePlanarCalibDeformableModel` |  | Create a deformable model for calibrated perspective matching. |
| `CreatePlanarUncalibDeformableModel` |  | Creates a deformable model for uncalibrated, perspective matching. |
| `CreateScaledShapeModel` |  | Prepare an isotropically scaled shape model for matching. |
| `CreateShapeModel` |  | Prepare a shape model for matching. |
| `CreateUncalibDescriptorModel` |  | Prepare a descriptor model for interest point matching. |
| `CriticalPointsSubPix` |  | Subpixel precise detection of critical points in an image. |
| `CropDomain` |  | Cut out of defined gray values. |
| `CropDomainRel` |  | Cut out an image area relative to the domain. |
| `CropPart` |  | Cut out one or more rectangular image areas. |
| `CropRectangle1` |  | Cut out one or more rectangular image areas. |
| `CropRectangle2` |  | Cut out one or more arbitrarily oriented rectangular image areas. |
| `DecodeBarCodeRectangle2` |  | Decode bar code symbols within a rectangle. |
| `Decompose2` |  | Convert a two-channel image into two images. |
| `Decompose3` |  | Convert a three-channel image into three images. |
| `Decompose4` |  | Convert a four-channel image into four images. |
| `Decompose5` |  | Convert a five-channel image into five images. |
| `Decompose6` |  | Convert a six-channel image into six images. |
| `Decompose7` |  | Convert a seven-channel image into seven images. |
| `DepthFromFocus` |  | Extract depth using multiple focus levels. |
| `DerivateGauss` |  | Convolve an image with derivatives of the Gaussian. |
| `DerivateVectorField` |  | Convolve a vector field with derivatives of the Gaussian. |
| `DeserializeImage` |  | Deserialize a serialized image object. |
| `DetectEdgeSegments` |  | Detect straight edge segments. |
| `DetermineDeformableModelParams` |  | Determine the parameters of a deformable model. |
| `DetermineShapeModelParams` |  | Determine the parameters of a shape model. |
| `DeviationImage` |  | Calculate the standard deviation of gray values within rectangular windows. |
| `DeviationN` |  | Calculate standard deviation over several channels. |
| `DiffOfGauss` |  | Approximate the LoG operator (Laplace of Gaussian). |
| `DispChannel` |  | Displays images with several channels. |
| `DispColor` |  | Displays a color (RGB) image |
| `DispImage` |  | Displays gray value images. |
| `DisparityImageToXyz` |  | Transform a disparity image into 3D points in a rectified stereo system. |
| `DivImage` |  | Divide two images. |
| `DoOcvSimple` |  | Verification of a pattern using an OCV tool. |
| `DotsImage` |  | Enhance circular dots in an image. |
| `DualRank` |  | Opening, Median and Closing with circle or rectangle mask. |
| `DualThreshold` |  | Threshold operator for signed images. |
| `DumpWindowImage` |  | Write the window content in an image object. |
| `DynThreshold` |  | Segment an image using a local threshold. |
| `EdgesColor` |  | Extract color edges using Canny, Deriche, or Shen filters. |
| `EdgesColorSubPix` |  | Extract subpixel precise color edges using Deriche, Shen, or Canny filters. |
| `EdgesImage` |  | Extract edges using Deriche, Lanser, Shen, or Canny filters. |
| `EdgesSubPix` |  | Extract sub-pixel precise edges using Deriche, Lanser, Shen, or Canny filters. |
| `EliminateMinMax` |  | Smooth an image in the spatial domain to suppress noise. |
| `EliminateSp` |  | Replace values outside of thresholds with average value. |
| `EllipticAxisGray` |  | Compute the orientation and major axes of a region in a gray value image. |
| `Emphasize` |  | Enhance contrast of the image. |
| `EnergyGabor` |  | Calculate the energy of a two-channel image. |
| `EntropyGray` |  | Determine the entropy and anisotropy of images. |
| `EntropyImage` |  | Calculate the entropy of gray values within a rectangular window. |
| `EquHistoImage` |  | Histogram linearization of images |
| `EquHistoImageRect` |  | Histogram linearization within a rectangluar mask. |
| `EstimateAlAm` |  | Estimate the albedo of a surface and the amount of ambient light. |
| `EstimateNoise` |  | Estimate the image noise from a single image. |
| `EstimateSlAlLr` |  | Estimate the slant of a light source and the albedo of a surface. |
| `EstimateSlAlZc` |  | Estimate the slant of a light source and the albedo of a surface. |
| `EstimateTiltLr` |  | Estimate the tilt of a light source. |
| `EstimateTiltZc` |  | Estimate the tilt of a light source. |
| `ExhaustiveMatch` |  | Matching of a template and an image. |
| `ExhaustiveMatchMg` |  | Matching a template and an image in a resolution pyramid. |
| `ExpImage` |  | Calculate the exponentiation of an image. |
| `ExpandDomainGray` |  | Expand the domain of an image and set the gray values in the expanded domain. |
| `ExpandGray` |  | Fill gaps between regions (depending on gray value or color) or split overlapping regions. |
| `ExpandGrayRef` |  | Fill gaps between regions (depending on gray value or color) or split overlapping regions. |
| `ExpandLine` |  | Expand a region starting at a given line. |
| `FastThreshold` |  | Fast thresholding of images using global thresholds. |
| `FftGeneric` |  | Compute the fast Fourier transform of an image. |
| `FftImage` |  | Compute the fast Fourier transform of an image. |
| `FftImageInv` |  | Compute the inverse fast Fourier transform of an image. |
| `FillInterlace` |  | Interpolate 2 video half images. |
| `FindAnisoShapeModel` |  | Find the best matches of an anisotropically scaled shape model in an image. |
| `FindAnisoShapeModels` |  | Find the best matches of multiple anisotropically scaled shape models. |
| `FindBarCode` |  | Detect and read bar code symbols in an image. |
| `FindCalibDescriptorModel` |  | Find the best matches of a calibrated descriptor model in an image and return their 3D pose. |
| `FindCaltab` |  | Segment the region of a standard calibration plate with rectangularly arranged marks in the image. |
| `FindComponentModel` |  | Find the best matches of a component model in an image. |
| `FindDataCode2d` |  | Detect and read 2D code symbols in an image or train the 2D code model. |
| `FindGenericShapeModel` |  | Find the best matches of one or multiple shape models in an image. |
| `FindLocalDeformableModel` |  | Find the best matches of a local deformable model in an image. |
| `FindMarksAndPose` |  | Extract rectangularly arranged 2D calibration marks from the image and calculate initial values for the external camera parameters. |
| `FindNccModel` |  | Find the best matches of an NCC model in an image. |
| `FindNccModels` |  | Find the best matches of multiple NCC models. |
| `FindPlanarCalibDeformableModel` |  | Find the best matches of a calibrated deformable model in an image and return their 3D pose. |
| `FindPlanarUncalibDeformableModel` |  | Find the best matches of a planar projective invariant deformable model in an image. |
| `FindRectificationGrid` |  | Segment the rectification grid region in the image. |
| `FindScaledShapeModel` |  | Find the best matches of an isotropically scaled shape model in an image. |
| `FindScaledShapeModels` |  | Find the best matches of multiple isotropically scaled shape models. |
| `FindShapeModel` |  | Find the best matches of a shape model in an image. |
| `FindShapeModel3d` |  | Find the best matches of a 3D shape model in an image. |
| `FindShapeModels` |  | Find the best matches of multiple shape models. |
| `FindText` |  | Find text in an image. |
| `FindUncalibDescriptorModel` |  | Find the best matches of a descriptor model in an image. |
| `FitSurfaceFirstOrder` |  | Calculate gray value moments and approximation by a first order surface (plane). |
| `FitSurfaceSecondOrder` |  | Calculate gray value moments and approximation by a second order surface. |
| `FreiAmp` |  | Detect edges (amplitude) using the Frei-Chen operator. |
| `FreiDir` |  | Detect edges (amplitude and direction) using the Frei-Chen operator. |
| `FullDomain` |  | Expand the domain of an image to maximum. |
| `FuzzyEntropy` |  | Determine the fuzzy entropy of regions. |
| `FuzzyMeasurePairing` |  | Extract straight edge pairs perpendicular to a rectangle or an annular arc. |
| `FuzzyMeasurePairs` |  | Extract straight edge pairs perpendicular to a rectangle or an annular arc. |
| `FuzzyMeasurePos` |  | Extract straight edges perpendicular to a rectangle or an annular arc. |
| `FuzzyPerimeter` |  | Calculate the fuzzy perimeter of a region. |
| `GammaImage` |  | Perform a gamma encoding or decoding of an image. |
| `GaussFilter` |  | Smooth using discrete Gauss functions. |
| `GaussImage` |  | Smooth an image using discrete Gaussian functions. |
| `GenBandfilter` |  | Generate an ideal band filter. |
| `GenBandpass` |  | Generate an ideal bandpass filter. |
| `GenBinocularProjRectification` |  | Compute the projective rectification of weakly calibrated binocular stereo images. |
| `GenBinocularRectificationMap` |  | Generate transformation maps that describe the mapping of the images of a binocular camera pair to a common rectified image plane. |
| `GenBundleAdjustedMosaic` |  | Combine multiple images into a mosaic image. |
| `GenCanonicalVariatesTrans` |  | Compute the transformation matrix of a multichannel image using the canonical variates analysis. |
| `GenCoocMatrix` |  | Calculate the co-occurrence matrix of a region in an image. |
| `GenCubeMapMosaic` |  | Create 6 cube map images of a spherical mosaic. |
| `GenDerivativeFilter` |  | Generate a derivative filter in the frequency domain. |
| `GenDiscSe` |  | Generate ellipsoidal structuring elements for gray morphology. |
| `GenFilterMask` |  | Store a filter mask in the spatial domain as a real-image. |
| `GenGabor` |  | Generate a Gabor filter. |
| `GenGaussFilter` |  | Generate a Gaussian filter in the frequency domain. |
| `GenGaussPyramid` |  | Calculating a Gauss pyramid. |
| `GenGridRectificationMap` |  | Compute the mapping between the distorted image and the rectified image based upon the points of a regular grid. |
| `GenHighpass` |  | Generate an ideal highpass filter. |
| `GenImage1` |  | Create an image from a pointer to the pixels. |
| `GenImage1Extern` |  | Create an image from a pointer on the pixels with storage management. |
| `GenImage1Rect` |  | Create an image with a rectangular domain from a pointer on the pixels (with storage management). |
| `GenImage3` |  | Create an image from three pointers to the pixels (red/green/blue). |
| `GenImage3Extern` |  | Create a three-channel image from three pointers on the pixels with storage management. |
| `GenImageConst` |  | Create an image with constant gray value. |
| `GenImageGrayRamp` |  | Create a gray value ramp. |
| `GenImageInterleaved` |  | Create a three-channel image from a pointer to the interleaved pixels. |
| `GenImageProto` |  | Create an image with a specified constant gray value. |
| `GenImageSurfaceFirstOrder` |  | Create a tilted gray surface with first order polynomial. |
| `GenImageSurfaceSecondOrder` |  | Create a curved gray surface with second order polynomial. |
| `GenImageToWorldPlaneMap` |  | Generate a projection map that describes the mapping between the image plane and the plane z=0 of a world coordinate system. |
| `GenInitialComponents` |  | Extract the initial components of a component model. |
| `GenLowpass` |  | Generate an ideal lowpass filter. |
| `GenMeanFilter` |  | Generate a mean filter in the frequency domain. |
| `GenPrincipalCompTrans` |  | Compute the transformation matrix of the principal component analysis of multichannel images. |
| `GenProjectiveMosaic` |  | Combine multiple images into a mosaic image. |
| `GenPsfDefocus` |  | Generate an impulse response of an uniform out-of-focus blurring. |
| `GenPsfMotion` |  | Generate an impulse response of a (linearly) motion blurring. |
| `GenRadialDistortionMap` |  | Generate a projection map that describes the mapping of images corresponding to a changing radial distortion. |
| `GenSavitzkyGolayFilter` |  | Compute the filter coefficients of a Savitzky-Golay filter. |
| `GenSinBandpass` |  | Generate a bandpass filter with sinusoidal shape. |
| `GenSphericalMosaic` |  | Create a spherical mosaic image. |
| `GenStdBandpass` |  | Generate a bandpass filter with Gaussian or sinusoidal shape. |
| `GetDomain` |  | Get the domain of an image. |
| `GetFeaturesOcrClassKnn` |  | Compute the features of a character. |
| `GetFeaturesOcrClassMlp` |  | Compute the features of a character. |
| `GetFeaturesOcrClassSvm` |  | Compute the features of a character. |
| `GetFoundComponentModel` |  | Return the components of a found instance of a component model. |
| `GetGrayval` |  | Access the gray values of an image object. |
| `GetGrayvalContourXld` |  | Return gray values of an image at the positions of an XLD contour. |
| `GetGrayvalInterpolated` |  | Return gray values of an image at the positions given by tuples of rows and columns. |
| `GetImagePointer1` |  | Access the pointer of a channel. |
| `GetImagePointer1Rect` |  | Access to the image data pointer and the image data inside the smallest rectangle of the domain of the input image. |
| `GetImagePointer3` |  | Access the pointers of a colored image. |
| `GetImageSize` |  | Return the size of an image. |
| `GetImageTime` |  | Request time at which the image was created. |
| `GetImageType` |  | Return the type of an image. |
| `GetMeasureParam` |  | Return the parameters and properties of a measure object. |
| `GetShapeModelClutter` |  | Get the clutter parameters of a shape model. |
| `GetSheetOfLightResult` |  | Get the iconic results of a measurement performed with the sheet-of light technique. |
| `GetTextureInspectionModelImage` |  | Get the training images contained in a texture inspection model. |
| `GiveBgEsti` |  | Return the estimated background image. |
| `GrabData` |  | Synchronous grab of images and preprocessed image data from the specified image acquisition device. |
| `GrabDataAsync` |  | Asynchronous grab of images and preprocessed image data from the specified image acquisition device. |
| `GrabImage` |  | Synchronous grab of an image from the specified image acquisition device. |
| `GrabImageAsync` |  | Asynchronous grab of an image from the specified image acquisition device. |
| `GrayBothat` |  | Perform a gray value bottom hat transformation on an image. |
| `GrayClosing` |  | Perform a gray value closing on an image. |
| `GrayClosingRect` |  | Perform a gray value closing with a rectangular mask. |
| `GrayClosingShape` |  | Perform a gray value closing with a selected mask. |
| `GrayDilation` |  | Perform a gray value dilation on an image. |
| `GrayDilationRect` |  | Determine the maximum gray value within a rectangle. |
| `GrayDilationShape` |  | Determine the maximum gray value within a selected mask. |
| `GrayErosion` |  | Perform a gray value erosion on an image. |
| `GrayErosionRect` |  | Determine the minimum gray value within a rectangle. |
| `GrayErosionShape` |  | Determine the minimum gray value within a selected mask. |
| `GrayHisto` |  | Calculate the gray value distribution. |
| `GrayHistoAbs` |  | Calculate the gray value distribution. |
| `GrayHistoRange` |  | Calculate the gray value distribution of a single channel image within a certain gray value range. |
| `GrayInside` |  | Calculate the lowest possible gray value on an arbitrary path to the image border for each point in the image. |
| `GrayOpening` |  | Perform a gray value opening on an image. |
| `GrayOpeningRect` |  | Perform a gray value opening with a rectangular mask. |
| `GrayOpeningShape` |  | Perform a gray value opening with a selected mask. |
| `GrayProjections` |  | Calculate horizontal and vertical gray-value projections. |
| `GrayRangeRect` |  | Determine the gray value range within a rectangle. |
| `GraySkeleton` |  | Thinning of gray value images. |
| `GrayTophat` |  | Perform a gray value top hat transformation on an image. |
| `GuidedFilter` |  | Guided filtering of an image. |
| `HarmonicInterpolation` |  | Perform a harmonic interpolation on an image region. |
| `HighpassImage` |  | Extract high frequency components from an image. |
| `Histo2dim` |  | Calculate the histogram of two-channel gray value images. |
| `HoughLineTransDir` |  | Compute the Hough transform for lines using local gradient direction. |
| `HoughLinesDir` |  | Detect lines in edge images with the help of the Hough transform using local gradient direction and return them in normal form. |
| `HysteresisThreshold` |  | Perform a hysteresis threshold operation on an image. |
| `Illuminate` |  | Illuminate image. |
| `ImageToChannels` |  | Convert a multi-channel image into One-channel images |
| `ImageToMemoryBlock` |  | Write an image to a memory block in various graphic formats. |
| `ImageToWorldPlane` |  | Rectify an image by transforming it into the plane z=0 of a world coordinate system. |
| `InpaintingAniso` |  | Perform an inpainting by anisotropic diffusion. |
| `InpaintingCed` |  | Perform an inpainting by coherence enhancing diffusion. |
| `InpaintingCt` |  | Perform an inpainting by coherence transport. |
| `InpaintingMcf` |  | Perform an inpainting by smoothing of level lines. |
| `InpaintingTexture` |  | Perform an inpainting by texture propagation. |
| `InsertObj` |  | Insert objects into an iconic object tuple. |
| `InspectShapeModel` |  | Create the representation of a shape model. |
| `Intensity` |  | Calculate the mean and deviation of gray values. |
| `InterleaveChannels` |  | Create an interleaved image from a multichannel image. |
| `InvertImage` |  | Invert an image. |
| `IsotropicDiffusion` |  | Perform an isotropic diffusion of an image. |
| `KirschAmp` |  | Detect edges (amplitude) using the Kirsch operator. |
| `KirschDir` |  | Detect edges (amplitude and direction) using the Kirsch operator. |
| `LabelToRegion` |  | Extract regions with equal gray values from an image. |
| `Laplace` |  | Calculate the Laplace operator by using finite differences. |
| `LaplaceOfGauss` |  | LoG-Operator (Laplace of Gaussian). |
| `LearnNdimNorm` |  | Construct classes for class_ndim_normclass_ndim_normClassNdimNormClassNdimNormclass_ndim_norm. |
| `LinearTransColor` |  | Compute an affine transformation of the color values of a multichannel image. |
| `LinesColor` |  | Detect color lines and their width. |
| `LinesFacet` |  | Detection of lines using the facet model. |
| `LinesGauss` |  | Detect lines and their width. |
| `LocalMax` |  | Detect all local maxima in an image. |
| `LocalMaxSubPix` |  | Subpixel precise detection of local maxima in an image. |
| `LocalMin` |  | Detect all local minima in an image. |
| `LocalMinSubPix` |  | Subpixel precise detection of local minima in an image. |
| `LocalThreshold` |  | Segment an image using local thresholding. |
| `LogImage` |  | Calculate the logarithm of an image. |
| `Lowlands` |  | Detect all gray value lowlands. |
| `LowlandsCenter` |  | Detect the centers of all gray value lowlands. |
| `LutTrans` |  | Transform an image with a gray-value look-up-table |
| `MapImage` |  | Apply a general transformation to an image. |
| `MatchEssentialMatrixRansac` |  | Compute the essential matrix for a pair of stereo images by automatically finding correspondences between image points. |
| `MatchFundamentalMatrixDistortionRansac` |  | Compute the fundamental matrix and the radial distortion coefficient for a pair of stereo images by automatically finding correspondences between image points. |
| `MatchFundamentalMatrixRansac` |  | Compute the fundamental matrix for a pair of stereo images by automatically finding correspondences between image points. |
| `MatchRelPoseRansac` |  | Compute the relative orientation between two cameras by automatically finding correspondences between image points. |
| `MaxImage` |  | Calculate the maximum of two images pixel by pixel. |
| `MeanCurvatureFlow` |  | Apply the mean curvature flow to an image. |
| `MeanImage` |  | Smooth by averaging. |
| `MeanImageShape` |  | Smooth image using a mean filter with arbitrary mask. |
| `MeanN` |  | Average gray values over several channels. |
| `MeanSp` |  | Suppress salt and pepper noise. |
| `MeasurePairs` |  | Extract straight edge pairs perpendicular to a rectangle or annular arc. |
| `MeasurePos` |  | Extract straight edges perpendicular to a rectangle or annular arc. |
| `MeasureProfileSheetOfLight` |  | Process the profile image provided as input and store the resulting disparity to the sheet-of-light model. |
| `MeasureProjection` |  | Extract a gray value profile perpendicular to a rectangle or annular arc. |
| `MeasureThresh` |  | Extracting points with a particular gray value along a rectangle or an annular arc. |
| `MedianImage` |  | Compute a median filter with various masks. |
| `MedianRect` |  | Compute a median filter with rectangular masks. |
| `MedianSeparate` |  | Separated median filtering with rectangle masks. |
| `MedianWeighted` |  | Weighted median filtering with different rank masks. |
| `MemoryBlockToImage` |  | Read an image from a memory block with different file formats. |
| `MidrangeImage` |  | Calculate the average of maximum and minimum inside any mask. |
| `MinImage` |  | Calculate the minimum of two images pixel by pixel. |
| `MinMaxGray` |  | Determine the minimum and maximum gray values within regions. |
| `MirrorImage` |  | Mirror an image. |
| `MomentsGrayPlane` |  | Calculate gray value moments and approximation by a plane. |
| `Monotony` |  | Calculating the monotony operation. |
| `MultImage` |  | Multiply two images. |
| `NoiseDistributionMean` |  | Determine the noise distribution of an image. |
| `NonmaxSuppressionAmp` |  | Suppress non-maximum points on an edge. |
| `NonmaxSuppressionDir` |  | Suppress non-maximum points on an edge using a direction image. |
| `ObjDiff` |  | Calculate the difference of two object tuples. |
| `OcrGetFeatures` |  | Access the features which correspond to a character. |
| `OpticalFlowMg` |  | Compute the optical flow between two images. |
| `OverpaintGray` |  | Overpaint the gray values of an image. |
| `OverpaintRegion` |  | Overpaint regions in an image. |
| `PaintGray` |  | Paint the gray values of an image into another image. |
| `PaintRegion` |  | Paint regions into an image. |
| `PaintXld` |  | Paint XLD objects into an image. |
| `PhaseCorrelationFft` |  | Compute the phase correlation of two images in the frequency domain. |
| `PhaseDeg` |  | Return the phase of a complex image in degrees. |
| `PhaseRad` |  | Return the phase of a complex image in radians. |
| `PhotometricStereo` |  | Reconstruct a surface according to the photometric stereo technique. |
| `PlaneDeviation` |  | Calculate the deviation of the gray values from the approximating image plane. |
| `Plateaus` |  | Detect all gray value plateaus. |
| `PlateausCenter` |  | Detect the centers of all gray value plateaus. |
| `PointsFoerstner` |  | Detect points of interest using the Förstner operator. |
| `PointsHarris` |  | Detect points of interest using the Harris operator. |
| `PointsHarrisBinomial` |  | Detect points of interest using the binomial approximation of the Harris operator. |
| `PointsLepetit` |  | Detect points of interest using the Lepetit operator. |
| `PointsSojka` |  | Find corners using the Sojka operator. |
| `PolarTransImage` |  | Transform an image to polar coordinates |
| `PolarTransImageExt` |  | Transform an annular arc in an image to polar coordinates. |
| `PolarTransImageInv` |  | Transform an image in polar coordinates back to Cartesian coordinates |
| `Pouring` |  | Segment an image by “pouring water” over it. |
| `PowImage` |  | Raise an image to a power. |
| `PowerByte` |  | Return the power spectrum of a complex image. |
| `PowerLn` |  | Return the power spectrum of a complex image. |
| `PowerReal` |  | Return the power spectrum of a complex image. |
| `PrewittAmp` |  | Detect edges (amplitude) using the Prewitt operator. |
| `PrewittDir` |  | Detect edges (amplitude and direction) using the Prewitt operator. |
| `PrincipalComp` |  | Compute the principal components of multichannel images. |
| `ProjHomMat2dToPose` |  | Compute a pose out of a homography describing the relation between world and image coordinates. |
| `ProjMatchPointsDistortionRansac` |  | Compute a projective transformation matrix between two images and the radial distortion coefficient by automatically finding correspondences between points. |
| `ProjMatchPointsDistortionRansacGuided` |  | Compute a projective transformation matrix and the radial distortion coefficient between two images by finding correspondences between points based on known approximations of the projective transformation matrix and the radial distortion coefficient. |
| `ProjMatchPointsRansac` |  | Compute a projective transformation matrix between two images by finding correspondences between points. |
| `ProjMatchPointsRansacGuided` |  | Compute a projective transformation matrix between two images by finding correspondences between points based on a known approximation of the projective transformation matrix. |
| `ProjectiveTransImage` |  | Apply a projective transformation to an image. |
| `ProjectiveTransImageSize` |  | Apply a projective transformation to an image and specify the output image size. |
| `RadiometricSelfCalibration` |  | Perform a radiometric self-calibration of a camera. |
| `RankImage` |  | Compute a rank filter with arbitrary masks. |
| `RankN` |  | Return gray values with given rank from multiple channels. |
| `RankRect` |  | Compute a rank filter with rectangular masks. |
| `ReadGraySe` |  | Load a structuring element for gray morphology. |
| `ReadImage` |  | Read an image with different file formats. |
| `ReadImageMetadata` |  | Read metadata from image files. |
| `ReadOcrTrainf` |  | Read training characters from files and convert to images. |
| `ReadOcrTrainfSelect` |  | Read training specific characters from files and convert to images. |
| `ReadSequence` |  | Read images. |
| `RealToComplex` |  | Convert two real images into a complex image. |
| `RealToVectorField` |  | Convert two real-valued images into a vector field image. |
| `ReceiveImage` |  | Receive an image over a socket connection. |
| `ReconstructHeightFieldFromGradient` |  | Reconstruct a surface from surface gradients. |
| `Rectangle1Domain` |  | Reduce the domain of an image to a rectangle. |
| `ReduceDomain` |  | Reduce the domain of an image. |
| `RegionToMean` |  | Paint regions with their average gray value. |
| `Regiongrowing` |  | Segment an image using region growing. |
| `RegiongrowingMean` |  | Perform a region growing using mean gray values. |
| `RegiongrowingN` |  | Segment an image using region growing for multi-channel images. |
| `RemoveObj` |  | Remove objects from an iconic object tuple. |
| `ReplaceObj` |  | Replaces one or more elements of an iconic object tuple. |
| `RftGeneric` |  | Compute the real-valued fast Fourier transform of an image. |
| `Rgb1ToGray` |  | Transform an RGB image into a gray scale image. |
| `Rgb3ToGray` |  | Transform an RGB image to a gray scale image. |
| `Roberts` |  | Detect edges using the Roberts filter. |
| `RobinsonAmp` |  | Detect edges (amplitude) using the Robinson operator. |
| `RobinsonDir` |  | Detect edges (amplitude and direction) using the Robinson operator. |
| `RotateImage` |  | Rotate an image about its center. |
| `RunBgEsti` |  | Estimate the background and return the foreground region. |
| `SaddlePointsSubPix` |  | Subpixel precise detection of saddle points in an image. |
| `ScaleImage` |  | Scale the gray values of an image. |
| `ScaleImageMax` |  | Maximum gray value spreading in the value range 0 to 255. |
| `SceneFlowUncalib` |  | Compute the uncalibrated scene flow between two stereo image pairs. |
| `SegmentImageMser` |  | Segment image using Maximally Stable Extremal Regions (MSER). |
| `SelectGrayvaluesFromChannels` |  | Selection of gray values of a multi-channel image using an index image. |
| `SelectObj` |  | Select objects from an object tuple. |
| `SendImage` |  | Send an image over a socket connection. |
| `SerializeImage` |  | Serialize an image object. |
| `SetGrayval` |  | Set single gray values in an image. |
| `SetLocalDeformableModelMetric` |  | Set the metric of a local deformable model that was created from XLD contours. |
| `SetNccModelParam` |  | Set selected parameters of the NCC model. |
| `SetPlanarCalibDeformableModelMetric` |  | Set the metric of a planar calibrated deformable model that was created from XLD contours. |
| `SetPlanarUncalibDeformableModelMetric` |  | Set the metric of a planar uncalibrated deformable model that was created from XLD contours. |
| `SetProfileSheetOfLight` |  | Set sheet of light profiles by measured disparities. |
| `SetShapeModelClutter` |  | Set the clutter parameters of a shape model. |
| `SetShapeModelMetric` |  | Set the metric of a shape model that was created from XLD contours. |
| `SetShapeModelParam` |  | Set selected parameters of the shape model. |
| `SfsModLr` |  | Reconstruct a surface from a gray value image. |
| `SfsOrigLr` |  | Reconstruct a surface from a gray value image. |
| `SfsPentland` |  | Reconstruct a surface from a gray value image. |
| `ShadeHeightField` |  | Shade a height field. |
| `ShockFilter` |  | Apply a shock filter to an image. |
| `SigmaImage` |  | Non-linear smoothing with the sigma filter. |
| `SimCaltab` |  | Simulate an image with calibration plate. |
| `SimulateDefocus` |  | Simulate an uniform out-of-focus blurring of an image. |
| `SimulateMotion` |  | Simulation of (linearly) motion blur. |
| `SinImage` |  | Calculate the sine of an image. |
| `SmoothImage` |  | Smooth an image using various filters. |
| `SobelAmp` |  | Detect edges (amplitude) using the Sobel operator. |
| `SobelDir` |  | Detect edges (amplitude and direction) using the Sobel operator. |
| `SqrtImage` |  | Calculate the square root of an image. |
| `SubImage` |  | Subtract two images. |
| `Symmetry` |  | Symmetry of gray values along a row. |
| `TanImage` |  | Calculate the tangent of an image. |
| `TestEqualObj` |  | Compare image objects regarding equality. |
| `TextureLaws` |  | Filter an image using a Laws texture filter. |
| `Threshold` |  | Segment an image using global threshold. |
| `ThresholdSubPix` |  | Extract level crossings from an image with subpixel accuracy. |
| `TileChannels` |  | Tile multiple images into a large image. |
| `TileImages` |  | Tile multiple image objects into a large image. |
| `TileImagesOffset` |  | Tile multiple image objects into a large image with explicit positioning information. |
| `TopographicSketch` |  | Compute the topographic primal sketch of an image. |
| `TrainGenericShapeModel` |  | Train a shape model for matching. |
| `TrainModelComponents` |  | Train components and relations for the component-based matching. |
| `TrainTextureInspectionModel` |  | Train a texture inspection model. |
| `TrainVariationModel` |  | Train a variation model. |
| `TraindOcvProj` |  | Training of an OCV tool. |
| `TransFromRgb` |  | Transform an image from the RGB color space to an arbitrary color space. |
| `TransToRgb` |  | Transform an image from an arbitrary color space to the RGB color space. |
| `TrimmedMean` |  | Smooth an image with an arbitrary rank mask. |
| `UncalibratedPhotometricStereo` |  | Reconstruct a surface from several, differently illuminated images. |
| `UnprojectCoordinates` |  | Calculates image coordinates for a point in a 3D plot window. |
| `UnwarpImageVectorField` |  | Unwarp an image using a vector field. |
| `UpdateBgEsti` |  | Change the estimated background image. |
| `VarThreshold` |  | Threshold an image by local mean and standard deviation analysis. |
| `VectorFieldLength` |  | Compute the length of the vectors of a vector field. |
| `VectorFieldToHomMat2d` |  | Approximate an affine map from a displacement vector field. |
| `VectorFieldToReal` |  | Convert a vector field image into two real-valued images. |
| `VectorToPose` |  | Compute an absolute pose out of point correspondences between world and image coordinates. |
| `Watersheds` |  | Extract watersheds and basins from an image. |
| `WatershedsMarker` |  | Extract watersheds and combine basins based on markers. |
| `WatershedsThreshold` |  | Extract watershed basins from an image using a threshold. |
| `WienerFilter` |  | Image restoration by Wiener filtering. |
| `WienerFilterNi` |  | Image restoration by Wiener filtering. |
| `WriteImage` |  | Write images in graphic formats. |
| `WriteImageMetadata` |  | Write metadata of image files. |
| `WriteOcrTrainfImage` |  | Write characters into a training file. |
| `ZeroCrossing` |  | Extract zero crossings from an image. |
| `ZeroCrossingSubPix` |  | Extract zero crossings from an image with subpixel accuracy. |
| `ZoomImageFactor` |  | Zoom an image by a given factor. |
| `ZoomImageSize` |  | Zoom an image to a given size. |
