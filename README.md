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
