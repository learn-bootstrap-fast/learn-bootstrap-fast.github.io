// Add your custom JavaScript here

// Stats Counter Animation
function animateCounter(counter) {
    const target = +counter.getAttribute('data-count');
    const duration = 1500;
    const start = 0;
    let startTimestamp = null;
    function step(timestamp) {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (target - start) + start);
        counter.textContent = value + (target >= 1000 ? '+' : '');
        if (progress < 1) {
            window.requestAnimationFrame(step);
        } else {
            counter.textContent = target + (target >= 1000 ? '+' : '');
        }
    }
    window.requestAnimationFrame(step);
}

function handleStatsCounters() {
    const counters = document.querySelectorAll('.stat-number');
    const options = { threshold: 0.6 };
    const observer = new window.IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                obs.unobserve(entry.target);
            }
        });
    }, options);
    counters.forEach(counter => observer.observe(counter));
}

document.addEventListener('DOMContentLoaded', handleStatsCounters);
