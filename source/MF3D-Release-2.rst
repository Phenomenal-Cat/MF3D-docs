.. _Stim_MF3DR2:

============================
:fa:`image` MF3D Release 2
============================

.. card::
  :margin: 0
  :class-header: sd-bg-warning
  :class-body: sd-bg-warning 

  :fa:`triangle-exclamation` Coming soon!
  ^^^^^^
  We have solved the expression transfer problem, and are in the prcess of rendering a set of static stimuli as a demonstration of what is possible ()



What's in MF3D R2?
------------------

A major limitation of the method used to produce the first stimulus set :link-badge:`MF3D-Release-1, MF3D R1, ref,badge-primary text-white` was that facial expression and facial identity could not be co-varied simultaneously. Consequently, MF3D R1 contained an :ref:`expression subset <mf3d-r1-expression>` in which facial identity was held constant (identity M02) and a separate :ref:`identity subset <mf3d-r1-identity>` in which expression was held constant (neutral expression). Using a computational operation known as 'expression cloning' (or more generally 'shape deformation transfer'), we are now able to transfer facial expressions across identities to generate a novel stimulus set of CGI
macaque faces with unparalleled parametric control.


The MF3D Release 1 'expression' stimulus set contained 133 head/body orientations x 5 expressions x 4 intensities for a total of 2661 images of a single identity (M02). Restricting the sampling to just 49 head angles (981 images), we now replicate this for the average identity and the first 5 principal components of MF3D face-space (5,880).


MF3D R2 Subsets
----------------------------

.. tab-set::
  :class: sd-bg-light sd-rounded-2 p-2

  .. tab-item:: Expression x Identity

    The static stimuli of MF3D R2 extends those of R1 by covarying facial identity along with head angle and facial expression.


  .. tab-item:: Animation subset

    The animated component of the MF3D R2 stimulus set will replicate the :link-badge:`mf3d-r1-animation, animation subset, ref, badge-success text-white` of MF3D R1, but includes a variety of facial identities of the avatar.
