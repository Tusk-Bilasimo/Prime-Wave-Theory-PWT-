# This is a sample Python script.
def parse_harmonic(h):
    if '/' in h:
        a, b = map(float, h.split('/'))
        return a / b
    else:
        return float(h)

def get_position(num):
    # Define periods based on atomic number ranges
    if 1 <= num <= 2:
        period = 1
    elif 3 <= num <= 10:
        period = 2
    elif 11 <= num <= 18:
        period = 3
    elif 19 <= num <= 36:
        period = 4
    elif 37 <= num <= 54:
        period = 5
    elif 55 <= num <= 86:
        period = 6
    elif 87 <= num <= 118:
        period = 7
    else:
        period = 0

    # Default row = period, but adjust for f-block
    row = period
    if 58 <= num <= 71:  # Ce to Lu
        row = 8
        column = num - 55
    elif 90 <= num <= 103:  # Th to Lr
        row = 9
        column = num - 87
    else:
        # Group and column for main block
        if num in [1, 3, 11, 19, 37, 55, 87]:
            column = 1
        elif num in [4, 12, 20, 38, 56, 88]:
            column = 2
        elif num in [21, 39, 57, 89]:  # Group 3
            column = 3
        elif num in [22, 40, 72, 104]:  # Group 4
            column = 4
        elif num in [23, 41, 73, 105]:  # Group 5
            column = 5
        elif num in [24, 42, 74, 106]:  # Group 6
            column = 6
        elif num in [25, 43, 75, 107]:  # Group 7
            column = 7
        elif num in [26, 44, 76, 108]:  # Group 8
            column = 8
        elif num in [27, 45, 77, 109]:  # Group 9
            column = 9
        elif num in [28, 46, 78, 110]:  # Group 10
            column = 10
        elif num in [29, 47, 79, 111]:  # Group 11
            column = 11
        elif num in [30, 48, 80, 112]:  # Group 12
            column = 12
        elif num in [5, 13, 31, 49, 81, 113]:  # Group 13
            column = 13
        elif num in [6, 14, 32, 50, 82, 114]:  # Group 14
            column = 14
        elif num in [7, 15, 33, 51, 83, 115]:  # Group 15
            column = 15
        elif num in [8, 16, 34, 52, 84, 116]:  # Group 16
            column = 16
        elif num in [9, 17, 35, 53, 85, 117]:  # Group 17
            column = 17
        elif num in [2, 10, 18, 36, 54, 86, 118]:  # Group 18
            column = 18
        else:
            column = 0  # For f-block main

    return row, column

