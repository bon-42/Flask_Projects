// Function to hide elements
function hideElement(selector) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => element.style.display = 'none');
}

// Hide YouTube comments
hideElement('#comments');

// Hide YouTube recommended videos (sidebar)
hideElement('#related');

// Hide YouTube recommended videos (below the video)
hideElement('ytd-watch-next-secondary-results-renderer');

// Optional: Hide YouTube end screen recommendations
hideElement('.ytp-endscreen-content');

// Observe changes in the page and hide comments and recommendations if they reappear
const observer = new MutationObserver(() => {
    hideElement('#comments');
    hideElement('#related');
    hideElement('ytd-watch-next-secondary-results-renderer');
    hideElement('.ytp-endscreen-content');
});

observer.observe(document.body, { childList: true, subtree: true });