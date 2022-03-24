.. _Stim_MF3DRT:

======================================
:fa:`gamepad` MF3D Real-time
======================================

MF3D RT is not a rendered stimulus set, but a code base for (near) real-time rendering of the macaque avatar using a game rendering engine. Since each frame must be rendered within a single display refresh (e.g. 16.6ms for a 60Hz display), there is a trade off in level of detail and realism that can be achieved compared to offline rendering. It is intended for brief visual presentations of static images employed in traditional neuroscience studies, although it can be used to generate slowly evolving scene dynamics. For real-time generation of animated sequences of the avatar embedded in virtual environments, see the :ref:`MF3D Unity <Stim_Unity>`_ below.

.. image:: _images/Logos/Blender.svg
  :width: 150
  :alt: Blender
.. image:: _images/Logos/cc-by-nc.svg
  :width: 100
  :alt: CC-BY-NC

.. Note:: 
	MF3D RT requires access to the 3D model Blender file, which is not currently publicly released. If you are interested in using this resource in your research then please contact us to discuss possible collaboration.

Adaptive stimulus optimization
------------------------------

The motivation for MF3D RT is to provide rapid access to the infinite stimulus space that is possible via combinations of the many continuous parameters of the MF3D avatar. Online updating of stimulus parameters is a common approach in psychophysics, where `adaptive staircase <https://en.wikipedia.org/wiki/Psychophysics#Adaptive_psychophysical_methods>`_ procedures are used to select appropriate parameters for subsequent stimuli based on an observer's previous responses. 

In the neural domain, similar adaptive approaches utilizing online analysis of neural recordings have shown promise (`DiMattina & Zhang, 2013 <https://doi.org/10.3389/fncir.2013.00101>`__), including `genetic algorithms <https://en.wikipedia.org/wiki/Genetic_algorithm>`_ (`Forrest, 1993 <DOI: 10.1126/science.8346439>`__). Application of this approach to studying single unit responses in the
macaque brain was pioneered by
`Connor <https://krieger.jhu.edu/mbi/directory/ed-connor/>`__ and
colleagues, who used a genetic algorithm to iteratively adapt 3D visual
stimuli in order to maximize firing rates of neurons in macaque
inferotemporal (IT) cortex (`Yamane et al.,
2008 <https://doi.org/10.1038/nn.2202>`__; `Hung et al.,
2012 <https://doi.org/10.1016/j.neuron.2012.04.029>`__; `Vaziri et al.,
2014 <https://doi.org/10.1016/j.neuron.2014.08.043>`__). Variations of
this approach have since been used to study the visual preferences of
neurons in the macaque 'face patch' regions of IT cortex (`Chang & Tsao,
2017 <https://doi.org/10.1016/j.cell.2017.05.011>`__; `Ponce et al.,
2019 <https://doi.org/10.1016/j.cell.2019.04.005>`__).

The MF3D RT implementation is agnostic of what data is being used to drive convergence towards 'optimal' stimuli, thus maintaining flexibility. 


UPBGE
-----

We utilize the `UPBGE <https://upbge.org/>`__ Blender game engine of the
open-source 3D graphics software `Blender <www.blender.org>`__ to
parametrically vary multiple aspects of facial appearance in real-time,
based on online analysis of neural spiking responses. On each screen
refresh interval, UPBGE updates the parameters of the virtual scene
based on an incoming vector of floating point values received from the
experimental control computer via `UDP <https://en.wikipedia.org/wiki/User_Datagram_Protocol>`__ connection.

A stimulus subspace is defined by the selection of N dimensions that
affect facial appearance in the pixel-domain (see **Table 1**).


MF3D RT Add-on
--------------

In the Blender or UPBGE graphical user interface, go to the `add-on menu <https://docs.blender.org/manual/en/latest/editors/preferences/addons.html>`_ and select the location of MF3D-RT.py. 



+--------+-------------------------+---------------------------------------+-----------+-----------+
| Dim.   | Category                | Description                           | Unit      | Range     |
+========+=========================+=======================================+===========+===========+
| 1      | Spatial - Allocentric   | Body azimuth angle                    | Degrees   |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 2      | Spatial - Allocentric   | Body elevation angle                  | Degrees   |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 3      | Spatial - Allocentric   | Head azimuth angle                    | Degrees   |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 4      | Spatial - Allocentric   | Head elevation angle                  | Degrees   |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 5      | Spatial - Allocentric   | Eye gaze azimuth angle                | Degrees   |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 6      | Spatial - Allocentric   | Eye gaze elevation angle              | Degrees   |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 7      | Social                  | Eye lid closure                       | Percent   | 0 - 100   |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 8      | Social                  | Pupil dilation                        | Percent   | 0 - 100   |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 9      | Social                  | Brow raise                            | Percent   | 0 - 100   |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 10     | Social                  | Mouth open                            | Percent   | 0 - 100   |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 11     | Social                  | Lip retraction - pout                 | Percent   | 0 - 100   |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 12     | Social                  | Ear flap                              | Percent   | 0 - 100   |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 13     | Face shape              | Principal component 1                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 14     | Face shape              | Principal component 2                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 15     | Face shape              | Principal component 3                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 16     | Face shape              | Principal component 4                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 17     | Face shape              | Principal component 5                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 18     | Face shape              | Principal component 6                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 19     | Face shape              | Principal component 7                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 20     | Face shape              | Principal component 8                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 21     | Face shape              | Principal component 9                 | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 22     | Face shape              | Principal component 10                | S.D.      | +/- 3     |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 23     | Texture                 | Lighting direction                    |           |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+
| 24     | Texture                 |                                       |           |           |
+--------+-------------------------+---------------------------------------+-----------+-----------+


MF3D RT Matlab Demo
--------------------

We provide Matlab scripts for use with `NIMH MonkeyLogic <https://monkeylogic.nimh.nih.gov/>`_ (`Hwang et al., 2019 <https://doi.org/10.1016/j.jneumeth.2019.05.002>`_) and `PsychToolbox <http://psychtoolbox.org/>`_ () / `PLDAPS <https://github.com/HukLab/PLDAPS>`_ (`Eastman & Huk, 2012 <https://www.doi.org/10.3389/fninf.2012.00001>`_) experiments that demonstrate online iterative control of the MF3D stimulus rendering in UPBGE. In all cases, Matlab communicates with UPBGE via TCP connection between each stimulus presentation in order to 



.. _Stim_Unity:

MF3D Unity
==============