# List of elements with PWT data
elements = [
    {"num": 1, "symbol": "H", "name": "Hydrogen", "prime_sig": "1", "harmonic": "0"},
    {"num": 2, "symbol": "He", "name": "Helium", "prime_sig": "2", "harmonic": "1/2"},
    {"num": 3, "symbol": "Li", "name": "Lithium", "prime_sig": "3", "harmonic": "1/3"},
    {"num": 4, "symbol": "Be", "name": "Beryllium", "prime_sig": "2²", "harmonic": "1"},
    {"num": 5, "symbol": "B", "name": "Boron", "prime_sig": "5", "harmonic": "1/5"},
    {"num": 6, "symbol": "C", "name": "Carbon", "prime_sig": "2 × 3", "harmonic": "5/6"},
    {"num": 7, "symbol": "N", "name": "Nitrogen", "prime_sig": "7", "harmonic": "1/7"},
    {"num": 8, "symbol": "O", "name": "Oxygen", "prime_sig": "2³", "harmonic": "3/2"},
    {"num": 9, "symbol": "F", "name": "Fluorine", "prime_sig": "3²", "harmonic": "2/3"},
    {"num": 10, "symbol": "Ne", "name": "Neon", "prime_sig": "2 × 5", "harmonic": "7/10"},
    {"num": 11, "symbol": "Na", "name": "Sodium", "prime_sig": "11", "harmonic": "1/11"},
    {"num": 12, "symbol": "Mg", "name": "Magnesium", "prime_sig": "2² × 3", "harmonic": "4/3"},
    {"num": 13, "symbol": "Al", "name": "Aluminium", "prime_sig": "13", "harmonic": "1/13"},
    {"num": 14, "symbol": "Si", "name": "Silicon", "prime_sig": "2 × 7", "harmonic": "9/14"},
    {"num": 15, "symbol": "P", "name": "Phosphorus", "prime_sig": "3 × 5", "harmonic": "8/15"},
    {"num": 16, "symbol": "S", "name": "Sulfur", "prime_sig": "2⁴", "harmonic": "2"},
    {"num": 17, "symbol": "Cl", "name": "Chlorine", "prime_sig": "17", "harmonic": "1/17"},
    {"num": 18, "symbol": "Ar", "name": "Argon", "prime_sig": "2 × 3²", "harmonic": "7/6"},
    {"num": 19, "symbol": "K", "name": "Potassium", "prime_sig": "19", "harmonic": "1/19"},
    {"num": 20, "symbol": "Ca", "name": "Calcium", "prime_sig": "2² × 5", "harmonic": "6/5"},
    {"num": 21, "symbol": "Sc", "name": "Scandium", "prime_sig": "3 × 7", "harmonic": "10/21"},
    {"num": 22, "symbol": "Ti", "name": "Titanium", "prime_sig": "2 × 11", "harmonic": "13/22"},
    {"num": 23, "symbol": "V", "name": "Vanadium", "prime_sig": "23", "harmonic": "1/23"},
    {"num": 24, "symbol": "Cr", "name": "Chromium", "prime_sig": "2³ × 3", "harmonic": "11/6"},
    {"num": 25, "symbol": "Mn", "name": "Manganese", "prime_sig": "5²", "harmonic": "2/5"},
    {"num": 26, "symbol": "Fe", "name": "Iron", "prime_sig": "2 × 13", "harmonic": "15/26"},
    {"num": 27, "symbol": "Co", "name": "Cobalt", "prime_sig": "3³", "harmonic": "1"},
    {"num": 28, "symbol": "Ni", "name": "Nickel", "prime_sig": "2² × 7", "harmonic": "11/7"},
    {"num": 29, "symbol": "Cu", "name": "Copper", "prime_sig": "29", "harmonic": "1/29"},
    {"num": 30, "symbol": "Zn", "name": "Zinc", "prime_sig": "2 × 3 × 5", "harmonic": "23/30"},
    {"num": 31, "symbol": "Ga", "name": "Gallium", "prime_sig": "31", "harmonic": "1/31"},
    {"num": 32, "symbol": "Ge", "name": "Germanium", "prime_sig": "2⁵", "harmonic": "5/2"},
    {"num": 33, "symbol": "As", "name": "Arsenic", "prime_sig": "3 × 11", "harmonic": "14/33"},
    {"num": 34, "symbol": "Se", "name": "Selenium", "prime_sig": "2 × 17", "harmonic": "19/34"},
    {"num": 35, "symbol": "Br", "name": "Bromine", "prime_sig": "5 × 7", "harmonic": "12/35"},
    {"num": 36, "symbol": "Kr", "name": "Krypton", "prime_sig": "2² × 3²", "harmonic": "5/3"},
    {"num": 37, "symbol": "Rb", "name": "Rubidium", "prime_sig": "37", "harmonic": "1/37"},
    {"num": 38, "symbol": "Sr", "name": "Strontium", "prime_sig": "2 × 19", "harmonic": "21/38"},
    {"num": 39, "symbol": "Y", "name": "Yttrium", "prime_sig": "3 × 13", "harmonic": "16/39"},
    {"num": 40, "symbol": "Zr", "name": "Zirconium", "prime_sig": "2³ × 5", "harmonic": "8/5"},
    {"num": 41, "symbol": "Nb", "name": "Niobium", "prime_sig": "41", "harmonic": "1/41"},
    {"num": 42, "symbol": "Mo", "name": "Molybdenum", "prime_sig": "2 × 3 × 7", "harmonic": "31/42"},
    {"num": 43, "symbol": "Tc", "name": "Technetium", "prime_sig": "43", "harmonic": "1/43"},
    {"num": 44, "symbol": "Ru", "name": "Ruthenium", "prime_sig": "2² × 11", "harmonic": "13/11"},
    {"num": 45, "symbol": "Rh", "name": "Rhodium", "prime_sig": "3² × 5", "harmonic": "13/15"},
    {"num": 46, "symbol": "Pd", "name": "Palladium", "prime_sig": "2 × 23", "harmonic": "25/46"},
    {"num": 47, "symbol": "Ag", "name": "Silver", "prime_sig": "47", "harmonic": "1/47"},
    {"num": 48, "symbol": "Cd", "name": "Cadmium", "prime_sig": "2⁴ × 3", "harmonic": "13/6"},
    {"num": 49, "symbol": "In", "name": "Indium", "prime_sig": "7²", "harmonic": "2/7"},
    {"num": 50, "symbol": "Sn", "name": "Tin", "prime_sig": "2 × 5²", "harmonic": "9/10"},
    {"num": 51, "symbol": "Sb", "name": "Antimony", "prime_sig": "3 × 17", "harmonic": "20/51"},
    {"num": 52, "symbol": "Te", "name": "Tellurium", "prime_sig": "2² × 13", "harmonic": "15/13"},
    {"num": 53, "symbol": "I", "name": "Iodine", "prime_sig": "53", "harmonic": "1/53"},
    {"num": 54, "symbol": "Xe", "name": "Xenon", "prime_sig": "2 × 3³", "harmonic": "10/9"},
    {"num": 55, "symbol": "Cs", "name": "Caesium", "prime_sig": "5 × 11", "harmonic": "16/55"},
    {"num": 56, "symbol": "Ba", "name": "Barium", "prime_sig": "2³ × 7", "harmonic": "15/7"},
    {"num": 57, "symbol": "La", "name": "Lanthanum", "prime_sig": "3 × 19", "harmonic": "22/57"},
    {"num": 58, "symbol": "Ce", "name": "Cerium", "prime_sig": "2 × 29", "harmonic": "31/58"},
    {"num": 59, "symbol": "Pr", "name": "Praseodymium", "prime_sig": "59", "harmonic": "1/59"},
    {"num": 60, "symbol": "Nd", "name": "Neodymium", "prime_sig": "2² × 3 × 5", "harmonic": "29/15"},
    {"num": 61, "symbol": "Pm", "name": "Promethium", "prime_sig": "61", "harmonic": "1/61"},
    {"num": 62, "symbol": "Sm", "name": "Samarium", "prime_sig": "2 × 31", "harmonic": "33/62"},
    {"num": 63, "symbol": "Eu", "name": "Europium", "prime_sig": "3² × 7", "harmonic": "16/21"},
    {"num": 64, "symbol": "Gd", "name": "Gadolinium", "prime_sig": "2⁶", "harmonic": "3"},
    {"num": 65, "symbol": "Tb", "name": "Terbium", "prime_sig": "5 × 13", "harmonic": "18/65"},
    {"num": 66, "symbol": "Dy", "name": "Dysprosium", "prime_sig": "2 × 3 × 11", "harmonic": "40/66"},
    {"num": 67, "symbol": "Ho", "name": "Holmium", "prime_sig": "67", "harmonic": "1/67"},
    {"num": 68, "symbol": "Er", "name": "Erbium", "prime_sig": "2² × 17", "harmonic": "19/17"},
    {"num": 69, "symbol": "Tm", "name": "Thulium", "prime_sig": "3 × 23", "harmonic": "26/69"},
    {"num": 70, "symbol": "Yb", "name": "Ytterbium", "prime_sig": "2 × 5 × 7", "harmonic": "26/35"},
    {"num": 71, "symbol": "Lu", "name": "Lutetium", "prime_sig": "71", "harmonic": "1/71"},
    {"num": 72, "symbol": "Hf", "name": "Hafnium", "prime_sig": "2³ × 3²", "harmonic": "2"},
    {"num": 73, "symbol": "Ta", "name": "Tantalum", "prime_sig": "73", "harmonic": "1/73"},
    {"num": 74, "symbol": "W", "name": "Tungsten", "prime_sig": "2 × 37", "harmonic": "39/74"},
    {"num": 75, "symbol": "Re", "name": "Rhenium", "prime_sig": "3 × 5²", "harmonic": "16/15"},
    {"num": 76, "symbol": "Os", "name": "Osmium", "prime_sig": "2² × 19", "harmonic": "21/19"},
    {"num": 77, "symbol": "Ir", "name": "Iridium", "prime_sig": "7 × 11", "harmonic": "18/77"},
    {"num": 78, "symbol": "Pt", "name": "Platinum", "prime_sig": "2 × 3 × 13", "harmonic": "45/78"},
    {"num": 79, "symbol": "Au", "name": "Gold", "prime_sig": "79", "harmonic": "1/79"},
    {"num": 80, "symbol": "Hg", "name": "Mercury", "prime_sig": "2⁴ × 5", "harmonic": "13/5"},
    {"num": 81, "symbol": "Tl", "name": "Thallium", "prime_sig": "3⁴", "harmonic": "4/3"},
    {"num": 82, "symbol": "Pb", "name": "Lead", "prime_sig": "2 × 41", "harmonic": "43/82"},
    {"num": 83, "symbol": "Bi", "name": "Bismuth", "prime_sig": "83", "harmonic": "1/83"},
    {"num": 84, "symbol": "Po", "name": "Polonium", "prime_sig": "2² × 3 × 7", "harmonic": "38/21"},
    {"num": 85, "symbol": "At", "name": "Astatine", "prime_sig": "5 × 17", "harmonic": "22/85"},
    {"num": 86, "symbol": "Rn", "name": "Radon", "prime_sig": "2 × 43", "harmonic": "45/86"},
    {"num": 87, "symbol": "Fr", "name": "Francium", "prime_sig": "3 × 29", "harmonic": "32/87"},
    {"num": 88, "symbol": "Ra", "name": "Radium", "prime_sig": "2³ × 11", "harmonic": "25/22"},
    {"num": 89, "symbol": "Ac", "name": "Actinium", "prime_sig": "89", "harmonic": "1/89"},
    {"num": 90, "symbol": "Th", "name": "Thorium", "prime_sig": "2 × 3² × 5", "harmonic": "28/15"},
    {"num": 91, "symbol": "Pa", "name": "Protactinium", "prime_sig": "7 × 13", "harmonic": "20/91"},
    {"num": 92, "symbol": "U", "name": "Uranium", "prime_sig": "2² × 23", "harmonic": "25/23"},
    {"num": 93, "symbol": "Np", "name": "Neptunium", "prime_sig": "3 × 31", "harmonic": "34/93"},
    {"num": 94, "symbol": "Pu", "name": "Plutonium", "prime_sig": "2 × 47", "harmonic": "49/94"},
    {"num": 95, "symbol": "Am", "name": "Americium", "prime_sig": "5 × 19", "harmonic": "24/95"},
    {"num": 96, "symbol": "Cm", "name": "Curium", "prime_sig": "2⁵ × 3", "harmonic": "19/6"},
    {"num": 97, "symbol": "Bk", "name": "Berkelium", "prime_sig": "97", "harmonic": "1/97"},
    {"num": 98, "symbol": "Cf", "name": "Californium", "prime_sig": "2 × 7²", "harmonic": "15/14"},
    {"num": 99, "symbol": "Es", "name": "Einsteinium", "prime_sig": "3² × 11", "harmonic": "17/33"},
    {"num": 100, "symbol": "Fm", "name": "Fermium", "prime_sig": "2² × 5²", "harmonic": "7/5"},
    {"num": 101, "symbol": "Md", "name": "Mendelevium", "prime_sig": "101", "harmonic": "1/101"},
    {"num": 102, "symbol": "No", "name": "Nobelium", "prime_sig": "2 × 3 × 17", "harmonic": "62/102"},
    {"num": 103, "symbol": "Lr", "name": "Lawrencium", "prime_sig": "103", "harmonic": "1/103"},
    {"num": 104, "symbol": "Rf", "name": "Rutherfordium", "prime_sig": "2³ × 13", "harmonic": "15/13"},
    {"num": 105, "symbol": "Db", "name": "Dubnium", "prime_sig": "3 × 5 × 7", "harmonic": "47/105"},
    {"num": 106, "symbol": "Sg", "name": "Seaborgium", "prime_sig": "2 × 53", "harmonic": "55/106"},
    {"num": 107, "symbol": "Bh", "name": "Bohrium", "prime_sig": "107", "harmonic": "1/107"},
    {"num": 108, "symbol": "Hs", "name": "Hassium", "prime_sig": "2² × 3³", "harmonic": "11/9"},
    {"num": 109, "symbol": "Mt", "name": "Meitnerium", "prime_sig": "109", "harmonic": "1/109"},
    {"num": 110, "symbol": "Ds", "name": "Darmstadtium", "prime_sig": "2 × 5 × 11", "harmonic": "38/110"},
    {"num": 111, "symbol": "Rg", "name": "Roentgenium", "prime_sig": "3 × 37", "harmonic": "40/111"},
    {"num": 112, "symbol": "Cn", "name": "Copernicium", "prime_sig": "2⁴ × 7", "harmonic": "17/7"},
    {"num": 113, "symbol": "Nh", "name": "Nihonium", "prime_sig": "113", "harmonic": "1/113"},
    {"num": 114, "symbol": "Fl", "name": "Flerovium", "prime_sig": "2 × 3 × 19", "harmonic": "60/114"},
    {"num": 115, "symbol": "Mc", "name": "Moscovium", "prime_sig": "5 × 23", "harmonic": "28/115"},
    {"num": 116, "symbol": "Lv", "name": "Livermorium", "prime_sig": "2² × 29", "harmonic": "31/29"},
    {"num": 117, "symbol": "Ts", "name": "Tennessine", "prime_sig": "3² × 13", "harmonic": "19/39"},
    {"num": 118, "symbol": "Og", "name": "Oganesson", "prime_sig": "2 × 59", "harmonic": "61/118"},
]

