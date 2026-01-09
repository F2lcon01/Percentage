/**
 * Neon Pulse Calculator - Main Application
 * Initializes and coordinates all modules
 */

class App {
    constructor() {
        this.currentSection = 'percentage';
    }

    /**
     * Initialize the application
     */
    init() {
        // Initialize all modules
        animations.init();
        calculator.init();
        percentageCalculator.init();

        // Setup navigation
        this.setupNavigation();
        
        // Show initial section
        this.showSection(this.currentSection);
        
        // Setup event listeners
        this.setupEventListeners();

        console.log('🚀 Neon Pulse Calculator initialized!');
    }

    /**
     * Setup navigation tabs
     */
    setupNavigation() {
        const navTabs = document.querySelectorAll('.nav-tab');
        
        navTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const section = tab.dataset.section;
                if (section && section !== this.currentSection) {
                    this.showSection(section);
                }
            });
        });
    }

    /**
     * Show a specific section
     * @param {string} sectionId - ID of section to show
     */
    showSection(sectionId) {
        const currentSectionEl = document.getElementById(`${this.currentSection}-section`);
        const newSectionEl = document.getElementById(`${sectionId}-section`);
        
        if (!newSectionEl) return;

        // Update current section
        const oldSection = this.currentSection;
        this.currentSection = sectionId;

        // Update navigation
        this.updateNavigation(sectionId);

        // Animate transition
        if (currentSectionEl && oldSection !== sectionId) {
            animations.animateSectionTransition(currentSectionEl, newSectionEl);
        } else {
            newSectionEl.classList.add('active');
        }
    }

    /**
     * Update navigation active state
     * @param {string} activeSection - Active section ID
     */
    updateNavigation(activeSection) {
        const navTabs = document.querySelectorAll('.nav-tab');
        
        navTabs.forEach(tab => {
            if (tab.dataset.section === activeSection) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        });
    }

    /**
     * Setup global event listeners
     */
    setupEventListeners() {
        // Use calculator result button
        const useCalcBtn = document.querySelector('.btn-use-calculator');
        if (useCalcBtn) {
            useCalcBtn.addEventListener('click', () => {
                percentageCalculator.useCalculatorResult();
            });
        }

        // Toggle history button
        const toggleHistoryBtn = document.querySelector('.btn-toggle-history');
        if (toggleHistoryBtn) {
            toggleHistoryBtn.addEventListener('click', () => {
                calculator.toggleHistory();
                toggleHistoryBtn.classList.toggle('active');
            });
        }

        // Keyboard shortcut to switch sections
        document.addEventListener('keydown', (e) => {
            if (e.altKey && e.key === '1') {
                e.preventDefault();
                this.showSection('percentage');
            } else if (e.altKey && e.key === '2') {
                e.preventDefault();
                this.showSection('calculator');
            }
        });
    }
}

// Global function wrappers for onclick handlers
function appendToDisplay(value) {
    calculator.appendToDisplay(value);
}

function clearDisplay() {
    calculator.clearDisplay();
}

function deleteLastCharacter() {
    calculator.deleteLastCharacter();
}

function calculate() {
    calculator.calculate();
}

function toggleHistory() {
    calculator.toggleHistory();
}

function useCalculatorResult() {
    percentageCalculator.useCalculatorResult();
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const app = new App();
    app.init();
});
