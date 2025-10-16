Thought for 18s
Prime Wave Theory (PWT) Repository

Welcome to the Prime Wave Theory (PWT) GitHub repository! PWT is a protoscientific framework exploring the universe through the lens of prime numbers, harmonic cascades, and reciprocal duality. Inspired by the PWT Thesis V6, this repo hosts code tools to model PWT concepts, from variable gravity predictors to DNA prime signature analyzers and interactive periodic tables highlighting harmonic signatures. Our goal is to foster community collaboration, turning PWT's insights into interactive, testable explorations of quantum harmonics, cosmic scaling, negentropy in biology, and beyond.

For more context, check out the PWT.life blog, including posts like Variable Gravity Through the PWT Lens, PWT Prime-Driven Order in Biology and Consciousness, and the series on chemical elements: Unveiling Chemical Insights: Harmonic Prime Signatures, Harmonic Resonances: Grouping Elements, and Elemental Stability Through Harmonic Lenses, which reference tools here.
Table of Contents

    Installation
    Usage
    Examples
    Contributing
    License
    Contact

Installation

To run the tools locally:

    Clone the repo:
    Install dependencies (Python 3.12+ recommended):
    For Jupyter notebooks: pip install notebook (or jupyterlab for advanced use).
    For interactive runs: Open Jupyter with jupyter notebook and load .ipynb files.

Note: Some tools (e.g., DNA analyzers) fetch data from NCBI—replace Entrez.email in the code with your real email to avoid rate limits.
Usage

This repo includes Python scripts and notebooks for PWT simulations. Key files:

A line plot showing n vs ΔE, with actual (blue) and rounded (red dashed) values, annotated with prime signatures. PWT includes the use of integer rounding; however, this rounding methodology is justified by the principle that quantum energy states possess a natural resonance width, not infinite precision, and our approach seeks the core integer signal within this resonance. Future work will focus on material-dependent tests of the gravitational constant, G, to further validate PWT's predictions.

    dna_prime_analyzer.py: Analyzes DNA sequences for prime signatures in codon counts, simulates evolutionary drifts to model negentropy. For details, see the blog post PWT Prime-Driven Order in Biology and Consciousness.
    Run: python dna_prime_analyzer.py
    Customize: Edit accession/start/end for different genes.
    PWT_DNA_Prime_Analyzer.ipynb: Interactive Jupyter version for browser-based experimentation—run it online via Binder!
    Generated Image

    Open in Jupyter to explore prime drifts in real-time, tying to PWT's negentropy concepts.
    g_variation_predictor.py (from variable gravity post): Predicts G variations based on atomic primes.
    Run: python g_variation_predictor.py
    PWT_Harmonics_Periodic_Table.ipynb: Interactive Jupyter notebook generating an HTML periodic table colored by harmonic prime signatures (low, medium, high). Ties to PWT's reciprocal lens for microcosmic patterns in chemistry and quantum mechanics. For details, see the blog series on harmonic signatures.
    Run: Open in Jupyter, execute cells to generate pwt_periodic_table.html—open the HTML in a browser for interactivity (hover tooltips, click modals).

For full usage details, see comments in each file.
Examples
DNA Prime Analysis

Fetch and analyze the HBB gene:

Output might show prime counts (e.g., 3 for certain codons, tying to Matter stability in PWT).
Evolutionary Simulation

Simulate drifts:

Observe how prime signatures persist, illustrating negentropy.
Jupyter Interactive (DNA)

Open PWT_DNA_Prime_Analyzer.ipynb in Jupyter, run cells, and tweak parameters (e.g., mutation_rate=0.05 for more chaos) to see prime rebounds.
Periodic Table Harmonics

Run PWT_Harmonics_Periodic_Table.ipynb:

Generates an interactive HTML table where elements are colored by harmonic ranges (e.g., low: #a7c9e7, medium: #bce6b2, high: #e6b2b6). Hover for signatures, click for details. Explore patterns like high harmonics in stable elements (e.g., Oxygen at 3/2).
Contributing

Quantum Overlays: Run PWT Quantum and Evolutionary Simulations

This notebook reproduces and extends the models from PWT blog Part 4: Correlations between harmonics and IE/EA, bond/polyatomic evo sims, and genome drift. Ties to Prime Wave Theory's reciprocal lens for quantum-evo insights.

Light as the Prime Key: Wave-Particle Duality and Prime 2 in PWT

Appendix D: Computational Implementation and Visualization
Prime Wave Theory (PWT) - Version 15.1
This module provides complete implementations for:
1. Computing the Prime Wave P_k(x)
2. Fourier coefficient calculation
3. Visualization (wave plots and spectra)
4. Numerical verification of theorems
Author: Tusk
Date: October 16, 2025
License: MIT (for research use)

Prime Wave Theory V15.2:
Causal Necessity of Prime-Indexed Discrete Scale Invariance
in Emergent Agency
1. Coherence Increase - Generating phi_d_plot
2. Negative Phase Dominance - Generating fourier_spectrum_plot
3. Memory Enhancement - Generating memory_persistence_plot

Prime Wave Theory (PWT) Model Implementation
1 This script implements the refined damped model developed in our explorations.
2 It includes functions for symbolic and numerical fits, prime factorization checks,
3 and examples from atomic spectra, redshifts, particle masses, and the sterile neutrino prediction.
4 Dependencies: sympy, numpy, scipy.optimize (for curve_fit)

README.md: Instructions for running (e.g., "Install dependencies: pip install numpy sympy scipy matplotlib pulp; Run in Jupyter").
- balmer_sim.ipynb
- emf_sim.ipynb
- entropy_sim.ipynb
balmer_sim.ipynb (Light as the Prime Key)
emf_sim.ipynb (Prime Harmonics Across the EMF Spectrum)
entropy_sim.ipynb (Light, Entropy, and Negentropy)

We welcome contributions to expand PWT! Ideas:

    Add new tools (e.g., Harmonic Cascade simulator for quantum energies).
    Enhance simulations (e.g., visualize prime drifts with matplotlib).
    Test predictions (e.g., prime signatures in other genomes like viral DNA).

To contribute:

    Fork the repo and create a branch (git checkout -b feature/new-tool).
    Commit changes (git commit -m "Add Harmonic Cascade simulator").
    Push (git push origin feature/new-tool).
    Open a Pull Request with a description linking to PWT concepts.

Please follow the Code of Conduct (add one if needed).
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

    Creator: Tusk Bilasimo
    Blog: pwt.life
    Issues: Open a GitHub issue for bugs or ideas.
    Community: Join discussions on the blog or fork to collaborate!

Let's polish the PWT lens together—explore, experiment, and uncover the prime symphony of the universe! 🚀
