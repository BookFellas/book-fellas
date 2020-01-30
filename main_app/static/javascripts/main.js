document.addEventListener("DOMContentLoaded", function() {
    (function() {
        var _btn = document.querySelector(".btn-slide-bar"),
            _body = document.querySelector("body");
        _btn.onmouseover = function() {
            _body.classList.toggle("active");
        }
    })(window)
}, false);