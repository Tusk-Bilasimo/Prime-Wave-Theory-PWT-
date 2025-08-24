# Prime Wave Theory (PWT) Repository

Welcome to the Prime Wave Theory (PWT) GitHub repository! PWT is a protoscientific framework exploring the universe through the lens of prime numbers, harmonic cascades, and reciprocal duality. Inspired by the [PWT Thesis V6](https://img1.wsimg.com/blobby/go/9e7c14d7-bed2-41da-a404-fe5da210ac73/downloads/24ef2270-454a-41e1-b753-f1dbcbc2e2b3/PWT_Thesis_V6.pdf?ver=1755844804910), this repo hosts code tools to model PWT concepts, from variable gravity predictors to DNA prime signature analyzers. Our goal is to foster community collaboration, turning PWT's insights into interactive, testable explorations of quantum harmonics, cosmic scaling, negentropy in biology, and beyond.

For more context, check out the [PWT.life blog](https://pwt.life/blog), including posts like [Variable Gravity Through the PWT Lens](https://pwt.life/blog/f/variable-gravity-through-the-pwt-lens-a-bridge-from-micro-to-mac) and [PWT Prime-Driven Order in Biology and Consciousness](https://pwt.life/blog/f/pwt-prime-driven-order-in-biology-and-consciousness), which reference tools here.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To run the tools locally:

1. Clone the repo:
2. 
2. Install dependencies (Python 3.12+ recommended):
3. - For Jupyter notebooks: `pip install notebook` (or `jupyterlab` for advanced use).

3. For interactive runs: Open Jupyter with `jupyter notebook` and load .ipynb files.

Note: Some tools (e.g., DNA analyzers) fetch data from NCBI—replace `Entrez.email` in the code with your real email to avoid rate limits.

## Usage

This repo includes Python scripts and notebooks for PWT simulations. Key files:

- **`dna_prime_analyzer.py`**: Analyzes DNA sequences for prime signatures in codon counts, simulates evolutionary drifts to model negentropy. For details, see the blog post [PWT Prime-Driven Order in Biology and Consciousness](https://pwt.life/blog/f/pwt-prime-driven-order-in-biology-and-consciousness).
- Run: `python dna_prime_analyzer.py`
- Customize: Edit accession/start/end for different genes.

- **`PWT_DNA_Prime_Analyzer.ipynb`**: Interactive Jupyter version for browser-based experimentation—run it online via Binder! [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Tusk-Bilasimo/Prime-Wave-Theory-PWT-/main?labpath=PWT_DNA_Prime_Analyzer.ipynb)
- Open in Jupyter to explore prime drifts in real-time, tying to PWT's negentropy concepts.

- **`g_variation_predictor.py`** (from variable gravity post): Predicts G variations based on atomic primes.
- Run: `python g_variation_predictor.py`

For full usage details, see comments in each file.

## Examples

### DNA Prime Analysis
Fetch and analyze the HBB gene:

Output might show prime counts (e.g., 3 for certain codons, tying to Matter stability in PWT).

### Evolutionary Simulation
Simulate drifts:

Observe how prime signatures persist, illustrating negentropy.

### Jupyter Interactive
Open `PWT_DNA_Prime_Analyzer.ipynb` in Jupyter, run cells, and tweak parameters (e.g., mutation_rate=0.05 for more chaos) to see prime rebounds.

## Contributing

We welcome contributions to expand PWT! Ideas:
- Add new tools (e.g., Harmonic Cascade simulator for quantum energies).
- Enhance simulations (e.g., visualize prime drifts with matplotlib).
- Test predictions (e.g., prime signatures in other genomes like viral DNA).

To contribute:
1. Fork the repo and create a branch (`git checkout -b feature/new-tool`).
2. Commit changes (`git commit -m "Add Harmonic Cascade simulator"`).
3. Push (`git push origin feature/new-tool`).
4. Open a Pull Request with a description linking to PWT concepts.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) (add one if needed).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Creator**: Tusk Bilasimo
- **Blog**: [pwt.life](https://pwt.life)
- **Issues**: Open a GitHub issue for bugs or ideas.
- **Community**: Join discussions on the blog or fork to collaborate!

Let's polish the PWT lens together—explore, experiment, and uncover the prime symphony of the universe! 🚀
