document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.dropdown').forEach(function(dropdown) {
        dropdown.addEventListener('mouseover', function() {
            dropdown.querySelector('.dropdown-content').style.display = 'block';
        });
        dropdown.addEventListener('mouseout', function() {
            dropdown.querySelector('.dropdown-content').style.display = 'none';
        });
    });
});
