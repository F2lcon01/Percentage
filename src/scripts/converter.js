/**
 * Neon Pulse Calculator - Unit Converter Module
 * Handles all unit conversions for length, mass, and digital storage
 */

class UnitConverter {
    constructor() {
        // Define unit categories with display names (Arabic)
        this.categories = {
            length: {
                name: 'الطول',
                icon: '📏',
                units: [
                    { id: 'nm', name: 'نانومتر (nm)' },
                    { id: 'um', name: 'ميكرومتر (μm)' },
                    { id: 'mm', name: 'مليمتر (mm)' },
                    { id: 'cm', name: 'سنتيمتر (cm)' },
                    { id: 'm', name: 'متر (m)' },
                    { id: 'km', name: 'كيلومتر (km)' },
                    { id: 'inch', name: 'بوصة (in)' },
                    { id: 'foot', name: 'قدم (ft)' },
                    { id: 'yard', name: 'ياردة (yd)' },
                    { id: 'mile', name: 'ميل (mi)' }
                ]
            },
            mass: {
                name: 'الوزن',
                icon: '⚖️',
                units: [
                    { id: 'mg', name: 'ميليغرام (mg)' },
                    { id: 'g', name: 'غرام (g)' },
                    { id: 'kg', name: 'كيلوغرام (kg)' },
                    { id: 'tonne', name: 'طن (t)' },
                    { id: 'oz', name: 'أونصة (oz)' },
                    { id: 'lb', name: 'رطل (lb)' }
                ]
            },
            storage: {
                name: 'البيانات',
                icon: '💾',
                units: [
                    { id: 'b', name: 'بت (b)' },
                    { id: 'B', name: 'بايت (B)' },
                    { id: 'KB', name: 'كيلوبايت (KB)' },
                    { id: 'MB', name: 'ميغابايت (MB)' },
                    { id: 'GB', name: 'غيغابايت (GB)' },
                    { id: 'TB', name: 'تيرابايت (TB)' },
                    { id: 'PB', name: 'بيتابايت (PB)' }
                ]
            }
        };

        this.currentCategory = 'length';
        this.fromUnit = 'm';
        this.toUnit = 'cm';
        this.inputValue = 1;
    }

    /**
     * Initialize the converter
     */
    init() {
        this.categoryButtons = document.querySelectorAll('.converter-category-btn');
        this.fromSelect = document.getElementById('converter-from');
        this.toSelect = document.getElementById('converter-to');
        this.inputField = document.getElementById('converter-input');
        this.resultDisplay = document.getElementById('converter-result');
        this.formulaDisplay = document.getElementById('converter-formula');
        this.swapBtn = document.getElementById('converter-swap');

        this.setupEventListeners();
        this.populateUnits();
        this.convert();
    }

