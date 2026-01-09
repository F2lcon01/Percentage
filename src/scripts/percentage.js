/**
 * Neon Pulse Calculator - Percentage Module
 * Handles percentage calculations
 */

class PercentageCalculator {
    constructor() {
        this.form = null;
        this.resultContainer = null;
        this.resultValue = null;
    }

    /**
     * Initialize the percentage calculator
     */
    init() {
        this.form = document.getElementById('percentage-form');
        this.resultContainer = document.getElementById('percentage-result');
        this.resultValue = document.getElementById('result-value');
        
        if (this.form) {
            this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        }
    }

    /**
     * Handle form submission
     * @param {Event} e - Submit event
     */
    handleSubmit(e) {
        e.preventDefault();
        
        const percentage = parseFloat(document.getElementById('percentage').value);
        const number = parseFloat(document.getElementById('number').value);
        const method = document.getElementById('method').value;

        // Validate inputs
        if (isNaN(percentage) || isNaN(number)) {
            this.showError('يرجى إدخال أرقام صحيحة');
            return;
        }

        // Calculate result
        const result = this.calculate(percentage, number, method);
        
        // Show result with animation
        this.showResult(result, percentage, number, method);
    }

    /**
     * Perform the calculation
     * @param {number} percentage - Percentage value
     * @param {number} number - Base number
     * @param {string} method - Calculation method
     * @returns {number} - Calculated result
     */
    calculate(percentage, number, method) {
        switch (method) {
            case 'extract':
                return (percentage / 100) * number;
            case 'add':
                return number + (percentage / 100) * number;
            case 'subtract':
                return number - (percentage / 100) * number;
            default:
                return 0;
        }
    }

    /**
     * Format the result message
     * @param {number} percentage - Percentage value
     * @param {number} number - Base number
     * @param {string} method - Calculation method
     * @returns {string} - Formatted message
     */
    formatMessage(percentage, number, method) {
        const messages = {
            extract: `${percentage}% من ${number}`,
            add: `${number} + ${percentage}%`,
            subtract: `${number} - ${percentage}%`
        };
        return messages[method] || '';
    }

    /**
     * Show the result
     * @param {number} result - Calculated result
     * @param {number} percentage - Percentage value
     * @param {number} number - Base number
     * @param {string} method - Calculation method
     */
    showResult(result, percentage, number, method) {
        if (this.resultContainer) {
            this.resultContainer.classList.remove('hidden');
            
            // Update result label
            const resultLabel = this.resultContainer.querySelector('.result-label');
            if (resultLabel) {
                resultLabel.textContent = this.formatMessage(percentage, number, method);
            }
            
            // Animate result value
            if (this.resultValue) {
                this.animateValue(this.resultValue, 0, result, 500);
            }
            
            // Add glow animation
            this.resultContainer.classList.add('animate-bounce-in', 'animate-glow');
            setTimeout(() => {
                this.resultContainer.classList.remove('animate-bounce-in');
            }, 500);
        }
    }

    /**
     * Show error message
     * @param {string} message - Error message
     */
    showError(message) {
        if (this.resultContainer) {
            this.resultContainer.classList.remove('hidden');
            
            const resultLabel = this.resultContainer.querySelector('.result-label');
            if (resultLabel) {
                resultLabel.textContent = message;
            }
            
            if (this.resultValue) {
                this.resultValue.textContent = '⚠️';
            }
            
            this.resultContainer.classList.add('animate-shake');
            setTimeout(() => {
                this.resultContainer.classList.remove('animate-shake');
            }, 500);
        }
    }

    /**
     * Use calculator result as input
     */
    useCalculatorResult() {
        const calcResult = calculator.getCurrentResult();
        
        if (calcResult !== null) {
            const numberInput = document.getElementById('number');
            if (numberInput) {
                numberInput.value = calcResult;
                
                // Animate the input
                numberInput.classList.add('animate-glow');
                setTimeout(() => {
                    numberInput.classList.remove('animate-glow');
                }, 500);
            }
        } else {
            // Show feedback that there's no value
            const btn = document.querySelector('.btn-use-calculator');
            if (btn) {
                btn.classList.add('animate-shake');
                setTimeout(() => {
                    btn.classList.remove('animate-shake');
                }, 500);
            }
        }
    }

    /**
     * Animate value counting up
     * @param {HTMLElement} element - Element to animate
     * @param {number} start - Start value
     * @param {number} end - End value
     * @param {number} duration - Animation duration
     */
    animateValue(element, start, end, duration) {
        const startTime = performance.now();
        const isDecimal = !Number.isInteger(end);
        
        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease out cubic
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            
            const current = start + (end - start) * easeProgress;
            
            if (isDecimal) {
                element.textContent = current.toFixed(2);
            } else {
                element.textContent = Math.round(current).toLocaleString('ar-EG');
            }
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                // Final value with proper formatting
                if (isDecimal) {
                    element.textContent = end.toFixed(2);
                } else {
                    element.textContent = end.toLocaleString('ar-EG');
                }
            }
        };
        
        requestAnimationFrame(animate);
    }
}

// Export for use in other modules
const percentageCalculator = new PercentageCalculator();
