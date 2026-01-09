/**
 * Neon Pulse Calculator - Animations Module
 * Handles advanced animations and effects
 */

class Animations {
    constructor() {
        this.prefersReducedMotion = false;
    }

    /**
     * Initialize animations
     */
    init() {
        // Check for reduced motion preference
        this.prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        
        // Listen for preference changes
        window.matchMedia('(prefers-reduced-motion: reduce)')
            .addEventListener('change', (e) => {
                this.prefersReducedMotion = e.matches;
            });

        // Initialize stagger animations
        this.initStaggerAnimations();
        
        // Add ripple effect to buttons
        this.initRippleEffect();
    }

    /**
     * Initialize stagger animations for list elements
     */
    initStaggerAnimations() {
        if (this.prefersReducedMotion) return;

        const staggerElements = document.querySelectorAll('.stagger-init');
        
        staggerElements.forEach((el, index) => {
            setTimeout(() => {
                el.classList.add('stagger-animate');
            }, index * 100);
        });
    }

    /**
     * Initialize ripple effect on buttons
     */
    initRippleEffect() {
        if (this.prefersReducedMotion) return;

        document.addEventListener('click', (e) => {
            const button = e.target.closest('.btn, .calc-btn, .nav-tab');
            if (!button) return;

            this.createRipple(e, button);
        });
    }

    /**
     * Create ripple effect
     * @param {MouseEvent} e - Click event
     * @param {HTMLElement} element - Target element
     */
    createRipple(e, element) {
        const existingRipple = element.querySelector('.ripple');
        if (existingRipple) {
            existingRipple.remove();
        }

        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        const ripple = document.createElement('span');
        ripple.className = 'ripple';
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, transparent 70%);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s ease-out;
            pointer-events: none;
        `;

        element.style.position = 'relative';
        element.style.overflow = 'hidden';
        element.appendChild(ripple);

        ripple.addEventListener('animationend', () => {
            ripple.remove();
        });
    }

    /**
     * Animate section transition
     * @param {HTMLElement} outSection - Section leaving
     * @param {HTMLElement} inSection - Section entering
     */
    animateSectionTransition(outSection, inSection) {
        if (this.prefersReducedMotion) {
            outSection.classList.remove('active');
            inSection.classList.add('active');
            return;
        }

        // Fade out
        outSection.style.opacity = '0';
        outSection.style.transform = 'translateX(-20px)';
        
        setTimeout(() => {
            outSection.classList.remove('active');
            outSection.style.opacity = '';
            outSection.style.transform = '';
            
            // Fade in
            inSection.classList.add('active');
            inSection.style.opacity = '0';
            inSection.style.transform = 'translateX(20px)';
            
            requestAnimationFrame(() => {
                inSection.style.transition = 'all 0.3s ease-out';
                inSection.style.opacity = '1';
                inSection.style.transform = 'translateX(0)';
                
                setTimeout(() => {
                    inSection.style.transition = '';
                    inSection.style.opacity = '';
                    inSection.style.transform = '';
                }, 300);
            });
        }, 200);
    }

    /**
     * Create particle burst effect
     * @param {HTMLElement} element - Source element
     * @param {string} color - Particle color
     */
    createParticleBurst(element, color = 'var(--color-neon-cyan)') {
        if (this.prefersReducedMotion) return;

        const rect = element.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        for (let i = 0; i < 12; i++) {
            const particle = document.createElement('div');
            const angle = (i / 12) * Math.PI * 2;
            const velocity = 50 + Math.random() * 50;
            
            particle.style.cssText = `
                position: fixed;
                width: 8px;
                height: 8px;
                background: ${color};
                border-radius: 50%;
                left: ${centerX}px;
                top: ${centerY}px;
                pointer-events: none;
                z-index: 9999;
                box-shadow: 0 0 10px ${color};
            `;
            
            document.body.appendChild(particle);

            const destX = Math.cos(angle) * velocity;
            const destY = Math.sin(angle) * velocity;

            particle.animate([
                { transform: 'translate(-50%, -50%) scale(1)', opacity: 1 },
                { transform: `translate(calc(-50% + ${destX}px), calc(-50% + ${destY}px)) scale(0)`, opacity: 0 }
            ], {
                duration: 600,
                easing: 'cubic-bezier(0.4, 0, 0.2, 1)'
            }).onfinish = () => particle.remove();
        }
    }

    /**
     * Animate value change with number counting
     * @param {HTMLElement} element - Target element
     * @param {number} from - Start value
     * @param {number} to - End value
     * @param {Object} options - Animation options
     */
    animateNumber(element, from, to, options = {}) {
        const {
            duration = 500,
            decimals = 0,
            locale = 'ar-EG',
            onComplete = null
        } = options;

        if (this.prefersReducedMotion) {
            element.textContent = to.toLocaleString(locale, {
                minimumFractionDigits: decimals,
                maximumFractionDigits: decimals
            });
            if (onComplete) onComplete();
            return;
        }

        const startTime = performance.now();
        
        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease out expo
            const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
            
            const current = from + (to - from) * easeProgress;
            
            element.textContent = current.toLocaleString(locale, {
                minimumFractionDigits: decimals,
                maximumFractionDigits: decimals
            });
            
            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                if (onComplete) onComplete();
            }
        };
        
        requestAnimationFrame(animate);
    }

    /**
     * Add glow pulse to element
     * @param {HTMLElement} element - Target element
     * @param {number} duration - Duration in ms
     */
    pulseGlow(element, duration = 1000) {
        if (this.prefersReducedMotion) return;

        element.animate([
            { boxShadow: '0 0 20px rgba(0, 245, 255, 0.4), 0 0 40px rgba(0, 245, 255, 0.2)' },
            { boxShadow: '0 0 30px rgba(0, 245, 255, 0.6), 0 0 60px rgba(0, 245, 255, 0.4)' },
            { boxShadow: '0 0 20px rgba(0, 245, 255, 0.4), 0 0 40px rgba(0, 245, 255, 0.2)' }
        ], {
            duration: duration,
            easing: 'ease-in-out'
        });
    }

    /**
     * Shake element for error feedback
     * @param {HTMLElement} element - Target element
     */
    shake(element) {
        if (this.prefersReducedMotion) return;

        element.animate([
            { transform: 'translateX(0)' },
            { transform: 'translateX(-5px)' },
            { transform: 'translateX(5px)' },
            { transform: 'translateX(-5px)' },
            { transform: 'translateX(5px)' },
            { transform: 'translateX(0)' }
        ], {
            duration: 400,
            easing: 'ease-in-out'
        });
    }
}

// Export for use in other modules
const animations = new Animations();