    /**
     * Setup all event listeners
     */
    setupEventListeners() {
        // Category buttons
        this.categoryButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.setCategory(btn.dataset.category);
            });
        });

        // Input field
        if (this.inputField) {
            this.inputField.addEventListener('input', () => {
                this.inputValue = parseFloat(this.inputField.value) || 0;
                this.convert();
            });
        }

        // From/To selects
        if (this.fromSelect) {
            this.fromSelect.addEventListener('change', () => {
                this.fromUnit = this.fromSelect.value;
                this.convert();
            });
        }

        if (this.toSelect) {
            this.toSelect.addEventListener('change', () => {
                this.toUnit = this.toSelect.value;
                this.convert();
            });
        }

        // Swap button
        if (this.swapBtn) {
            this.swapBtn.addEventListener('click', () => {
                this.swapUnits();
            });
        }
    }

    /**
     * Set the active category
     * @param {string} category - Category ID
     */
    setCategory(category) {
        if (!this.categories[category]) return;

        this.currentCategory = category;

        // Update active button
        this.categoryButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.category === category);
        });

        // Repopulate units
        this.populateUnits();
        this.convert();
    }

    /**
     * Populate the unit dropdowns based on current category
     */
    populateUnits() {
        const units = this.categories[this.currentCategory].units;

        // Clear and populate From select
        if (this.fromSelect) {
            this.fromSelect.innerHTML = units.map(u => 
                `<option value="${u.id}">${u.name}</option>`
            ).join('');
            this.fromSelect.value = units[0].id;
            this.fromUnit = units[0].id;
        }

        // Clear and populate To select
        if (this.toSelect) {
            this.toSelect.innerHTML = units.map(u => 
                `<option value="${u.id}">${u.name}</option>`
            ).join('');
            // Default to second unit if available
            this.toSelect.value = units.length > 1 ? units[1].id : units[0].id;
            this.toUnit = this.toSelect.value;
        }
    }

    /**
     * Swap the from and to units
     */
    swapUnits() {
        const temp = this.fromUnit;
        this.fromUnit = this.toUnit;
        this.toUnit = temp;

        if (this.fromSelect) this.fromSelect.value = this.fromUnit;
        if (this.toSelect) this.toSelect.value = this.toUnit;

        // Animate the swap button
        if (this.swapBtn) {
            this.swapBtn.classList.add('animate-rotate');
            setTimeout(() => this.swapBtn.classList.remove('animate-rotate'), 300);
        }

        this.convert();
    }

    /**
     * Perform the conversion
     */
    convert() {
        if (!this.inputValue && this.inputValue !== 0) {
            this.showResult(0, '');
            return;
        }

        try {
            let result;
            
            // Use math.js for conversion
            if (this.currentCategory === 'storage') {
                // Handle storage units specially (math.js uses different notation)
                result = this.convertStorage(this.inputValue, this.fromUnit, this.toUnit);
            } else {
                const fromValue = math.unit(this.inputValue, this.fromUnit);
                result = fromValue.to(this.toUnit).toNumber();
            }

            // Format the result
            const formattedResult = this.formatNumber(result);
            const formula = `${this.inputValue} ${this.fromUnit} = ${formattedResult} ${this.toUnit}`;
            
            this.showResult(formattedResult, formula);

        } catch (error) {
            console.error('Conversion error:', error);
            this.showResult('خطأ', '');
        }
    }

    /**
     * Handle storage unit conversion
     * @param {number} value - Input value
     * @param {string} from - From unit
     * @param {string} to - To unit
     * @returns {number} - Converted value
     */
    convertStorage(value, from, to) {
        // Storage units in bits
        const storageUnits = {
            'b': 1,
            'B': 8,
            'KB': 8 * 1024,
            'MB': 8 * 1024 * 1024,
            'GB': 8 * 1024 * 1024 * 1024,
            'TB': 8 * 1024 * 1024 * 1024 * 1024,
            'PB': 8 * 1024 * 1024 * 1024 * 1024 * 1024
        };

        const fromBits = value * storageUnits[from];
        return fromBits / storageUnits[to];
    }

    /**
     * Format number for display
     * @param {number} num - Number to format
     * @returns {string} - Formatted number
     */
    formatNumber(num) {
        if (num === 0) return '0';
        
        // Handle very small or very large numbers with scientific notation
        if (Math.abs(num) < 0.000001 || Math.abs(num) >= 1000000000) {
            return num.toExponential(6);
        }
        
        // Round to reasonable precision
        const precision = num < 1 ? 8 : 6;
        return parseFloat(num.toPrecision(precision)).toString();
    }

    /**
     * Display the result
     * @param {string|number} result - The result to display
     * @param {string} formula - The formula string
     */
    showResult(result, formula) {
        if (this.resultDisplay) {
            this.resultDisplay.textContent = result;
            this.resultDisplay.classList.add('animate-scale-in');
            setTimeout(() => this.resultDisplay.classList.remove('animate-scale-in'), 300);
        }

        if (this.formulaDisplay) {
            this.formulaDisplay.textContent = formula;
        }
    }
}

// Export for use in other modules
const unitConverter = new UnitConverter();
