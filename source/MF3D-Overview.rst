*************
MF3D Overview
*************

About MF3D
===============================

The Macaque Face 3D (MF3D) project is an effort to develop a parametrically controlled,
anatomically accurate, three-dimensional, virtual avatar of the Rhesus macaque face and head, for
visual stimulation in behavioral neuroscience experiments involving this important model species.
The avatar has been used to produced the first ever publicly available database of computer generated 
images of macaque facial expression and identity, which you can learn more about below.
Full details of how the model and rendered images were generated have been published here:


.. _murphy-leopold:

.. note::  

    **Murphy AP & Leopold DA (2019)**. A parameterized digital 3D model
    of the Rhesus macaque face for investigating the visual processing
    of social cues. *J.Neurosci.Methods*, 324: 108309. `DOI:
    10.1016/j.jneumeth.2019.06.001 <https://doi.org/10.1016/j.jneumeth.2019.06.001>`_

.. image:: https://user-images.githubusercontent.com/7523776/58911022-ef7b2000-86e4-11e9-8a6a-ef9a44206a4e.png
  :width: 800
  :alt: MF3D construction summary


--------------

MF3D R1 Stimulus Set
===============================

The `MF3D stimulus
set (Release 1) <https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544>`_ consist of 14,000 high resolution images and animated video sequences. The images and animations are hosted on `Figshare <https://figshare.com>`_ and can be downloaded separately:

-  `MF3D Expression set <https://doi.org/10.6084/m9.figshare.8226029>`_

-  `MF3D Identities set <https://doi.org/10.6084/m9.figshare.8226311>`_

-  `MF3D Animations set <https://doi.org/10.6084/m9.figshare.8226317>`_

An overview of the contents of this stimulus set can be found
:doc:`here <MF3D-Release-1>`.
The `MF3D Tools <https://github.com/MonkeyGone2Heaven/MF3D-Tools>`_ GitHub repository contains code (Matlab and Python) to facilitate
the selection, loading, editing, analysis and saving of images and animations from the stimulus set.

The code in this repository is licensed under GNU General Public License `GNU GPLv3 <https://choosealicense.com/licenses/gpl-3.0/#>`_,
while the media provided in the MF3D R1 stimulus set is licensed under Creative Commons `CC BY-NC
4.0 <http://creativecommons.org/licenses/by-nc/4.0/>`_. If you use any content from the stimulus set in your research, we ask
that you cite the :ref:`publication <murphy-leopold>` listed above.


.. image:: _images/Logos/Figshare.svg
  :width: 125
  :alt: Figshare
  :target: https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544
.. image:: _images/spacer.png
  :width: 15
.. image:: _images/Logos/GitHub.svg
  :width: 40
  :alt: GitHub
  :target: https://github.com/MonkeyGone2Heaven/MF3D-Tools
.. image:: _images/spacer.png
  :width: 15
.. image:: _images/Logos/Copyleft.png
  :width: 40
  :alt: Copyleft
  :target: https://en.wikipedia.org/wiki/Copyleft
.. image:: _images/spacer.png
  :width: 20
.. image:: _images/Logos/cc-by-nc.svg
  :width: 110
  :alt: CC-BY-NC
  :target: http://creativecommons.org/licenses/by-nc/4.0/
.. image:: _images/spacer.png
  :width: 20
.. image:: _images/Logos/gplv3.png
  :width: 100
  :alt: GPL v3
  :target: https://choosealicense.com/licenses/gpl-3.0/#


Feature Overview
===============================

The following video animations demonstrate some of the parameters of the
MF3D avatar that can be controlled and how these variations are encoded.

Facial expression, gaze and lighting
----------------------------------------------


.. raw:: html

	<iframe src="https://player.vimeo.com/video/326460055?color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>


This video demonstrates how our macaque model of emotional facial
expressions (for a single identity) can be continuously and
parametrically varied to adjust appearance. The model was constructed
using computed tomography (CT) data from a real Rhesus macaque, acquired
under anesthesia, and edited and rigged by a professional digital
artist. In addition to control of various facial expressions, the
model's head and eye gaze direction can be programmatically controlled,
as well as other variables such as environmental lighting and surface
coloration, amongst others.


Facial dynamics estimation
------------------------------------

.. raw:: html

	<iframe src="https://player.vimeo.com/video/329805226?color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>

In order to simulate naturalistic facial dynamics in the macaque avatar,
we estimate the time courses of facial motion from video footage of real
animals. Applying these time courses to the animation of bones and shape
keys of the model, we can mimic the facial motion of the original clip,
while retaining independent control over a wide range of other
variables. The output animation can be rendered at a higher resolution
and frame rate (using interpolation) than the input video. (Original
video footage in the left panel is used with permission of Off The
Fence™).


Identity morphing
---------------------------

.. raw:: html

	<iframe src="https://player.vimeo.com/video/323447440?loop=1&color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>


Individual variations in
cranio-facial morphology (3D face shape) can be continuously and
parametrically varied to adjust appearance, as in the `MF3D R1
Identity <https://doi.org/10.6084/m9.figshare.8226311>`_ stimulus set.
The statistical model was constructed through principal component
analysis (PCA) of the 3D surface reconstructions of 23 real Rhesus
monkeys from computed tomography (CT) data acquired under anesthesia.
The 3D plot in the top right corner illustrates the first three
principal components of this 'face-space', where the origin of the plot
represents the sample average face.



Animated sequences
----------------------------

.. raw:: html

	<iframe src="https://player.vimeo.com/video/394782616?color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>


Animated facial expression clips from the `MF3D R1
Animation <https://figshare.com/articles/MF3D_R1_Animations/8226317>`_
stimulus set can be combined to form a longer continuous animation
sequence for use in experiments that require more naturalistic dynamics.
This example was generated using the Python script
`MF3D_ConcatClips_Demo.py <https://github.com/MonkeyGone2Heaven/MF3D-Tools/blob/master/MF3D_Blender/MF3D_ConcatClips_Demo.py>`_
to interleave the appropriate head rotation sequences between consecutive expression clips, controlled via the open-source `Blender <www.blender.org>`_ video sequence editor.
