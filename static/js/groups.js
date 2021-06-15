let ag = document.getElementById('all-groups')
let cg = document.getElementById('created-groups')
if (is_creator) {
    tg = document.getElementById('toggle-groups')
    tg.style.display = "block"
}
const btn = document.getElementById("flexSwitchCheckDefault").addEventListener('change',(e)=> {
    if(ag.style.display === "none") {
        ag.style.display = "block"
        cg.style.display = "none"
    }else {
        ag.style.display = "none"
        cg.style.display = "block"
        const grpbtn = document.getElementById('form-btn')
        grpbtn.addEventListener('click', (e) => {
            const labels = document.getElementsByTagName('label')
            console.log(labels)
            labels[1].style.display = 'none'
            labels[2].style.display = 'none'
        })
        const grpnameInput = document.getElementById('id_group_name')
        grpnameInput.setAttribute("placeholder", "Group Name")
        const grpinfoInput = document.getElementById('id_group_info')
        grpinfoInput.setAttribute("placeholder", "Group Info")
    }
})

const errorlist = document.getElementsByClassName('errorlist')
errorlist[0].style.display = 'none'
const errordiv = document.getElementById('error-div')
const errorul = document.createElement('ul')
const errorli = document.createElement('li')
const errormsg = document.createTextNode(errorlist[0].innerText)
errorli.appendChild(errormsg)
errorul.appendChild(errorli)
errordiv.appendChild(errorul)

setTimeout(() => {
    const errordiv = document.getElementById('error-div')
    errordiv.children[1].remove()
}, 3000)


