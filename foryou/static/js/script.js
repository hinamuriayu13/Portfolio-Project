document.addEventListener('DOMContentLoaded', () => {
    const toggleButtons = document.querySelectorAll('.toggle-btn');
    const forms = document.querySelectorAll('.form-content');

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetForm = document.getElementById(button.getAttribute('data-target'));

            forms.forEach(form => form.classList.add('hidden'));
            targetForm.classList.remove('hidden');

            toggleButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });
});