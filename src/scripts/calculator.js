/**
 * Neon Pulse Calculator - Calculator Module
 * Handles all calculator operations and history
 */

class Calculator {
    constructor() {
        this.display = null;
        this.historyPanel = null;
        this.history = [];
        this.currentValue = '';
        this.maxHistoryItems = 20;
    }

    /**
     * Initialize the calculator
     */
    init() {
        this.display = document.getElementById('calc-display');
        this.historyPanel = document.getElementById('calc-history');
        
        // Load history from localStorage
        this.loadHistory();
        
        // Setup keyboard support
        this.setupKeyboardSupport();
    }

    /**
     * Append value to display
     * @param {string} value - Value to append
     */
    appendToDisplay(value) {
        if (this.currentValue === 'خطأ') {
            this.clearDisplay();
        }
        this.currentValue += value;
        this.updateDisplay();
        
        // Trigger button animation
        this.animateInput();
    }

    /**
     * Clear the display
     */
    clearDisplay() {
        this.currentValue = '';
        this.updateDisplay();
    }

    /**
     * Delete the last character
     */
    deleteLastCharacter() {
        this.currentValue = this.currentValue.slice(0, -1);
        this.updateDisplay();
    }

    /**
     * Update the display element
     */
    updateDisplay() {
        if (this.display) {
            this.display.value = this.currentValue || '0';
        }
    }

    /**
     * Perform calculation
     */
    calculate() {
        if (!this.currentValue) return;

        try {
            // Use math.js for safe evaluation
            const result = math.evaluate(this.currentValue);
            
            // Add to history
            this.addToHistory(this.currentValue, result);
            
            // Update display with animation
            this.currentValue = result.toString();
            this.updateDisplay();
            this.animateResult();
            
        } catch (error) {
            this.currentValue = 'خطأ';
            this.updateDisplay();
            this.animateError();
        }
    }

    /**
     * Add calculation to history
     * @param {string} expression - The expression
     * @param {number} result - The result
     */
    addToHistory(expression, result) {
        const entry = {
            expression: expression,
            result: result,
            timestamp: Date.now()
        };

        this.history.unshift(entry);
        
        // Limit history size
        if (this.history.length > this.maxHistoryItems) {
            this.history.pop();
        }

        this.saveHistory();
        this.renderHistory();
    }

    /**
     * Render history to the DOM
     */
    renderHistory() {
        // Dynamically get historyPanel if not already set
        if (!this.historyPanel) {
            this.historyPanel = document.getElementById('calc-history');
            if (!this.historyPanel) return;
        }

        if (this.history.length === 0) {
            this.historyPanel.innerHTML = `
                <div class="history-empty">
                    <span>لا توجد عمليات سابقة</span>
                </div>
            `;
            return;
        }

        this.historyPanel.innerHTML = this.history.map((entry, index) => `
            <div class="history-item animate-fade-in-up stagger-${Math.min(index + 1, 8)}" 
                 data-index="${index}"
                 onclick="calculator.useHistoryResult(${index})">
                <span class="history-expression">${entry.expression}</span>
                <span class="history-equals">=</span>
                <span class="history-result">${entry.result}</span>
            </div>
        `).join('');
    }

    /**
     * Use result from history
     * @param {number} index - History item index
     */
    useHistoryResult(index) {
        const entry = this.history[index];
        if (entry) {
            this.currentValue = entry.result.toString();
            this.updateDisplay();
            this.animateInput();
        }
    }

    /**
     * Clear all history
     */
    clearHistory() {
        this.history = [];
        this.saveHistory();
        this.renderHistory();
    }

    /**
     * Toggle history panel visibility
     */
    toggleHistory() {
        // Ensure historyPanel reference is valid
        if (!this.historyPanel) {
            this.historyPanel = document.getElementById('calc-history');
            if (!this.historyPanel) return;
        }
        
        const isHidden = this.historyPanel.classList.contains('hidden');
        
        if (isHidden) {
            this.historyPanel.classList.remove('hidden');
            this.historyPanel.classList.add('animate-fade-in-up');
            // Re-render history when opening to ensure it's up to date
            this.renderHistory();
        } else {
            this.historyPanel.classList.add('hidden');
            this.historyPanel.classList.remove('animate-fade-in-up');
        }
    }

    /**
     * Save history to localStorage
     */
    saveHistory() {
        try {
            localStorage.setItem('calculatorHistory', JSON.stringify(this.history));
        } catch (e) {
            console.warn('Could not save history to localStorage');
        }
    }

    /**
     * Load history from localStorage
     */
    loadHistory() {
        try {
            const saved = localStorage.getItem('calculatorHistory');
            if (saved) {
                this.history = JSON.parse(saved);
                this.renderHistory();
            }
        } catch (e) {
            console.warn('Could not load history from localStorage');
            this.history = [];
        }
    }

    /**
     * Get current result for use in percentage calculator
     * @returns {number|null} - Current result or null
     */
    getCurrentResult() {
        const value = parseFloat(this.currentValue);
        return isNaN(value) ? null : value;
    }

    /**
     * Setup keyboard support
     */
    setupKeyboardSupport() {
        document.addEventListener('keydown', (e) => {
            // Only handle if calculator section is active
            const calcSection = document.getElementById('calculator-section');
            if (!calcSection || !calcSection.classList.contains('active')) return;

            const key = e.key;

            // Numbers
            if (/^[0-9]$/.test(key)) {
                e.preventDefault();
                this.appendToDisplay(key);
            }
            // Operators
            else if (['+', '-', '*', '/', '.', '(', ')'].includes(key)) {
                e.preventDefault();
                this.appendToDisplay(key);
            }
            // Enter = Calculate
            else if (key === 'Enter') {
                e.preventDefault();
                this.calculate();
            }
            // Backspace = Delete
            else if (key === 'Backspace') {
                e.preventDefault();
                this.deleteLastCharacter();
            }
            // Escape or Delete = Clear
            else if (key === 'Escape' || key === 'Delete') {
                e.preventDefault();
                this.clearDisplay();
            }
        });
    }

    /**
     * Animate input feedback
     */
    animateInput() {
        if (this.display) {
            this.display.classList.remove('animate-scale-in');
            void this.display.offsetWidth; // Trigger reflow
            this.display.classList.add('animate-scale-in');
        }
    }

    /**
     * Animate successful result
     */
    animateResult() {
        if (this.display) {
            this.display.classList.add('animate-glow');
            setTimeout(() => {
                this.display.classList.remove('animate-glow');
            }, 500);
        }
    }

    /**
     * Animate error state
     */
    animateError() {
        if (this.display) {
            this.display.classList.add('animate-shake');
            setTimeout(() => {
                this.display.classList.remove('animate-shake');
            }, 500);
        }
    }
}

// Export for use in other modules
const calculator = new Calculator();
