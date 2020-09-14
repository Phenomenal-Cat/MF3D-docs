===============================
Compiling Animation Sequences
===============================

For addressing certain scientific questions, it may be beneficial to
be able to present dynamic video stimuli continuously over a longer
duration, with many variations of facial movement interleaved. The short
animated videos provided in the :ref:`MF3D Animations R1 <mf3d-r1-animation>` stimulus set have been rendered in manner that allows users to concatenate multiple clips
together to achieve this goal. Specifically, the first and last frames
of each movie clip for a given head azimuth orientation are identical.
Therefore, all that is needed to create longer movie clips containing
many permutations of facial actions is to edit the original clips
together in video editing software.

.. sidebar:: Video Editing in Blender

  .. image:: _images/Logos/Blender.svg
    :height: 30
    :align: left
    :alt: Blender
    :target: https://www.blender.org

  While there are many programs available for video editing, we recommend the video sequence editor (VSE) provided in `Blender <https://www.blender.org/>`__, for several reasons:

  1. Blender is `free and
     open-source <https://www.blender.org/about/license/>`__ under the GNU
     General Public License
  2. Blender has an embedded `Python
     interpreter <https://docs.blender.org/api/current/>`__, allowing
     Python scripting of various actions.
  3. Blender is the software that we also used to render the images and
     movies of 3D macaque avatar, and hope to make publicly available in future.


Using MF3D_ConcatClips.py
-----------------------------

MF3D R1 provides a limited set of movie clips, which are summarized in
the accompanying spreadsheet (.csv file). `MF3D_ConcatClips_Demo.py <https://github.com/Phenomenal-Cat/MF3D-Tools/blob/master/MF3D_Blender/MF3D_ConcatClips_Demo.py>`__
reads the data from this spreadsheet to find the appropriate order to
position various movie clips in order to generate a new longer movie
containing smooth continuous motion.

.. figure:: _images/GUIs/Blender_VSE_Script.png
  :align: left
  :figwidth: 50%
  :width: 100%
  :alt: Blender VSE window

  A screenshot of the Blender VSE window. Animated clips can be arranged manually or programmatically via Python scripting.

.. container:: clearer

    .. image :: _images/spacer.png
       :width: 1

Example
--------

For example, if a user were to specify the following variables in
`MF3D_ConcatClips.py <https://github.com/Phenomenal-Cat/MF3D-Tools/blob/master/MF3D_Blender/MF3D_ConcatClips_Demo.py>`_:

.. code:: python

    ClipSequence    = ['Yawn','Rotate','Coo','Rotate','Scream']     
    HeadAzimuths    = [0, -60, -60, 30, 30]      
    PlaybackSpeed   = [1, 2, 1, 3, 1]

This tells the script to load the following sequence of five movie
clips:

.. raw:: html

	<iframe src="https://player.vimeo.com/video/394782616?color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="right" allow="autoplay; fullscreen" allowfullscreen></iframe>

1. Load the movie clip in which the avatar performs a yawn action with
   the head azimuth angle at 0° (i.e. facing the virtual camera).

2. Once the yawn clip is completed, a subset of frames will be loaded
   from the head rotation clip, and appended in reverse order so as to
   produce a head rotation from 0 to -60° at a speed of 60°/second.

3. Load the movie clip containing a 'coo' vocalization with the head
   azimuth angle at -60°,

4. Load the frames from the head rotation clip to show the head rotating
   from -60° to +30°, at 105°/second

5. Load the movie clip containing a 'scream' vocalization with the head
   azimuth angle at +30°



