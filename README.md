MVHristov 6D Unified Field Theory – Computational Package
=========================================================

Author: Martin V. Hristov  
Version: December 2025  
License: Apache 2.0  

This folder contains the complete theoretical and computational companion
materials for the 6D Unified Field Theory (6D-UFT), including the full paper,
LaTeX source, and executable Python demonstrations used to generate all
validation plots.

Folder Contents
---------------

MVHristov_6D_UFT_Complete.pdf  
    The full scientific paper describing the complete 6D Unified Field Theory.
    Topics include:
        - Geometric foundations of the (1+3+2) temporal–spatial structure  
        - Field equations from the 6D Ricci scalar  
        - Internal temporal geometry (t₂, t₃)  
        - Emergent quantum mechanics and collapse mechanism  
        - Decoherence, uncertainty, internal curvature  
        - Galaxy rotation curve derivation (no dark matter)  
        - Short-range gravity predictions  
        - Atomic clock fluctuation predictions  
        - Stability, anomalies, unitarity, renormalization  
        - Research roadmap and falsifiability criteria  

MVHristov_6D_UFT_Source.tex  
    The LaTeX source file used to produce the PDF.

MVHristov_6D_UFT_Computations.py  
    A Python script implementing the key computational predictions of the
    theory and generating all four validation figures.

    The script includes:

      1. Galaxy Rotation Curves  
         Computes circular velocity using the 6D corrected potential  
             V(r) = -GM/r [1 + α e^{-r/λΦ} + β e^{-r/λθ}]  
         and compares it to Newtonian predictions.  
         Output:  
             MVHristov_6D_UFT_outputs/rotation_curves.png  

      2. Decoherence Rates  
         Implements the 6D-UFT macroscopic decoherence scaling:  
             Γ_decoh ~ (M / m_p)^(2/3) × 10⁻⁵ s⁻¹  
         Output:  
             MVHristov_6D_UFT_outputs/decoherence_scaling.png  

      3. Short-Range Gravity Modifications  
         Computes deviations from Newtonian gravity at sub-mm distances using  
         Yukawa corrections arising from internal temporal curvature.  
         Output:  
             MVHristov_6D_UFT_outputs/short_range_gravity.png  

      4. Atomic Clock Fluctuations  
         Simulates predicted fluctuations in δν/ν from internal temporal noise.  
         Output:  
             MVHristov_6D_UFT_outputs/clock_fluctuations.png  

      5. Internal Temporal Metric Tools  
         Functions to compute φ_ab and approximate internal curvature indicators.

      6. Mathematical Consistency Tests  
         Verifies:
            - α and β are dimensionless  
            - Newtonian limit recovered when α, β → 0  
            - Decoherence scaling behaves as predicted  

Running the Code
----------------

Requirements:
    Python 3.10+  
    numpy  
    scipy  
    matplotlib  

Install dependencies:
    pip install numpy scipy matplotlib

(Recommended) Create an isolated environment:
    python -m venv venv
    venv\Scripts\activate
    pip install numpy scipy matplotlib

Run the script:

    1. Open Command Prompt (CMD)
    2. Navigate to the folder:
           D:
           cd D:\MVHristov_6D_UFT_Complete
    3. Execute:
           python MVHristov_6D_UFT_Computations.py

All generated figures will appear in:

    MVHristov_6D_UFT_outputs/

Notes on Parameters
-------------------

All parameters in the Python script correspond to order-of-magnitude ranges
derived in the paper. They are not precision fits; their purpose is to:

    - Demonstrate functional behaviour of the 6D formulas  
    - Visualize how internal temporal geometry affects observables  
    - Enable researchers to explore parameter dependence  
    - Provide a transparent, modifiable baseline implementation  

Users may freely tune correlation lengths, couplings, and internal geometry
fields to compare predictions with specific datasets.

Scientific Purpose of This Package
----------------------------------

This directory serves as the complete companion to the 6D Unified Field Theory
and provides:

    • A reproducible numerical demonstration of the theory’s predictions  
    • Clear computational tools for further research  
    • A baseline implementation for comparison and falsification  
    • A bridge between theoretical derivations and empirical tests  

The Python code directly reflects equations from the 6D action and is not a
toy model—its outputs correspond to the analytic structure of the theory.

License
-------

This work is released under the Apache License 2.0.  
It may be used, redistributed, and built upon, provided proper attribution is
given to **Martin V. Hristov (2025)**. No warranty is provided.

------------------------------------------------------------
End of README
------------------------------------------------------------
