MF3D Release 1
===============

The `MF3D stimulus set (Release 1) <https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544>`_ consist of 14,000 high resolution images and animated video sequences. The images and animations are hosted on `Figshare <https://figshare.com>`_ and can be downloaded separately (:opticon:`file-zip`):



.. panels::
  :column: col-lg-12 p-2

  .. image:: _images/Logos/Figshare.svg
    :width: 150
    :align: right
    :class: align-right
    :alt: Figshare
  .. image:: _images/Logos/cc-by-nc.svg
    :width: 100
    :align: right
    :class: align-right
    :alt: CC-BY-NC

  .. link-button:: https://doi.org/10.6084/m9.figshare.8226029
    :type: url
    :text: MF3D Expression set (10.97 GB)
    :tooltip: Figshare
    :classes: btn-primary btn-sm

  .. link-button:: https://doi.org/10.6084/m9.figshare.8226311
    :type: url
    :text: MF3D Identities set (26.75 GB)
    :tooltip: Figshare
    :classes: btn-primary btn-sm

  .. link-button:: https://doi.org/10.6084/m9.figshare.8226317
    :type: url
    :text: MF3D Animations set (614 MB)
    :tooltip: Figshare
    :classes: btn-primary btn-sm


What's in MF3D R1?
------------------

MF3D R1 is a publicly released stimulus set for the macaque research community that consists of 14,000 static renders of the macaque avatar, saved as high resolution (3840 x 2160 pixels, 32-bit) RGBA images in .png format (:ref:`Figure 1A, i <mf3d-r1-figA>`) and a smaller sample of animated video clips. The inclusion of the alpha transparency channel allows for compositing of multiple images into a frame, including backgrounds, as well as making it easy to generate control stimuli with identical silhouettes. The high resolution permits down-sampling or cropping as appropriate for the display size being used.

The virtual scene was configured such that the avatar will appear at real-world retinal size when images are presented at full-screen on a 27” monitor with 16:9 aspect ratio, at 57cm viewing distance from the subject. For each 2D colour image, we additionally provide a label map image, which is an indexed image that assigns each pixel an integer value depending on the anatomical region of the avatar it belongs to (:ref:`Figure 1A, ii <mf3d-r1-figA>`). Label maps can be used to analyse subjects’ gaze in free-viewing paradigms (:ref:`Figure 1A, iii-iv <mf3d-r1-figA>`), for gaze-contingent reward schedules, or for generating novel stimuli by masking specific structures in the corresponding colour image.

.. _mf3d-r1-figA:

.. figure:: _images/ML_Figs/MurphyLeopold_Fig1A.png
  :alt: Figure 1A - Stimulus set format

  **Figure 1A.** Stimulus set format and applications. **i.** Each colour image in the set is rendered as a 3840 x 2160 pixel RGBA image in .png format with 32-bits per pixel. The avatar is positioned such that the center of the screen coincides with the cyclopean eye when the avatar is directly facing the camera. **ii.** For each colour image, we provide a corresponding label map image (.hdr format) of the same dimensions, where integer pixel values indicate which anatomical structure of the avatar they belong to. **iii.** An example of a simulated gaze distribution map for the stimulus shown in i. **iv.** Proportion of fixations on each labelled structure can be easily computed. **v.** Novel stimuli can be created by using the label map to mask specific parts of the original image. 

The static stimuli of MF3D release 1 are divided into two collections:

  1) variable expressions with fixed identity (corresponding to real individual M02); and 
  2) variable identities with fixed expression (neutral). 

.. _mf3d-r1-expression:

MF3D R1 Subsets
-----------------

