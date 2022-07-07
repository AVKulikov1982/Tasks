window.addEventListener('DOMContentLoaded', function () {

    let inputs = document.querySelectorAll('input')
       for (i = 0; i < inputs.length; i++) {
           inputs[i].setAttribute('autocomplete','off')
       }

    if (document.querySelector('#click_change_responsible')) {
        document.querySelector('#click_change_responsible').addEventListener('click', function (event) {
            document.querySelector('#change_responsible').classList.add('is-active')
        });
        document.querySelector('#click_save_change_responsible').addEventListener('click', function (event) {
            document.querySelector('#change_responsible').classList.remove('is-active')
        });
    }

    if (document.querySelector('#filter')) {
        document.querySelector('#filter').addEventListener('click', function (event) {
            document.querySelector('#filter_dropdown').classList.add('is-active-dropdown')
        });
        document.querySelector('#close').addEventListener('click', function (event) {
            document.querySelector('#filter_dropdown').classList.remove('is-active-dropdown')
        });
    }

    if (document.getElementsByClassName('content__header-row')) {
        let elems = document.getElementsByClassName('content__header-row');
        for (i = 0; i < elems.length; i++) {
            let elem = elems[i].textContent.trim().split('\n')

            if (elem[elem.length - 1].trim() === 'просрочена') {
                red.call(elems[i])
            }
            else if (elem[elem.length - 1].trim() === 'закрыта') {
                grey.call(elems[i])
            }
        }
    }
});

function red() {
    this.style.color = 'red';
}

function grey() {
    this.style.color = '#c0c0c0';
}