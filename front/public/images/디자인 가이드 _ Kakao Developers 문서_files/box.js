;(function () {
  'use strict'
  window.addEventListener('DOMContentLoaded', function () {
    const boxButtons = document.querySelectorAll(
      '.box_sign.collapse .collapse_btn'
    )
    const docsRoot = document.querySelector('#docsRoot')

    function findBoxArea(target, root) {
      if (target == undefined) return
      if (target == root) return
      if (target.classList.contains('box_sign')) return target
      return findBoxArea(target.parentElement, root)
    }

    function initBox() {
      boxButtons.forEach((boxButton) => {
        boxButton.addEventListener('click', function (e) {
          const boxArea = findBoxArea(this, docsRoot)
          if (boxArea) {
            boxArea.classList.toggle('open_on')
          }
          const description = this.nextElementSibling
          if (description) {
            description.style.maxHeight = description.style.maxHeight
              ? null
              : description.scrollHeight + 'px'
          }
        })
      })
    }

    initBox()
  })
})()