.. tabbed:: Expression subset

  For the expression set, we varied head orientation (±90° azimuth x ±30° elevation in 10° increments = 133 orientations; :ref:`Figure 1B, i <mf3d-r1-figB>`), facial expression type (neutral plus bared-teeth ‘fear grimace’, open-mouthed threat, coo, yawn, and tongue-protrusion = 5) and the intensity of the expression (25, 50, 75 and 100% = 4; :ref:`Figure 1B, ii <mf3d-r1-figB>`). We additionally include the neutral expression with open and closed eyes, as well as azimuth rotations beyond 90° (100 to 260° in 10° increments) for a total of 2,926 colour images. In order to maintain naturalistic poses, head orientation was varied through a combination of neck (±30° azimuth and elevation) and body (±60° azimuth) orientations.

  .. _mf3d-r1-figB:

  .. figure:: _images/ML_Figs/MurphyLeopold_Fig1B.png
    :alt: Figure 1B - Expression stimuli

    **Figure 1B, Expression stimuli. i.** All head orientations rendered for each expression condition (neutral expression shown for illustration): 19 azimuth angles (-90 to +90° in 10° increments) x 7 elevation angles (-30 to +30° in 10° increments) for 133 unique head orientations. **ii.** Five facial expressions (rows) rendered at four levels of intensity (columns), at each of the head orientations illustrated in **i**, for a total of 2,793 unique colour images. 

.. tabbed:: Identity subset

  .. _mf3d-r1-identity:

  For the identity set, we selected a subset of head orientations (±90° azimuth x ±30° elevation in 30° increments = 21 orientations; :ref:`Figure 1C, i <mf3d-r1-figC>`), and co-varied facial morphology based on distinct trajectories within PCA-space (n = 65; :ref:`Figure 1C, ii <mf3d-r1-figC>`), including each of the first five PCs (which together account for 75% of the sample variance in facial morphology), with distinctiveness (Euclidean distance from the average face, ±4σ in 1σ increments = 8 levels, excluding the mean; :ref:`Figure 1C, iii <mf3d-r1-figC>`) for a total of 10,941 identity images.

  .. _mf3d-r1-figc:

  .. figure:: _images/ML_Figs/MurphyLeopold_Fig1C.png
    :alt: Figure 1C - Identity stimuli

    **Figure 1C. Identity stimuli. i.** All head orientations rendered for each identity condition (average identity shown for illustration): 7 azimuth angles x 3 elevation angles for 21 head orientations. **ii.** Identity trajectories through face space were selected through all pairwise combinations of the first 5 principal components from the PCA (which cumulatively account for 75% of the sample variance in facial morphology), at 3 polar angles for a total of 65 unique trajectories. **iii.** Identities were rendered at eight levels of distinctiveness (±4σ from the sample mean in 1σ increments) along each identity trajectory (shown here for the first 5 PCs), plus the sample mean for a total of 10,941 unique colour images.



.. tabbed:: Animation subset

  .. _mf3d-r1-animation:

  .. _mf3d-r1-figD:

  .. figure:: _images/ML_Figs/MurphyLeopold_Fig1D.png
    :align: left
    :width: 100%
    :figwidth: 40%
    :alt: Figure 1C - Identity stimuli

    **Figure 1D.** Animated stimuli. A subset of frames from an example animation sequence included in the MF3D R1 stimulus set is rendered at 5 different head azimuth orientations (rows). Bottom panel: Accompanying audio waveform and spectrogram for this particular animation, which depicts a ‘scream’ vocalization.


  For studies requiring more naturalistic stimuli, we also have the ability to generate a virtually limitless number of animations that promise great flexibility for studying dynamic facial behaviour. Here we have included a small selection of short animations (2 seconds or less per clip) as a proof of concept, which are rendered at 3840 x 2160 pixels and 60 frames per second, encoded with H.264 perceptually-lossless compression and saved in .mp4 format with a black background. For each action sequence, animations are rendered at 5 different head azimuth angles (-60, to 60° in 30° increments). All animations feature identical start and end frames, which allows the possibility of stitching multiple clips together using video editing software (such as the video editor included in Blender), to produce longer, seamless movies containing various permutations of action sequences. We provide a :link-badge:`https://github.com/Phenomenal-Cat/MF3D-Tools/blob/master/MF3D_ConcatClips_Demo.py,Python script,cls=badge-primary text-white` to demonstrate automated compilation of animation clips using Blender's video sequence editor. The animations were produced by manually coding video footage of real Rhesus macaques performing facial expressions and vocalizations.


  .. raw:: html

	<iframe src="https://player.vimeo.com/video/394782616?color=ff9933&byline=0&portrait=0" style="display:block; padding:10px; border:5px" width="400" height="225" frameborder="0" align="right" allow="autoplay; fullscreen" allowfullscreen></iframe>

  .. container:: clearer

    .. image :: _images/spacer.png
       :width: 1