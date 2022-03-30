.. _Methods_ExpressionTransfer:

==========================================
:fa:`flask` Methods - Expression Transfer
==========================================

.. contents:: :local:

Background
-------------------------------------


.. figure:: _images/DocFigs/ExpressionCloning_Error.png
  :align: right
  :figwidth: 50%
  :width: 100%
  :alt: Expression cloning

  **A.** 

One limitation of the MF3D model construction approach was that variations in craniofacial morphologies were characterized by collecting CT data from different individuals while anesthetized. Consequently, adding multiple facial expressions to a given identity involved the labor-intensive process of digital sculpting by a professional CG artist. As a result, identity was parameterized separately from expression, and it was therefore not possible to generate faces of different individuals with the various modeled expressions. 


To resolve this issue we performed a digital technique known as 'expression cloning', to transfer the expression components of the original model (identity M02) into the face-space framework. This was achieved using `Wrap3 (RS3D) <https://www.russian3dscanner.com/>`_ software.


Process
-------------------------------------

