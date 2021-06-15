const emailInput = document.getElementById('id_email')
emailInput.setAttribute("placeholder", "email")
emailInput.classList.add("form-control")
emailInput.classList.add("rounded-left")

const usernameInput = document.getElementById('id_username')
usernameInput.setAttribute("placeholder", "username")
usernameInput.classList.add("form-control")
usernameInput.classList.add("rounded-left")

const positionInput = document.getElementById('id_position')
positionInput.setAttribute("placeholder", "Position")
positionInput.setAttribute("aria-label", ".form-select-sm example")
positionInput.classList.add("form-select-sm")
positionInput.classList.add("form-select-sm")
positionInput.classList.add("rounded-left")

let passwordInput = document.getElementById('id_password1')
passwordInput.setAttribute("placeholder", "Password")
passwordInput.classList.add("form-control")
passwordInput.classList.add("rounded-left")
passwordInput = document.getElementById('id_password2')
passwordInput.setAttribute("placeholder", "Confirm Password")
passwordInput.classList.add("form-control")
passwordInput.classList.add("rounded-left")

const form = document.getElementById('signup-form')

setTimeout(() => {
    const errorul = form.getElementsByClassName('errorlist')
    errorul[0].remove()
}, 3000)