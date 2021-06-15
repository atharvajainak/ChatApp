const emailInput = document.getElementById('id_email')
emailInput.setAttribute("placeholder", "email")
emailInput.classList.add("form-control")
emailInput.classList.add("rounded-left")

const passwordInput = document.getElementById('id_password')
passwordInput.setAttribute("placeholder", "Password")
passwordInput.classList.add("form-control")
passwordInput.classList.add("rounded-left")

setTimeout(() => {
    const errordiv = document.getElementById('error-div')
    errordiv.children[0].remove()
}, 3000)