# Add row and column to each element
for e in elements:
    e['row'], e['column'] = get_position(e['num'])
    h_float = parse_harmonic(e['harmonic'])
    if h_float < 0.5:
        e['harmonic_class'] = 'low-harmonic'
    elif 0.5 <= h_float <= 1:
        e['harmonic_class'] = 'medium-harmonic'
    else:
        e['harmonic_class'] = 'high-harmonic'

# Generate HTML
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive Periodic Table Highlighting Prime Wave Theory (PWT) Harmonics</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 60px);
            grid-template-rows: repeat(9, 60px);
            grid-gap: 2px;
            justify-content: center;
        }
        .element {
            position: relative;
            border: 1px solid #ccc;
            text-align: center;
            padding: 5px;
            cursor: pointer;
            color: white;
        }
        .low-harmonic {
            background-color: blue;
        }
        .medium-harmonic {
            background-color: green;
        }
        .high-harmonic {
            background-color: red;
        }
        .symbol {
            font-weight: bold;
        }
        .tooltip {
            display: none;
            position: absolute;
            background: white;
            color: black;
            border: 1px solid black;
            padding: 5px;
            z-index: 10;
            left: 70px;
            top: 0;
        }
        .element:hover .tooltip {
            display: block;
        }
        #modal {
            display: none;
            position: fixed;
            z-index: 100;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            justify-content: center;
            align-items: center;
        }
        #modal-content {
            background: white;
            padding: 20px;
            border: 1px solid #888;
            width: 300px;
        }
        #close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        #close:hover {
            color: black;
            cursor: pointer;
        }
        .legend {
            margin: 20px;
        }
        .legend-item {
            display: inline-block;
            margin-right: 20px;
        }
        .legend-color {
            width: 20px;
            height: 20px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>Interactive Periodic Table Highlighting Prime Wave Theory (PWT) Harmonics</h1>
    <div class="legend">
        <div class="legend-item"><span class="legend-color low-harmonic"></span> Low Harmonic (<0.5)</div>
        <div class="legend-item"><span class="legend-color medium-harmonic"></span> Medium Harmonic (0.5-1)</div>
        <div class="legend-item"><span class="legend-color high-harmonic"></span> High Harmonic (>1)</div>
    </div>
    <div class="periodic-table">
"""

for e in elements:
    html += f'''
        <div class="element {e["harmonic_class"]}" style="grid-row: {e["row"]}; grid-column: {e["column"]};" data-name="{e["name"]}" data-prime="{e["prime_sig"]}" data-harmonic="{e["harmonic"]}">
            <div class="num">{e["num"]}</div>
            <div class="symbol">{e["symbol"]}</div>
            <div class="tooltip">
                <p>{e["name"]}</p>
                <p>Prime Signature: {e["prime_sig"]}</p>
                <p>Harmonic: {e["harmonic"]}</p>
            </div>
        </div>
'''

html += """
    </div>
    <div id="modal">
        <div id="modal-content">
            <span id="close">&times;</span>
            <div id="content"></div>
        </div>
    </div>
    <script>
        var modal = document.getElementById("modal");
        var close = document.getElementById("close");
        var content = document.getElementById("content");
        document.querySelectorAll('.element').forEach(function(el) {
            el.addEventListener('click', function() {
                content.innerHTML = `
                    <p>Name: ${el.dataset.name}</p>
                    <p>Prime Signature: ${el.dataset.prime}</p>
                    <p>Harmonic Prime Signature: ${el.dataset.harmonic}</p>
                `;
                modal.style.display = 'flex';
            });
        });
        close.addEventListener('click', function() {
            modal.style.display = 'none';
        });
        window.addEventListener('click', function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    </script>
</body>
</html>
"""

with open("pwt_periodic_table.html", "w") as f:
    f.write(html)

print("Interactive periodic table generated as pwt_periodic_table.html")
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
