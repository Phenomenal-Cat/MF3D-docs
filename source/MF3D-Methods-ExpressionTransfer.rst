.. _Methods_ExpressionTransfer:

==========================================
:fa:`flask` Methods - Expression Transfer
==========================================

.. contents:: :local:

Background
-------------------------------------


.. figure:: _images/DocFigs/ExpressionCloning_Error.png
  :align: right
  :figwidth: 40%
  :width: 100%
  :alt: Expression cloning


One limitation of the MF3D model construction approach was that variations in craniofacial morphologies were characterized by collecting CT data from different individuals while anesthetized. Consequently, adding multiple facial expressions to a given identity involved the labor-intensive process of digital sculpting by a professional CG artist. As a result, identity was parameterized separately from expression, and it was therefore not possible to generate faces of different individuals with the various modeled expressions. 


Deformation Transfer Process
-------------------------------------

To resolve this issue we perform 'expression cloning' using the deformation transfer method (`Sumner & Popovic, 2004 <https://doi.org/10.1145/1015706.101573>`_), This process was used to transfer each canonical expression component that was sculpted for the original model (identity M02) into the face-space framework. 