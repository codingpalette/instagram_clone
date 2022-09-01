function copy_url(id) {
  function getToastRoot() {
    const modalRoot = document.getElementById('modal-root')
    if (!modalRoot) return

    let toastRoot = modalRoot.getElementsByClassName('docsToastRoot')[0]
    if (!toastRoot) {
      toastRoot = document.createElement('ul')
      toastRoot.classList.add('docsToastRoot')
      modalRoot.appendChild(toastRoot)
    }
    return toastRoot
  }
  function addToast(message) {
    const toastRoot = getToastRoot()
    if (!toastRoot) return

    const toast = document.createElement('li')
    const closeButton = `<button type="button" class="btn_close"><span class="kdc_ico_developers">close</span></button>`
    toast.innerHTML = `<div class="docsToast"><p class="desc_msg">${message}</p>${closeButton}</div>`
    toastRoot.appendChild(toast)
    setTimeout(() => toastRoot.removeChild(toast), 3000)
    toast.querySelector('.btn_close').onclick = () => {
      toastRoot.removeChild(toast)
    }
  }

  const element = document.createElement('textarea')
  element.value = `${location.origin}${location.pathname}#${id}`
  element.setAttribute('readonly', '')
  element.style.position = 'absolute'
  element.style.left = '-9999px'
  document.body.appendChild(element)
  element.select()
  document.execCommand('copy')
  document.body.removeChild(element)
  addToast(
    docs_lang === 'en' ? 'Copied to clipboard.' : '클립보드에 복사했습니다.'
  )
}
