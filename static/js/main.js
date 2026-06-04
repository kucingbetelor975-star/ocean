// Init AOS animations safely
if (typeof AOS !== 'undefined') {
    try {
        AOS.init({
            once: true,
            duration: 800,
            easing: 'ease-out-cubic'
        });
    } catch (e) {
        console.error("AOS initialization failed:", e);
    }
}

// Programmatic bubble creation
function createBubbles() {
    try {
        const container = document.createElement('div');
        container.className = 'bubble-container';
        document.body.appendChild(container);

        const bubbleCount = 20;
        for (let i = 0; i < bubbleCount; i++) {
            const bubble = document.createElement('div');
            bubble.className = 'bubble';
            
            const size = Math.random() * 25 + 5; // 5px to 30px
            bubble.style.width = `${size}px`;
            bubble.style.height = `${size}px`;
            bubble.style.left = `${Math.random() * 100}%`;
            bubble.style.animationDelay = `${Math.random() * 10}s`;
            bubble.style.animationDuration = `${Math.random() * 8 + 8}s`; // 8s to 16s
            
            container.appendChild(bubble);
        }
    } catch (e) {
        console.error("Bubble creation failed:", e);
    }
}
document.addEventListener("DOMContentLoaded", createBubbles);

// Drag and drop & Preview functionality
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const uploadPlaceholder = document.getElementById('uploadPlaceholder');
const imagePreviewContainer = document.getElementById('imagePreviewContainer');
const imagePreview = document.getElementById('imagePreview');
const fileName = document.getElementById('fileName');
const uploadForm = document.getElementById('uploadForm');
const loadingState = document.getElementById('loadingState');

if (dropZone && fileInput) {
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => dropZone.classList.add('dragover', 'scale-[1.02]'), false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => dropZone.classList.remove('dragover', 'scale-[1.02]'), false);
    });

    dropZone.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if(files && files.length > 0) {
            fileInput.files = files;
            previewFile();
        }
    }
}

function previewFile() {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function() {
            imagePreview.src = reader.result;
            fileName.textContent = file.name;
            uploadPlaceholder.classList.add('hidden');
            imagePreviewContainer.classList.remove('hidden');
        }
    }
}

// Clear selected image / Cancel function without refresh
function clearImage(e) {
    if (e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    if (fileInput) fileInput.value = '';
    if (imagePreview) imagePreview.src = '';
    if (fileName) fileName.textContent = '';
    
    if (imagePreviewContainer) imagePreviewContainer.classList.add('hidden');
    if (uploadPlaceholder) uploadPlaceholder.classList.remove('hidden');
    
    // Hide prediction result overlay if active
    const resultSection = document.getElementById('resultSection');
    if (resultSection) {
        resultSection.remove();
    }
    
    // Re-enable the upload card
    const uploadCard = document.querySelector('.glass-card.group');
    if (uploadCard) {
        uploadCard.classList.remove('opacity-30', 'filter', 'blur-sm', 'pointer-events-none');
    }
}

if (uploadForm && loadingState) {
    uploadForm.addEventListener('submit', function() {
        if(fileInput && fileInput.files.length > 0) {
            loadingState.classList.remove('hidden');
            const scanLine = document.createElement('div');
            scanLine.className = 'scan-line';
            dropZone.appendChild(scanLine);
        }
    });
}

// Chart.js Dashboard Data
document.addEventListener("DOMContentLoaded", function() {
    if (typeof Chart === 'undefined') {
        return;
    }

    const hasHistory = (typeof predictionHistory !== 'undefined' && predictionHistory.length > 0);

    // ==========================================
    // RASIO CHART (DOUGHNUT) - DYNAMICALLY UPDATED
    // ==========================================
    const ctxRatio = document.getElementById('ratioChart');
    if (ctxRatio) {
        let lowCount = 0;
        let midCount = 0;
        let highCount = 0;

        if (hasHistory) {
            lowCount = predictionHistory.filter(r => r.prediction === 'Polusi Rendah').length;
            midCount = predictionHistory.filter(r => r.prediction === 'Polusi Sedang').length;
            highCount = predictionHistory.filter(r => r.prediction === 'Polusi Tinggi').length;
        }

        const dataValues = hasHistory ? [lowCount, midCount, highCount] : [0, 0, 0];
        
        new Chart(ctxRatio, {
            type: 'doughnut',
            data: {
                labels: ['Polusi Rendah', 'Polusi Sedang', 'Polusi Tinggi'],
                datasets: [{
                    data: dataValues,
                    backgroundColor: ['rgba(34, 197, 94, 0.6)', 'rgba(14, 165, 233, 0.6)', 'rgba(239, 68, 68, 0.6)'],
                    borderColor: ['#22c55e', '#0ea5e9', '#ef4444'],
                    borderWidth: 1.5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { 
                        position: 'bottom',
                        labels: { 
                            color: '#e2e8f0',
                            font: {
                                family: 'Inter',
                                size: 12
                            },
                            padding: 15
                        } 
                    }
                },
                cutout: '65%'
            }
        });
    }
});
